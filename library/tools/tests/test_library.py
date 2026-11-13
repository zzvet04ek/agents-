import contextlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import library as lib
import governance as gov


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.library = self.root / 'library'
        self.cols = self.library / 'collections'
        self.cols.mkdir(parents=True)
        self.patch = patch.multiple(lib, REPO=self.root, LIB=self.library, COLLECTIONS=self.cols,
                                    SOURCES=self.library/'sources.yaml', LOCK=self.library/'sources.lock.json',
                                    FAVORITES=self.library/'favorites.yaml', RU_DIR=self.library/'ru',
                                    INDEX=self.library/'INDEX.md', CATALOG=self.library/'CATALOG.md',
                                    RU_OUT=self.library/'SKILLS_RU.md',
                                    ACTIVE_DIRS=(self.root/'.claude/skills', self.root/'.agents/skills'))
        self.patch.start()
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(self.patch.stop)
        lib.SOURCES.write_text('collections: {}\n')
        lib.FAVORITES.write_text('favorites: []\n')

    def skill(self, cid='alpha', name='copywriting', license='MIT'):
        path = self.cols/cid/name/'SKILL.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'---\nname: {name}\ndescription: Fixture description\n---\n\nUse assets/example.txt.\n')
        (path.parent/'assets').mkdir(exist_ok=True)
        (path.parent/'assets/example.txt').write_text('source asset')
        return {'collection':cid, 'name':name, 'path':str(path.relative_to(self.root)),
                'description':'Fixture description', 'license':license, 'category':''}

    def favorites(self, *ids):
        lib.FAVORITES.write_text(yaml.safe_dump({'favorites':list(ids)}))

    def apply(self, skills):
        with contextlib.redirect_stdout(io.StringIO()):
            lib.apply_favorites(skills)


class FavoritesTests(Fixture):
    def test_two_colliding_sources_install_both_hosts_and_keep_originals(self):
        a,b = self.skill(),self.skill('beta')
        self.favorites('alpha/copywriting','beta/copywriting')
        for active in lib.ACTIVE_DIRS:
            old=active/'copywriting';old.mkdir(parents=True)
            (old/lib.FAVORITE_MARKER).write_text('alpha/copywriting\n')
            manual=active/'skill-library';manual.mkdir();(manual/'SKILL.md').write_text('manual')
        self.apply([a,b]);self.apply([b,a])
        for active in lib.ACTIVE_DIRS:
            self.assertFalse((active/'copywriting').exists())
            self.assertEqual((active/'skill-library/SKILL.md').read_text(),'manual')
            for cid in ('alpha','beta'):
                path=active/f'{cid}-copywriting/SKILL.md'
                self.assertEqual(lib.parse_frontmatter(path.read_text())['name'],f'{cid}-copywriting')
                self.assertIn(f'library/collections/{cid}/copywriting/SKILL.md',path.read_text())
                self.assertEqual((self.cols/cid/'copywriting/assets/example.txt').read_text(),'source asset')
        self.favorites();self.apply([a,b])
        self.assertTrue(all(list(p.iterdir())==[p/'skill-library'] for p in lib.ACTIVE_DIRS))

    def test_unknown_or_ambiguous_id_does_not_remove_previous_install(self):
        a,b=self.skill(),self.skill('beta')
        self.favorites('alpha/copywriting');self.apply([a,b])
        for bad in ('copywriting','missing/copywriting'):
            self.favorites(bad)
            with self.assertRaises(ValueError):self.apply([a,b])
            self.assertTrue(all((p/'alpha-copywriting/SKILL.md').exists() for p in lib.ACTIVE_DIRS))

    def test_second_host_manual_conflict_preserves_first_host(self):
        a=self.skill();self.favorites('alpha/copywriting');self.apply([a])
        self.favorites('beta/copywriting');b=self.skill('beta')
        manual=lib.ACTIVE_DIRS[1]/'custom';manual.mkdir()
        (manual/'SKILL.md').write_text('---\nname: beta-copywriting\n---\nManual')
        with self.assertRaises(ValueError):self.apply([a,b])
        self.assertTrue((lib.ACTIVE_DIRS[0]/'alpha-copywriting/SKILL.md').exists())
        self.assertIn('Manual',(manual/'SKILL.md').read_text())

    def test_long_names_and_nc_notice(self):
        a=self.skill('alpha','x'*80,'PolyForm-Noncommercial-1.0.0')
        self.favorites('alpha/'+'x'*80);self.apply([a])
        path=next(lib.ACTIVE_DIRS[0].glob('*/SKILL.md'))
        self.assertLessEqual(len(path.parent.name),64)
        self.assertIn('Non-commercial use only',path.read_text())


