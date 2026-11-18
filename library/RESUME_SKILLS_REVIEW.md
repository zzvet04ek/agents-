# Подключение ResumeSkills

Источник: https://github.com/Paramchoudhary/ResumeSkills.
Зафиксированный коммит: `74ae19e7c62b0516d1c298328e5544976c12da5d`.
Лицензия: MIT; корневой LICENSE скопирован, инструкции сохранены без изменений.

## Состав и пересечения

Фактически найдено и подключено **22 навыка**, хотя исходный README перечисляет 20. В библиотеке теперь **1055 навыков из 9 коллекций**. Это инструкции для библиотекаря; отдельные работающие агенты не создаются.

Точные совпадения имён с существующими навыками: **0**. Побайтово одинаковые SKILL.md: **0**. Тематическое пересечение с career не трактуется как полная взаимозаменяемость.

| Новый навык | Основной маршрут для обычного запроса | Доступ к новому варианту |
|---|---|---|
| `resume-skills/academic-cv-builder` | `career/academic-research-cv` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/application-form-filler` | `resume-skills/application-form-filler` | основной вариант для этой специализированной задачи |
| `resume-skills/career-changer-translator` | `career/career-pivot-planner` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/cold-email-writer` | `resume-skills/cold-email-writer` | основной вариант для этой специализированной задачи |
| `resume-skills/cover-letter-generator` | `career/cover-letter-writer` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/creative-portfolio-resume` | `resume-skills/creative-portfolio-resume` | основной вариант для этой специализированной задачи |
| `resume-skills/executive-resume-writer` | `career/executive-leadership-resume` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/interview-prep-generator` | `career/mock-interview-coach` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/job-description-analyzer` | `career/job-fit-analyzer` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/linkedin-profile-optimizer` | `career/linkedin-profile-booster` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/offer-comparison-analyzer` | `resume-skills/offer-comparison-analyzer` | основной вариант для этой специализированной задачи |
| `resume-skills/portfolio-case-study-writer` | `career/portfolio-case-study` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/reference-list-builder` | `resume-skills/reference-list-builder` | основной вариант для этой специализированной задачи |
| `resume-skills/resume-ats-optimizer` | `career/ats-resume-checker` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/resume-bullet-writer` | `resume-skills/resume-bullet-writer` | основной вариант для этой специализированной задачи |
| `resume-skills/resume-formatter` | `resume-skills/resume-formatter` | основной вариант для этой специализированной задачи |
| `resume-skills/resume-quantifier` | `resume-skills/resume-quantifier` | основной вариант для этой специализированной задачи |
| `resume-skills/resume-section-builder` | `resume-skills/resume-section-builder` | основной вариант для этой специализированной задачи |
| `resume-skills/resume-tailor` | `career/resume-customizer` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/resume-version-manager` | `resume-skills/resume-version-manager` | основной вариант для этой специализированной задачи |
| `resume-skills/salary-negotiation-prep` | `career/compensation-negotiator` | полный ID или слово ResumeSkills в запросе |
| `resume-skills/tech-resume-optimizer` | `career/software-engineer-resume` | полный ID или слово ResumeSkills в запросе |

В `routing.yaml` описаны 22 карьерных правила. Все 12 навыков исходной коллекции career сохраняют свои базовые задачи. Десять новых специализированных маршрутов используют ResumeSkills по умолчанию. Новые варианты не добавлены в избранное: по-прежнему загружается один библиотекарь, а остальные инструкции читаются по задаче.

## Применение исходных рекомендаций

Исходник resume-quantifier предлагает оценивать показатели при отсутствии точных данных; используйте только оценки с понятным основанием и подтверждением кандидата, не выдумывайте достижения. Проценты соответствия вакансии и оценки ATS — эвристики, не вероятность найма и не гарантия прохождения ATS. Утверждения README о росте числа интервью не включены в русские описания как доказанные результаты.

Оба библиотекаря содержат эти условия применения. Анкеты, письма и обновления профиля готовятся как черновики; подключение коллекции не отправляет сообщения и не публикует данные.

## Проверки

- 22/22 русских описания: суть, возможности, задачи, связанные навыки; категория career.
- 25 новых сценариев выбора плюс 30 существующих: 55 задач, по три повтора, без ошибок.
- Проверка известных идентификаторов и связей, лицензии MIT и закреплённого коммита.
- Лицензионный эталон пополнен только 22 новыми записями; прежние записи не менялись.
- Сторонние установщики, скрипты и реальные процессы отправки заявок не запускались.

Политика работы библиотеки описана в `GOVERNANCE.md`. Эта интеграция построена поверх научной коллекции и оптимизации из PR #2 и PR #3.
