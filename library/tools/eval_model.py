#!/usr/bin/env python3
"""Run an independent JSON-in/JSON-out model adapter per case and repeat.

Example: python3 library/tools/eval_model.py --runner library/tools/codex_route_runner.py --output /tmp/model-eval.json
No execution without an explicit runner. Expected answers are never passed to it.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import yaml
import library as lib
import governance as gov


def evaluate(runner, cases, *, repeats=3, timeout=120):
    routes=gov.load_routes(lib)
    skills={gov.skill_id(s):{'license':s['license'],'noncommercial':lib.is_nc(s['license'])} for s in lib.collect_skills()}
    routed={r['primary'] for r in routes}|{a['skill'] for r in routes for a in r.get('alternatives',[])}
    records=[]
    for case in cases:
        explicit=set(re.findall(r'[a-z0-9-]+/[a-z0-9-]+',case['query']))
        payload={'query':case['query'],'available':case.get('available'), 'commercial':case.get('commercial',False),
                 'routes':routes,'skills':{k:skills[k] for k in sorted(routed|explicit) if k in skills}}
        for repeat in range(repeats):
            start=time.monotonic()
            record={'case':case['id'],'repeat':repeat+1}
            try:
                completed=subprocess.run([str(runner)],input=json.dumps(payload,ensure_ascii=False),text=True,
                                         capture_output=True,timeout=timeout,check=True)
                answer=json.loads(completed.stdout)
                if answer.get('status') not in {'selected','blocked','no_route','ambiguous'}:
                    raise ValueError('invalid result status')
                if answer.get('primary') is not None and answer['primary'] not in skills:
                    raise ValueError('runner returned unknown skill ID')
                record.update(answer=answer,correct=answer.get('primary')==case.get('expected') and answer['status']==case.get('status','selected'))
            except (subprocess.CalledProcessError,subprocess.TimeoutExpired,ValueError) as exc:
                record.update(error=type(exc).__name__,detail=str(exc)[:500],correct=False)
                record['elapsed_seconds']=round(time.monotonic()-start,3)
                records.append(record)
                return summarize(records,cases,repeats,complete=False)
            record['elapsed_seconds']=round(time.monotonic()-start,3)
            records.append(record)
    return summarize(records,cases,repeats,complete=True)


def summarize(records,cases,repeats,*,complete):
    stable=0
    for case in cases:
        answers=[(r['answer'].get('primary'),r['answer']['status']) for r in records if r['case']==case['id'] and 'answer' in r]
        stable+=len(answers)==repeats and len(set(answers))==1
    return {'kind':'external-runner evaluation; runner identity must be verified separately',
            'completed_at':datetime.now(timezone.utc).isoformat(),'complete':complete,'cases':len(cases),
            'repeats':repeats,'attempted':len(records),'correct':sum(r.get('correct',False) for r in records),
            'stable_cases':stable,'records':records}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runner',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--repeats',type=int,default=3)
    parser.add_argument('--case',help='Run one case ID (use for a smoke test before a full run)')
    parser.add_argument('--timeout',type=int,default=120)
    args=parser.parse_args()
    if args.repeats<2 or args.timeout<1:parser.error('repeats >= 2 and timeout >= 1 required')
    cases=yaml.safe_load((lib.LIB/'evals/routing.yaml').read_text())['cases']
    if args.case:cases=[c for c in cases if c['id']==args.case]
    if not cases:parser.error('no matching cases')
    result=evaluate(args.runner.resolve(),cases,repeats=args.repeats,timeout=args.timeout)
    result['runner']=str(args.runner)
    result['library_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=lib.REPO,text=True).strip()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},ensure_ascii=False,indent=2))
    return 0 if result['complete'] and result['correct']==len(cases)*args.repeats else 1


if __name__=='__main__':sys.exit(main())