class RoutingTests(Fixture):
    def setUp(self):
        super().setUp()
        self.skills=[self.skill('alpha','research','CC-BY-NC-4.0'),self.skill('beta','research')]
        self.routes=[{'id':'research','primary':'alpha/research','match':['исследован'],
                      'requires':['api-a'],'alternatives':[{'skill':'beta/research','requires':['api-b']}]}]
        (self.library/'routing.yaml').write_text(yaml.safe_dump({'routes':self.routes}))

    def resolve(self, query='исследование', **kwargs):
        return gov.resolve(lib,query,skills=self.skills,**kwargs)

    def test_tools_and_commercial_gate_choose_documented_alternative(self):
        self.assertEqual(self.resolve(available={'api-a'})['primary'],'alpha/research')
        self.assertEqual(self.resolve(available={'api-b'},commercial=True)['primary'],'beta/research')
        self.assertEqual(self.resolve(available=set())['status'],'blocked')
        self.assertEqual(self.resolve()['status'],'blocked')

    def test_explicit_selection_is_not_substituted(self):
        self.assertEqual(self.resolve('beta/research',available={'api-b'})['primary'],'beta/research')
        self.assertEqual(self.resolve('alpha/research',available={'api-a','api-b'},commercial=True)['status'],'blocked')
        self.assertEqual(self.resolve('unknown/research',available=set())['status'],'blocked')

    def test_unknown_and_equal_routes_fail_clearly(self):
        self.assertEqual(self.resolve('расскажи анекдот')['status'],'no_route')
        self.routes.append({'id':'other','primary':'beta/research','match':['исследован']})
        (self.library/'routing.yaml').write_text(yaml.safe_dump({'routes':self.routes}))
        self.assertEqual(self.resolve()['status'],'ambiguous')


class RegistryTests(Fixture):
    def test_nested_copies_are_one_logical_agent_with_all_paths(self):
        skill=self.skill()
        paths=[self.cols/'alpha/agents/common.md',self.cols/'alpha/copywriting/agents/nested/common.md']
        for path in paths:path.parent.mkdir(parents=True,exist_ok=True);path.write_text('---\nname: shared\ntools: [Read]\n---\nRole')
        agents=gov.agent_inventory(lib,[skill])
        self.assertEqual(len(agents),1)
        self.assertEqual(len(agents[0]['paths']),2)
        self.assertEqual(agents[0]['owner_skills'],['alpha/copywriting'])
        original=agents[0]['id'];paths[1].write_text('Different instructions')
        changed=gov.agent_inventory(lib,[skill])
        self.assertEqual(len(changed),2)
        self.assertIn(original,[a['id'] for a in changed])


class RestoreTests(Fixture):
    def git(self,*args,cwd=None):
        return subprocess.check_output(['git',*args],cwd=cwd,text=True,stderr=subprocess.DEVNULL).strip()

    def test_restore_uses_pinned_commit_after_remote_head_moves_and_keeps_my(self):
        remote=self.root/'remote';remote.mkdir();self.git('init','-q',cwd=remote)
        path=remote/'skills/example/SKILL.md';path.parent.mkdir(parents=True)
        path.write_text('---\nname: example\ndescription: first\n---\nFirst version')
        self.git('add','.',cwd=remote)
        self.git('-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','first',cwd=remote)
        first=self.git('rev-parse','HEAD',cwd=remote)
        spec={'repo':str(remote),'include':['skills'],'license':'MIT'}
        config={'collections':{'alpha':spec}}
        lib.SOURCES.write_text(yaml.safe_dump(config))
        lock={'alpha':{'repo':str(remote),'ref':None,'license':'MIT','commit':first,'config_sha256':lib.source_config_digest(spec,{})}}
        lib.LOCK.write_text(json.dumps(lock));before=lib.LOCK.read_bytes()
        path.write_text('Changed remote head')
        self.git('add','.',cwd=remote)
        self.git('-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','second',cwd=remote)
        own=self.cols/'my/keep.txt';own.parent.mkdir();own.write_text('mine')
        with patch.object(lib,'cmd_index'),contextlib.redirect_stdout(io.StringIO()):lib.cmd_restore([])
        self.assertIn('First version',(self.cols/'alpha/skills/example/SKILL.md').read_text())
        self.assertEqual(lib.LOCK.read_bytes(),before)
        self.assertEqual(own.read_text(),'mine')
        config['collections']['alpha']['include']=['other']
        lib.SOURCES.write_text(yaml.safe_dump(config))
        with self.assertRaises(ValueError):lib.cmd_restore([])
        self.assertIn('First version',(self.cols/'alpha/skills/example/SKILL.md').read_text())


class AuditTests(Fixture):
    def test_changed_license_and_broken_related_skill_are_reported(self):
        self.skill('my','example')
        lib.RU_DIR.mkdir();(lib.RU_DIR/'skills').mkdir()
        (lib.RU_DIR/'categories.yaml').write_text('other: {}\n')
        (lib.RU_DIR/'skills/test.yaml').write_text('my/example:\n  cat: other\n  with: missing/skill\n')
        (self.library/'audit-baseline.json').write_text(json.dumps({'licenses':{'my/example':{'effective':'MIT','declared':''}}}))
        result=gov.audit(lib)
        self.assertTrue(any('license changed' in e for e in result['errors']))
        self.assertTrue(any('broken related skill' in e for e in result['errors']))


class FailureRecoveryTests(Fixture):
    def test_second_host_io_failure_rolls_back_both_hosts(self):
        a,b=self.skill(),self.skill('beta')
        self.favorites('alpha/copywriting');self.apply([a,b])
        self.favorites('beta/copywriting')
        original=Path.rename
        failed=False
        def fail_once(path,target):
            nonlocal failed
            if not failed and Path(target)==lib.ACTIVE_DIRS[1]/'beta-copywriting':
                failed=True
                raise OSError('simulated host write failure')
            return original(path,target)
        with patch.object(Path,'rename',fail_once),self.assertRaises(OSError):self.apply([a,b])
        for active in lib.ACTIVE_DIRS:
            self.assertTrue((active/'alpha-copywriting/SKILL.md').exists())
            self.assertFalse((active/'beta-copywriting').exists())


class ModelHarnessTests(Fixture):
    def test_expected_answers_not_sent_and_repetitions_scored(self):
        import eval_model
        a=self.skill()
        runner=self.root/'runner.py'
        runner.write_text('#!/usr/bin/env python3\nimport sys,json\np=json.load(sys.stdin)\nassert "expected" not in p\nprint(json.dumps({"primary":"alpha/copywriting","status":"selected"}))\n')
        runner.chmod(0o755)
        cases=[{'id':'one','query':'alpha/copywriting','expected':'alpha/copywriting'}]
        with patch.object(lib,'collect_skills',return_value=[a]):
            result=eval_model.evaluate(runner,cases,repeats=3)
        self.assertTrue(result['complete'])
        self.assertEqual(result['correct'],3)
        self.assertEqual(result['stable_cases'],1)

    def test_runner_failure_stops_without_claiming_completed_series(self):
        import eval_model
        a=self.skill();runner=self.root/'fail.py'
        runner.write_text('#!/usr/bin/env python3\nraise SystemExit(2)\n');runner.chmod(0o755)
        cases=[{'id':'one','query':'alpha/copywriting','expected':'alpha/copywriting'}]
        with patch.object(lib,'collect_skills',return_value=[a]):
            result=eval_model.evaluate(runner,cases,repeats=3)
        self.assertFalse(result['complete'])
        self.assertEqual(result['attempted'],1)
        self.assertEqual(result['correct'],0)


if __name__=='__main__':unittest.main()
