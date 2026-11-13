# Навыки библиотеки — описание по категориям

Генерируется `library/tools/library.py index` из `library/ru/`. Правьте описания в `library/ru/skills/*.yaml`, не здесь.

Описано навыков: **1033** из 1033.

Для каждого навыка: суть, ключевые навыки, решаемые задачи и с чем сочетать. Идентификатор `коллекция/имя` можно назвать Claude напрямую: «возьми навык marketing/copywriting».

## Содержание

| Категория | Навыков |
|---|---|
| [Backend-разработка, языки и фреймворки](#cat-dev-backend) | 35 |
| [Frontend, UI и дизайн интерфейсов](#cat-dev-frontend) | 25 |
| [Мобильная и десктопная разработка](#cat-dev-mobile) | 13 |
| [Тестирование и контроль качества кода](#cat-testing) | 52 |
| [Безопасность](#cat-security) | 26 |
| [DevOps, инфраструктура, деплой и мониторинг](#cat-devops) | 35 |
| [Базы данных, данные и аналитика](#cat-data) | 37 |
| [AI, LLM и агентные системы](#cat-ai-agents) | 98 |
| [Архитектура, планирование и процесс разработки](#cat-eng-process) | 49 |
| [Настройка Claude Code и экосистемы ECC](#cat-claude-setup) | 44 |
| [Документация и управление знаниями](#cat-docs) | 20 |
| [Контент, тексты и бренд](#cat-content) | 17 |
| [Маркетинг, SEO и рост](#cat-marketing) | 90 |
| [Продажи, клиенты и поддержка](#cat-sales) | 26 |
| [Продакт-менеджмент](#cat-product) | 61 |
| [Управление проектами и командами](#cat-project) | 14 |
| [Стратегия бизнеса и C-level](#cat-strategy) | 65 |
| [Финансы, биллинг и инвестиции](#cat-finance) | 21 |
| [Регуляторика, комплаенс и качество (QMS)](#cat-compliance) | 34 |
| [Операции, логистика и закупки](#cat-operations) | 13 |
| [Карьера и HR](#cat-career) | 20 |
| [Исследования и наука](#cat-research) | 57 |
| [Личная продуктивность и коммуникации](#cat-productivity) | 23 |
| [Видео, графика и мультимедиа](#cat-media) | 27 |
| [Сети и homelab](#cat-network) | 10 |
| [Блокчейн, Web3 и трейдинг](#cat-web3) | 8 |
| [Медицина и здравоохранение](#cat-healthcare) | 21 |
| [Биоинформатика, геномика и исследовательские изображения](#cat-bioinformatics) | 47 |
| [Химия, молекулярное моделирование и белки](#cat-chemistry) | 18 |
| [Физика, материалы и научные вычисления](#cat-scientific-computing) | 17 |
| [Лабораторная автоматизация и оборудование](#cat-lab-automation) | 10 |

---

<a id="cat-dev-backend"></a>
## Backend-разработка, языки и фреймворки

**Область применения.** Серверная логика, API и бизнес-код на Python, Node.js/TypeScript, Go, Rust, Java/Kotlin, C#, C++, PHP, Ruby, Perl и их фреймворках (Django, FastAPI, Spring Boot, Quarkus, Laravel, Rails, NestJS, Ktor).

**Решаемые задачи.** Написание идиоматичного кода по стандартам языка; проектирование REST/GraphQL API; работа с ORM; фоновые задачи; обработка ошибок; ревью кода и рефакторинг.

**Типовые связки.** *-patterns (как писать) → *-tdd / *-testing (тесты сначала) → *-security (защита) → *-verification (финальная проверка перед релизом); api-design + contract-first для согласования интерфейсов.

Навыков в категории: 35.

### `ecc/api-connector-builder`

Добавление нового API-коннектора или провайдера строго по образцу уже существующих интеграций проекта.

- **Ключевые навыки:** анализ существующего паттерна интеграций; повторение структуры без второй архитектуры.
- **Задачи:** подключить ещё один внешний сервис так же, как подключены остальные.
- **Сочетается с:** `ecc/api-design`, `ecc/error-handling`, `ecc/contract-first`

### `claude-skills/api-design-reviewer`

Ревью PR и спецификаций, меняющих REST API.

- **Ключевые навыки:** линтер соглашений; детектор ломающих изменений; оценка дизайна.
- **Задачи:** не допустить плохих или ломающих изменений API.
- **Сочетается с:** `ecc/api-design`, `claude-skills/api-test-suite-builder`

### `ecc/api-design`

Паттерны проектирования REST API для продакшена.

- **Ключевые навыки:** именование ресурсов; коды статусов; пагинация и фильтрация; формат ошибок; версионирование; rate limiting.
- **Задачи:** спроектировать или отревьюить REST-эндпоинты.
- **Сочетается с:** `ecc/contract-first`, `ecc/backend-patterns`, `ecc/error-handling`

### `ecc/backend-patterns`

Архитектура бэкенда на Node.js, Express и API-роутах Next.js.

- **Ключевые навыки:** структура API; доступ к данным; оптимизация запросов к БД; серверные лучшие практики.
- **Задачи:** построить или отревьюить серверную часть на Node.js.
- **Сочетается с:** `ecc/api-design`, `ecc/postgres-patterns`, `ecc/error-handling`

### `claude-skills/boost-asio-pro`

Сетевой C++-код на Boost.Asio и standalone Asio.

- **Ключевые навыки:** TCP/UDP; SSL; таймеры; strands; io_context; корутины co_spawn и awaitable.
- **Задачи:** писать и отлаживать сетевой C++-код.
- **Сочетается с:** `ecc/cpp-coding-standards`, `ecc/latency-critical-systems`

### `ecc/bun-runtime`

Bun как рантайм, менеджер пакетов, бандлер и тест-раннер.

- **Ключевые навыки:** выбор между Bun и Node; миграция; поддержка на Vercel.
- **Задачи:** решить, переходить ли на Bun, и выполнить переход.
- **Сочетается с:** `ecc/typescript-patterns`, `ecc/vite-patterns`

### `ecc/content-hash-cache-pattern`

Кэширование результатов дорогой обработки файлов по SHA-256 содержимого.

- **Ключевые навыки:** кэш, не зависящий от пути; автоматическая инвалидация; отдельный сервисный слой.
- **Задачи:** ускорить повторную обработку файлов.
- **Сочетается с:** `ecc/redis-patterns`, `ecc/benchmark-optimization-loop`

### `ecc/cpp-coding-standards`

Стандарты C++ на основе C++ Core Guidelines.

- **Ключевые навыки:** современный безопасный C++; идиомы; владение ресурсами.
- **Задачи:** писать, ревьюить и рефакторить C++-код.
- **Сочетается с:** `ecc/cpp-testing`, `ecc/latency-critical-systems`

### `ecc/django-celery`

Фоновые задачи Django и Celery.

- **Ключевые навыки:** конфигурация; дизайн задач; beat-расписания; ретраи; canvas; мониторинг и тесты.
- **Задачи:** добавить фоновые и периодические задачи в Django.
- **Сочетается с:** `ecc/django-patterns`, `ecc/redis-patterns`, `ecc/django-tdd`

### `ecc/django-patterns`

Архитектура Django — DRF, ORM, кэширование, сигналы, middleware.

- **Ключевые навыки:** REST API на DRF; эффективные запросы ORM; кэш; структура продакшен-приложения.
- **Задачи:** построить или отревьюить Django-приложение.
- **Сочетается с:** `ecc/django-tdd`, `ecc/django-security`, `ecc/django-verification`

### `ecc/dotnet-patterns`

Идиоматичный C# и .NET.

- **Ключевые навыки:** соглашения; DI; async/await; надёжная архитектура.
- **Задачи:** писать и ревьюить .NET-приложения.
- **Сочетается с:** `ecc/csharp-testing`, `ecc/error-handling`

### `claude-skills/email-template-builder`

Транзакционные письма — шаблоны React Email, Resend, Postmark, SendGrid, SES.

- **Ключевые навыки:** превью; локализация; тёмная тема; доставляемость.
- **Задачи:** сделать красивые и доставляемые системные письма.
- **Сочетается с:** `ecc/mailtrap-email-integration`

### `claude-skills/embedded-iot-mentor`

Наставник по встраиваемым и IoT-проектам — ESP32, STM32, Arduino, Pico.

- **Ключевые навыки:** прошивки; печатные платы; MQTT; Home Assistant; дашборды датчиков.
- **Задачи:** собрать и запрограммировать устройство.
- **Сочетается с:** `ecc/homelab-network-setup`

### `ecc/error-handling`

Надёжная обработка ошибок в TypeScript, Python и Go.

- **Ключевые навыки:** типизированные ошибки; error boundaries; ретраи; circuit breaker; понятные пользователю сообщения.
- **Задачи:** спроектировать типы ошибок и стратегию отказоустойчивости.
- **Сочетается с:** `ecc/api-design`, `ecc/backend-patterns`, `ecc/python-patterns`

### `ecc/fastapi-patterns`

Лучшие практики FastAPI.

- **Ключевые навыки:** структура проекта; схемы Pydantic v2; внедрение зависимостей; асинхронные обработчики; аутентификация; транзакционный сервисный слой.
- **Задачи:** построить или отревьюить сервис на FastAPI.
- **Сочетается с:** `ecc/python-patterns`, `ecc/python-testing`, `ecc/api-design`

### `ecc/generating-python-installer`

Сборка компактного коммерческого установщика Python-приложения для Windows.

- **Ключевые навыки:** компиляция Nuitka; уменьшение дистрибутива; анализ DLL; упаковка Inno Setup.
- **Задачи:** выпустить Python-программу как обычное Windows-приложение.
- **Сочетается с:** `ecc/python-patterns`, `ecc/windows-desktop-e2e`

### `ecc/golang-patterns`

Идиоматичный Go.

- **Ключевые навыки:** соглашения языка; обработка ошибок; конкурентность; структура пакетов.
- **Задачи:** писать и ревьюить Go-код.
- **Сочетается с:** `ecc/golang-testing`, `ecc/error-handling`

### `ecc/java-coding-standards`

Стандарты Java для сервисов на Spring Boot и Quarkus.

- **Ключевые навыки:** именование; неизменяемость; Optional; стримы; исключения; дженерики; реактивные паттерны.
- **Задачи:** писать и ревьюить Java-код.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/quarkus-patterns`, `ecc/jpa-patterns`

### `ecc/kotlin-ktor-patterns`

Серверы на Ktor.

- **Ключевые навыки:** роутинг; плагины; аутентификация; Koin; kotlinx.serialization; WebSocket; тестирование.
- **Задачи:** построить серверное приложение на Ktor.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/kotlin-exposed-patterns`

### `ecc/kotlin-patterns`

Идиоматичный Kotlin.

- **Ключевые навыки:** null safety; корутины; DSL; соглашения.
- **Задачи:** писать и ревьюить Kotlin-код.
- **Сочетается с:** `ecc/kotlin-testing`, `ecc/kotlin-coroutines-flows`

### `ecc/laravel-patterns`

Архитектура Laravel.

- **Ключевые навыки:** маршруты и контроллеры; Eloquent; сервисный слой; очереди; события; кэш; API-ресурсы.
- **Задачи:** построить или отревьюить Laravel-приложение.
- **Сочетается с:** `ecc/laravel-tdd`, `ecc/laravel-security`, `ecc/laravel-verification`

### `ecc/laravel-plugin-discovery`

Поиск и оценка пакетов Laravel через LaraPlugins.io MCP.

- **Ключевые навыки:** здоровье пакета; совместимость с версиями PHP и Laravel.
- **Задачи:** выбрать подходящий пакет.
- **Сочетается с:** `ecc/laravel-patterns`

### `ecc/mailtrap-email-integration`

Интеграция отправки транзакционных писем через Mailtrap Email API.

- **Ключевые навыки:** песочница; верификация домена; аутентификация API.
- **Задачи:** подключить отправку писем в приложении.
- **Сочетается с:** `ecc/api-connector-builder`

### `ecc/nestjs-patterns`

Архитектура NestJS.

- **Ключевые навыки:** модули; контроллеры; провайдеры; валидация DTO; guards; interceptors; конфигурация.
- **Задачи:** построить бэкенд на NestJS.
- **Сочетается с:** `ecc/typescript-patterns`, `ecc/api-design`

### `ecc/perl-patterns`

Современный Perl 5.36+.

- **Ключевые навыки:** идиомы; лучшие практики; соглашения.
- **Задачи:** писать и ревьюить современный Perl-код.
- **Сочетается с:** `ecc/perl-testing`, `ecc/perl-security`

### `ecc/python-patterns`

Питоничный код — PEP 8, аннотации типов, лучшие практики.

- **Ключевые навыки:** идиомы Python; типизация; структура приложения.
- **Задачи:** писать и ревьюить Python-код.
- **Сочетается с:** `ecc/python-testing`, `ecc/fastapi-patterns`, `ecc/django-patterns`

### `ecc/quarkus-patterns`

Архитектура Quarkus 3.x LTS.

- **Ключевые навыки:** Camel для сообщений; REST API; CDI; Panache; асинхронная обработка.
- **Задачи:** построить Java-сервис на Quarkus.
- **Сочетается с:** `ecc/quarkus-tdd`, `ecc/quarkus-security`, `ecc/quarkus-verification`

### `ecc/rails-patterns`

Ruby on Rails 7.1+ и 8.x.

- **Ключевые навыки:** тонкие контроллеры и сервисные объекты; form и query objects; фоновые задачи; Hotwire.
- **Задачи:** строить и ревьюить Rails-приложение.
- **Сочетается с:** `ecc/api-design`, `ecc/postgres-patterns`

### `ecc/rust-patterns`

Идиоматичный Rust.

- **Ключевые навыки:** владение; обработка ошибок; трейты; конкурентность.
- **Задачи:** писать безопасный и быстрый Rust-код.
- **Сочетается с:** `ecc/rust-testing`, `ecc/latency-critical-systems`

### `claude-skills/senior-backend`

Разработка и исправление бэкенда — REST и GraphQL, авторизация, микросервисы, PostgreSQL, миграции, нагрузочные тесты.

- **Ключевые навыки:** сквозная серверная разработка.
- **Задачи:** построить или починить серверную часть.
- **Сочетается с:** `ecc/backend-patterns`, `ecc/postgres-patterns`

### `claude-skills/senior-fullstack`

Старт fullstack-проекта или аудит кодовой базы.

- **Ключевые навыки:** выбор стека (Next.js, FastAPI, MERN, Django); каркас; оценка качества кода.
- **Задачи:** начать проект с правильного стека.
- **Сочетается с:** `claude-skills/tech-stack-evaluator`, `claude-skills/saas-scaffolder`

### `claude-skills/spec-to-repo`

Создание нового репозитория-приложения по спецификации или идее.

- **Ключевые навыки:** каркас проекта; стартовый код.
- **Задачи:** «сделай мне приложение».
- **Сочетается с:** `claude-skills/saas-scaffolder`, `ecc/orch-build-mvp`

### `ecc/springboot-patterns`

Архитектура Spring Boot.

- **Ключевые навыки:** REST API; слоистые сервисы; доступ к данным; кэш; асинхронность; логирование.
- **Задачи:** строить Java-бэкенд на Spring Boot.
- **Сочетается с:** `ecc/springboot-tdd`, `ecc/springboot-security`, `ecc/jpa-patterns`

### `ecc/tinystruct-patterns`

Разработка на Java-фреймворке tinystruct.

- **Ключевые навыки:** устройство фреймворка; паттерны приложений.
- **Задачи:** работать с проектами на tinystruct.
- **Сочетается с:** `ecc/java-coding-standards`

### `ecc/typescript-patterns`

Строгий типобезопасный TypeScript.

- **Ключевые навыки:** строгая конфигурация компилятора; дизайн типов; сужение типов; дженерики.
- **Задачи:** писать надёжный код на TypeScript.
- **Сочетается с:** `ecc/react-patterns`, `ecc/nestjs-patterns`, `ecc/error-handling`

---

<a id="cat-dev-frontend"></a>
## Frontend, UI и дизайн интерфейсов

**Область применения.** Веб-интерфейсы на React, Next.js, Vue/Nuxt, Angular, Svelte, Vite; дизайн-системы, анимации, доступность, вёрстка презентаций и лендингов.

**Решаемые задачи.** Компоненты и состояние; производительность рендеринга; дизайн-токены; анимации; доступность (WCAG); превращение макетов в код; визуальная доработка интерфейсов.

**Типовые связки.** frontend-design-direction (визуальное направление) → *-patterns фреймворка → design-system / motion-* → accessibility / frontend-a11y → browser-qa / e2e-testing.

Навыков в категории: 25.

### `claude-skills/a11y-audit`

Аудит и исправление доступности (WCAG 2.2 A/AA) в React, Next.js, Vue, Angular, Svelte и HTML со скриптами проверки.

- **Ключевые навыки:** сканер доступности; проверка контраста; отчёт о соответствии; проверка в CI.
- **Задачи:** найти и исправить нарушения доступности, затем перепроверить.
- **Сочетается с:** `ecc/accessibility`, `claude-skills/code-reviewer`

### `ecc/accessibility`

Проектирование, реализация и аудит доступных интерфейсов по WCAG 2.2 AA для веба, iOS и Android.

- **Ключевые навыки:** семантика и ARIA-роли; трейты и подсказки доступности в мобильных ОС; управление фокусом и клавиатурой; контраст и размер зон касания; поддержка экранных дикторов.
- **Задачи:** аудит интерфейса на доступность; исправление нарушений WCAG; подготовка к требованиям законодательства о доступности.
- **Сочетается с:** `ecc/frontend-a11y`, `ecc/browser-qa`, `ecc/design-system`

### `ecc/angular-developer`

Генерация кода и архитектурные советы по Angular — от сигналов и форм до SSR и тестирования.

- **Ключевые навыки:** сигналы, linkedSignal, resource; формы; DI; роутинг; SSR; анимации; стили и Tailwind; Angular CLI.
- **Задачи:** создать проект, компоненты и сервисы Angular; применить лучшие практики реактивности.
- **Сочетается с:** `ecc/typescript-patterns`, `ecc/e2e-testing`, `ecc/accessibility`

### `claude-skills/design-qa`

Финальная проверка дизайна экрана или компонента перед сдачей.

- **Ключевые навыки:** поиск «шаблонности» и недоделок в сгенерированном UI; чек-лист качества.
- **Задачи:** не выпустить сырой интерфейс.
- **Сочетается с:** `ecc/make-interfaces-feel-better`, `claude-skills/ui-design-system`

### `ecc/design-system`

Создание дизайн-системы из существующего кода или аудит визуальной согласованности.

- **Ключевые навыки:** извлечение токенов (цвета, типографика, отступы, тени); CSS-переменные; документация дизайн-системы.
- **Задачи:** навести порядок в стилях; задокументировать визуальный язык.
- **Сочетается с:** `ecc/frontend-design-direction`, `ecc/accessibility`, `ecc/make-interfaces-feel-better`

### `claude-skills/epic-design`

Кинематографичный дизайн лендингов и hero-блоков — параллакс, scrollytelling, наложения.

- **Ключевые навыки:** эффекты прокрутки; визуальная драматургия.
- **Задачи:** сделать впечатляющую посадочную страницу.
- **Сочетается с:** `claude-skills/landing`, `ecc/motion-advanced`

### `ecc/frontend-a11y`

Доступность в React и Next.js.

- **Ключевые навыки:** семантичный HTML; ARIA; подписи форм; клавиатурная навигация; фокус; экранные дикторы.
- **Задачи:** сделать React-интерфейс доступным.
- **Сочетается с:** `ecc/accessibility`, `ecc/react-patterns`

### `ecc/frontend-design-direction`

Задание визуального направления для продакшен-интерфейсов.

- **Ключевые навыки:** визуальный язык; иерархия; выбор стиля для сайтов, дашбордов, лендингов.
- **Задачи:** сделать интерфейс выразительным, а не шаблонным.
- **Сочетается с:** `ecc/design-system`, `ecc/make-interfaces-feel-better`, `ecc/taste`

### `ecc/frontend-patterns`

Паттерны фронтенда на React и Next.js.

- **Ключевые навыки:** компоненты; управление состоянием; оптимизация производительности; UI-практики.
- **Задачи:** построить или отревьюить React/Next.js-интерфейс.
- **Сочетается с:** `ecc/react-patterns`, `ecc/typescript-patterns`, `ecc/e2e-testing`

### `claude-skills/landing-page-generator`

Лендинг или страница кампании как компонент Next.js на Tailwind.

- **Ключевые навыки:** каркас страницы; секции; тексты.
- **Задачи:** добавить посадочную страницу в Next.js-проект.
- **Сочетается с:** `claude-skills/page-cro`, `claude-skills/copywriting`

### `claude-skills/landing`

Премиальный одностраничный HTML-лендинг с 3D CSS, эффектами GSAP и параллаксом.

- **Ключевые навыки:** короткий бриф по позиционированию; эффекты прокрутки.
- **Задачи:** быстро сделать эффектную посадочную страницу.
- **Сочетается с:** `claude-skills/epic-design`, `claude-skills/copywriting`

### `ecc/make-interfaces-feel-better`

Конкретные детали дизайн-инжиниринга, делающие интерфейс отполированным.

- **Ключевые навыки:** отступы; типографика; границы и тени; движение; зоны клика.
- **Задачи:** улучшить «ощущение» от интерфейса.
- **Сочетается с:** `ecc/design-system`, `ecc/motion-patterns`, `ecc/frontend-design-direction`

### `ecc/motion-advanced`

Продвинутая анимация в React/Next.js.

- **Ключевые навыки:** drag and drop; жесты; анимация текста; рисование SVG; useAnimate; лоадеры.
- **Задачи:** сделать сложные интерактивные анимации.
- **Сочетается с:** `ecc/motion-foundations`, `ecc/motion-patterns`

### `ecc/motion-foundations`

Базовый слой анимации в React — токены движения, пружины, производительность, доступность, SSR.

- **Ключевые навыки:** пресеты; адаптация под устройство; уважение reduced motion.
- **Задачи:** заложить единые правила анимации в проекте.
- **Сочетается с:** `ecc/motion-patterns`, `ecc/motion-advanced`, `ecc/accessibility`

### `ecc/motion-patterns`

Готовые паттерны анимации — кнопки, модалки, тосты, переходы страниц, скролл.

- **Ключевые навыки:** stagger; анимация выхода; layout-анимации.
- **Задачи:** добавить типовые анимации в интерфейс.
- **Сочетается с:** `ecc/motion-foundations`, `ecc/make-interfaces-feel-better`

### `ecc/nextjs-turbopack`

Next.js 16+ и Turbopack.

- **Ключевые навыки:** инкрементальная сборка; кэширование; быстрый HMR; Turbopack против webpack.
- **Задачи:** ускорить разработку на Next.js.
- **Сочетается с:** `ecc/frontend-patterns`, `ecc/react-performance`

### `ecc/nuxt4-patterns`

Приложения на Nuxt 4.

- **Ключевые навыки:** безопасная гидратация; производительность; route rules; ленивая загрузка; useFetch и useAsyncData.
- **Задачи:** строить или ревьюить Nuxt-приложение.
- **Сочетается с:** `ecc/vue-patterns`

### `ecc/react-patterns`

React 18/19.

- **Ключевые навыки:** дисциплина хуков; серверные и клиентские компоненты; Suspense и error boundaries; form actions; управление состоянием.
- **Задачи:** писать современный React-код.
- **Сочетается с:** `ecc/react-performance`, `ecc/react-testing`, `ecc/frontend-patterns`

### `ecc/react-performance`

Оптимизация производительности React и Next.js по практикам Vercel.

- **Ключевые навыки:** лишние ре-рендеры; загрузка данных; размер бандла; серверные компоненты.
- **Задачи:** ускорить медленное React-приложение.
- **Сочетается с:** `ecc/react-patterns`, `ecc/benchmark`, `ecc/nextjs-turbopack`

### `claude-skills/saas-scaffolder`

Каркас нового SaaS — авторизация, БД, биллинг Stripe и дашборд на Next.js, TypeScript, Tailwind, shadcn/ui.

- **Ключевые навыки:** стартовый проект с типовыми функциями.
- **Задачи:** быстро начать новый SaaS.
- **Сочетается с:** `claude-skills/stripe-integration-expert`, `claude-skills/spec-to-repo`

### `claude-skills/senior-frontend`

Разработка и ревью фронтенда на React, Next.js, TypeScript, Tailwind.

- **Ключевые навыки:** компоненты; каркас; производительность; размер бандла.
- **Задачи:** построить качественный фронтенд.
- **Сочетается с:** `ecc/react-patterns`, `ecc/react-performance`

### `claude-skills/ui-design-system`

Построение дизайн-системы — токены, документация компонентов, адаптивные шкалы, передача разработчикам.

- **Ключевые навыки:** генерация токенов.
- **Задачи:** создать дизайн-систему.
- **Сочетается с:** `ecc/design-system`, `claude-skills/design-qa`

### `ecc/ui-to-vue`

Пакетное превращение скриншотов и макетов в компоненты Vue 3.

- **Ключевые навыки:** Vant, Element Plus, Ant Design Vue.
- **Задачи:** сверстать интерфейс по картинкам.
- **Сочетается с:** `ecc/vue-patterns`

### `ecc/vite-patterns`

Сборщик Vite.

- **Ключевые навыки:** конфигурация; плагины; HMR; переменные окружения; прокси; SSR; режим библиотеки.
- **Задачи:** настроить и оптимизировать сборку.
- **Сочетается с:** `ecc/react-patterns`, `ecc/vue-patterns`

### `ecc/vue-patterns`

Vue 3 Composition API.

- **Ключевые навыки:** архитектура компонентов; реактивность; Pinia; Vue Router; Nuxt SSR.
- **Задачи:** строить приложения на Vue.
- **Сочетается с:** `ecc/nuxt4-patterns`, `ecc/ui-to-vue`

---

<a id="cat-dev-mobile"></a>
## Мобильная и десктопная разработка

**Область применения.** iOS (Swift, SwiftUI), Android (Kotlin, Jetpack Compose), кроссплатформа (Flutter, React Native, Kotlin Multiplatform), десктоп под Windows.

**Решаемые задачи.** Архитектура приложения; UI и навигация; конкурентность и хранение данных; иконки и ассеты; тестирование на устройствах.

**Типовые связки.** *-patterns платформы → архитектурный навык (android-clean-architecture) → *-testing → accessibility; для ИИ на устройстве — foundation-models-on-device.

Навыков в категории: 13.

### `ecc/android-clean-architecture`

Clean Architecture для Android и Kotlin Multiplatform — модули, правила зависимостей, UseCase, репозитории, слой данных.

- **Ключевые навыки:** модульная структура; направление зависимостей; UseCase и Repository; организация слоя данных.
- **Задачи:** спроектировать или навести порядок в архитектуре Android/KMP-проекта.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/compose-multiplatform-patterns`, `ecc/kotlin-coroutines-flows`

### `claude-skills/apple-hig-expert`

Проектирование и ревью интерфейсов iOS, macOS, watchOS, visionOS по Apple HIG.

- **Ключевые навыки:** Liquid Glass; контраст; зоны касания; платформенные паттерны.
- **Задачи:** проверить интерфейс на соответствие гайдлайнам Apple.
- **Сочетается с:** `ecc/swiftui-patterns`, `ecc/liquid-glass-design`

### `ecc/compose-multiplatform-patterns`

Compose Multiplatform и Jetpack Compose для KMP-проектов.

- **Ключевые навыки:** управление состоянием; навигация; темы; производительность; платформенный UI.
- **Задачи:** построить UI на Compose для нескольких платформ.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/android-clean-architecture`, `ecc/kotlin-coroutines-flows`

### `ecc/dart-flutter-patterns`

Паттерны Dart и Flutter для продакшена.

- **Ключевые навыки:** null safety; Freezed; асинхронность; архитектура виджетов; BLoC, Riverpod, Provider; GoRouter; Dio; тестирование.
- **Задачи:** писать и ревьюить Flutter-приложения.
- **Сочетается с:** `ecc/flutter-dart-code-review`, `ecc/accessibility`

### `ecc/flutter-dart-code-review`

Чек-лист ревью кода Flutter и Dart независимо от библиотек.

- **Ключевые навыки:** виджеты; паттерны состояния (BLoC, Riverpod, Provider, GetX, MobX); идиомы Dart; производительность.
- **Задачи:** провести ревью Flutter-приложения.
- **Сочетается с:** `ecc/dart-flutter-patterns`

### `ecc/foundation-models-on-device`

Локальная LLM на устройствах Apple через фреймворк FoundationModels (iOS 26+).

- **Ключевые навыки:** генерация текста; управляемая генерация через @Generable; вызов инструментов; потоковая выдача.
- **Задачи:** добавить ИИ-функции в iOS-приложение без облака.
- **Сочетается с:** `ecc/swiftui-patterns`, `ecc/swift-concurrency-6-2`

### `ecc/ios-icon-gen`

Генерация иконок iOS-приложения из SF Symbols или Iconify.

- **Ключевые навыки:** наборы PNG для каталога ассетов Xcode.
- **Задачи:** быстро сделать иконки для iOS-приложения.
- **Сочетается с:** `ecc/swiftui-patterns`

### `ecc/kotlin-coroutines-flows`

Корутины и Flow в Kotlin для Android и KMP.

- **Ключевые навыки:** структурная конкурентность; операторы Flow; StateFlow; ошибки; тестирование.
- **Задачи:** писать асинхронный код на Kotlin.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/kotlin-testing`

### `ecc/liquid-glass-design`

Дизайн-система Liquid Glass в iOS 26.

- **Ключевые навыки:** стеклянный материал с размытием и отражениями; морфинг; SwiftUI, UIKit, WidgetKit.
- **Задачи:** сделать интерфейс в новом стиле iOS 26.
- **Сочетается с:** `ecc/swiftui-patterns`

### `ecc/react-native-patterns`

React Native и Expo.

- **Ключевые навыки:** Expo Router; разделение состояния; TanStack Query и Zod; производительные списки.
- **Задачи:** построить мобильное приложение на React Native.
- **Сочетается с:** `ecc/react-patterns`, `ecc/typescript-patterns`

### `ecc/swift-actor-persistence`

Потокобезопасное хранение данных в Swift на акторах.

- **Ключевые навыки:** кэш в памяти с файловым хранилищем; отсутствие гонок по построению.
- **Задачи:** надёжно сохранять данные в Swift-приложении.
- **Сочетается с:** `ecc/swift-concurrency-6-2`, `ecc/swiftui-patterns`

### `ecc/swift-concurrency-6-2`

Упрощённая конкурентность Swift 6.2.

- **Ключевые навыки:** однопоточность по умолчанию; @concurrent; изолированные соответствия протоколам.
- **Задачи:** перейти на модель конкурентности Swift 6.2.
- **Сочетается с:** `ecc/swift-actor-persistence`, `ecc/swiftui-patterns`

### `ecc/swiftui-patterns`

Архитектура SwiftUI.

- **Ключевые навыки:** Observable-макрос; композиция представлений; навигация; производительность.
- **Задачи:** строить современный интерфейс iOS и macOS.
- **Сочетается с:** `ecc/swift-concurrency-6-2`, `ecc/liquid-glass-design`, `ecc/accessibility`

---

<a id="cat-testing"></a>
## Тестирование и контроль качества кода

**Область применения.** Модульные, интеграционные и E2E-тесты, TDD, регрессия, качество и здоровье кода, проверки перед коммитом и релизом.

**Решаемые задачи.** Тесты до кода (TDD); E2E на Playwright; поиск флаки-тестов; регрессия после ИИ-правок; ревью кода и PR; оценка покрытия; quality gates.

**Типовые связки.** tdd-workflow → *-testing языка → e2e-testing / browser-qa → verification-loop → code-review / security-review перед мержем.

Навыков в категории: 52.

### `claude-skills/adversarial-reviewer`

Жёсткое критическое ревью диффа или PR через «враждебные» роли ревьюеров.

- **Ключевые навыки:** поиск общих слепых зон; критика с разных позиций.
- **Задачи:** получить честную жёсткую проверку перед мержем.
- **Сочетается с:** `claude-skills/code-reviewer`, `ecc/santa-method`

### `ecc/ai-regression-testing`

Регрессионное тестирование при ИИ-разработке — тесты API в песочнице без БД и ловушки для «слепых зон» модели.

- **Ключевые навыки:** sandbox-тесты API; автоматические проверки на баги; защита от ситуации, когда одна модель пишет и ревьюит код.
- **Задачи:** покрыть регрессиями код, написанный ИИ; проверить изменения, которые ревьюила та же модель.
- **Сочетается с:** `ecc/tdd-workflow`, `ecc/verification-loop`, `ecc/ai-first-engineering`

### `claude-skills/api-test-suite-builder`

Построение набора API-, интеграционных и контрактных тестов по маршрутам.

- **Ключевые навыки:** позитивные сценарии; авторизация; ошибки валидации; граничные случаи.
- **Задачи:** покрыть REST API тестами.
- **Сочетается с:** `claude-skills/api-design-reviewer`, `ecc/tdd-workflow`

### `ecc/browser-qa`

Автоматическая проверка UI после деплоя через браузер — ошибки консоли, Web Vitals, формы, визуальная регрессия, доступность.

- **Ключевые навыки:** smoke-проверки; тесты форм и авторизации; скриншоты на трёх брейкпоинтах; аудит axe-core; вердикт SHIP/DO-NOT-SHIP.
- **Задачи:** проверить фичу на стейдже; оценить фронтенд-PR перед релизом.
- **Сочетается с:** `ecc/e2e-testing`, `ecc/canary-watch`, `ecc/accessibility`

### `claude-skills/browserstack`

Запуск Playwright-тестов в BrowserStack на матрице браузеров.

- **Ключевые навыки:** кросс-браузерное тестирование; Safari и Firefox.
- **Задачи:** проверить сайт во всех нужных браузерах.
- **Сочетается с:** `ecc/e2e-testing`, `claude-skills/coverage`

### `ecc/click-path-audit`

Трассировка каждой кнопки интерфейса через всю цепочку изменений состояния.

- **Ключевые навыки:** поиск функций, которые по отдельности работают, но гасят друг друга; проверка итогового состояния UI.
- **Задачи:** найти баги, когда пользователи жалуются на кнопки, а отладка ничего не нашла; проверка после рефакторинга состояния.
- **Сочетается с:** `ecc/browser-qa`, `ecc/e2e-testing`, `ecc/react-testing`

### `claude-skills/code-reviewer`

Ревью кода — PR, дифф, коммит или фрагмент на TypeScript, Python, Go, Swift, Kotlin и других языках.

- **Ключевые навыки:** корректность; безопасность; производительность; читаемость.
- **Задачи:** провести ревью любого кода.
- **Сочетается с:** `claude-skills/adversarial-reviewer`, `ecc/security-review`

### `ecc/codehealth-mcp`

Оценка структурного здоровья кода в реальном времени через CodeScene MCP.

- **Ключевые навыки:** ревью до правок; дельта оценки после изменений; гейты для коммитов и PR.
- **Задачи:** проверить, не ухудшил ли ИИ файл; рефакторинг с контролем качества.
- **Сочетается с:** `ecc/plankton-code-quality`, `ecc/coding-standards`

### `claude-skills/coverage`

Поиск непокрытого тестами — страницы, сценарии, пробелы.

- **Ключевые навыки:** карта покрытия; приоритизация недостающих тестов.
- **Задачи:** понять, что ещё нужно протестировать.
- **Сочетается с:** `ecc/test-collaboration`, `claude-skills/api-test-suite-builder`

### `ecc/cpp-testing`

Тесты на C++ с GoogleTest и CTest.

- **Ключевые навыки:** написание и исправление тестов; флаки-тесты; покрытие; санитайзеры.
- **Задачи:** добавить или починить тесты C++-проекта.
- **Сочетается с:** `ecc/cpp-coding-standards`, `ecc/tdd-workflow`

### `ecc/csharp-testing`

Тестирование на C# и .NET — xUnit, FluentAssertions, моки, интеграционные тесты.

- **Ключевые навыки:** организация тестов; моки; интеграционное тестирование.
- **Задачи:** написать или отревьюить тесты .NET-проекта.
- **Сочетается с:** `ecc/dotnet-patterns`, `ecc/tdd-workflow`

### `ecc/delivery-gate`

Хук, не дающий Claude завершить работу, пока не пройдены проверки качества.

- **Ключевые навыки:** детекция «отговорок» в тексте; проверка журнала обучения; контроль свободного места.
- **Задачи:** принудительно требовать готовность результата перед завершением.
- **Сочетается с:** `ecc/verification-loop`, `ecc/gateguard`, `ecc/hookify-rules`

### `ecc/django-tdd`

Тестирование Django по TDD с pytest-django и factory_boy.

- **Ключевые навыки:** фабрики; моки; покрытие; тесты DRF API.
- **Задачи:** писать тесты Django или вести фичу через тесты.
- **Сочетается с:** `ecc/django-patterns`, `ecc/tdd-workflow`, `ecc/python-testing`

### `ecc/django-verification`

Полный цикл проверки Django перед релизом.

- **Ключевые навыки:** mypy, ruff, black; безопасность миграций; pytest с покрытием; pip-audit и bandit; ревью настроек.
- **Задачи:** финальная проверка Django-проекта перед PR или релизом.
- **Сочетается с:** `ecc/django-tdd`, `ecc/django-security`, `ecc/verification-loop`

### `ecc/e2e-testing`

E2E-тесты на Playwright.

- **Ключевые навыки:** Page Object Model; конфигурация; интеграция в CI; артефакты; борьба с флаки-тестами.
- **Задачи:** написать E2E-тесты или починить нестабильные.
- **Сочетается с:** `ecc/browser-qa`, `ecc/tdd-workflow`, `ecc/react-testing`

### `claude-skills/fix`

Диагностика и исправление падающего или нестабильного Playwright-теста.

- **Ключевые навыки:** поиск причины флаки; стабилизация.
- **Задачи:** починить сломанный E2E-тест.
- **Сочетается с:** `claude-skills/pw`, `ecc/e2e-testing`

### `ecc/fsharp-testing`

Тестирование на F#.

- **Ключевые навыки:** xUnit, FsUnit, Unquote; property-based тесты на FsCheck; интеграционные тесты.
- **Задачи:** писать тесты F#-проекта.
- **Сочетается с:** `ecc/dotnet-patterns`, `ecc/csharp-testing`

### `claude-skills/full-page-screenshot`

Полностраничные скриншоты веб-страниц.

- **Ключевые навыки:** прокрутка в SPA; ленивые изображения; очень длинные страницы.
- **Задачи:** сделать скриншот всей страницы.
- **Сочетается с:** `ecc/browser-qa`

### `ecc/gateguard`

Хук, который блокирует первую попытку правки или команды, пока агент не приведёт конкретные факты о коде.

- **Ключевые навыки:** принуждение к исследованию перед правкой; проверка импортов и потоков данных.
- **Задачи:** снизить число «слепых» правок агента.
- **Сочетается с:** `ecc/delivery-gate`, `ecc/search-first`, `ecc/hookify-rules`

### `claude-skills/generate`

Написание Playwright-тестов для страницы, компонента или фичи.

- **Ключевые навыки:** генерация E2E-тестов по описанию.
- **Задачи:** быстро добавить E2E-тесты.
- **Сочетается с:** `claude-skills/pw`, `ecc/e2e-testing`

### `ecc/golang-testing`

Тестирование на Go по TDD.

- **Ключевые навыки:** табличные тесты; подтесты; бенчмарки; фаззинг; покрытие.
- **Задачи:** писать тесты Go-проекта.
- **Сочетается с:** `ecc/golang-patterns`, `ecc/tdd-workflow`

### `claude-skills/karpathy-coder`

Проверка диффа на переусложнение по четырём принципам Карпати.

- **Ключевые навыки:** скрытые допущения; лишние абстракции; нехирургические правки; непроверенные цели.
- **Задачи:** упростить слишком «умный» код.
- **Сочетается с:** `claude-skills/minimalist`, `claude-skills/code-reviewer`

### `ecc/kotlin-testing`

Тестирование на Kotlin по TDD.

- **Ключевые навыки:** Kotest; MockK; тесты корутин; property-based; покрытие Kover.
- **Задачи:** писать тесты Kotlin-проекта.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/tdd-workflow`

### `ecc/laravel-tdd`

Тестирование Laravel.

- **Ключевые навыки:** PHPUnit и Pest; фабрики моделей; HTTP-тесты; Sanctum; моки; покрытие.
- **Задачи:** писать тесты Laravel-проекта.
- **Сочетается с:** `ecc/laravel-patterns`, `ecc/tdd-workflow`

### `ecc/laravel-verification`

Цикл проверки Laravel-проекта перед релизом.

- **Ключевые навыки:** окружение; линтеры; статический анализ; тесты с покрытием; скан безопасности.
- **Задачи:** финальная проверка перед PR или деплоем.
- **Сочетается с:** `ecc/laravel-tdd`, `ecc/laravel-security`

### `claude-skills/migrate`

Перенос тестов с Cypress или Selenium на Playwright.

- **Ключевые навыки:** конвертация тестов.
- **Задачи:** перейти на Playwright.
- **Сочетается с:** `claude-skills/pw`

### `ecc/module-regression`

Контроль межмодульных регрессий через реестр REGRESSION.md.

- **Ключевые навыки:** потребители каждого модуля; команды приёмки; прогон после изменений.
- **Задачи:** не сломать соседние модули в большом репозитории.
- **Сочетается с:** `ecc/module-governance`, `ecc/change-impact`

### `claude-skills/named-persona-adversarial-review`

Ревью PR глазами известных инженеров на основе их задокументированных взглядов.

- **Ключевые навыки:** архитектурная и UX-критика.
- **Задачи:** получить нестандартное ревью важного PR.
- **Сочетается с:** `claude-skills/adversarial-reviewer`

### `ecc/perl-testing`

Тестирование на Perl.

- **Ключевые навыки:** Test2::V0, Test::More, prove; моки; покрытие Devel::Cover; TDD.
- **Задачи:** писать тесты Perl-проекта.
- **Сочетается с:** `ecc/perl-patterns`, `ecc/tdd-workflow`

### `ecc/plankton-code-quality`

Контроль качества кода в момент записи через Plankton — автоформатирование, линтинг и исправления на каждую правку.

- **Ключевые навыки:** хуки на правку файла; автоисправления Claude.
- **Задачи:** настроить автоматическую проверку качества при каждом изменении.
- **Сочетается с:** `ecc/codehealth-mcp`, `ecc/hookify-rules`

### `claude-skills/pr-review-expert`

Пофайловое ревью PR на баги, безопасность и качество с вердиктом о мерже.

- **Ключевые навыки:** построчный анализ; вердикт.
- **Задачи:** отревьюить pull request.
- **Сочетается с:** `claude-skills/code-reviewer`, `claude-skills/adversarial-reviewer`

### `claude-skills/pw-init`

Настройка Playwright в проекте.

- **Ключевые навыки:** конфигурация; первые тесты.
- **Задачи:** добавить E2E-тестирование.
- **Сочетается с:** `claude-skills/pw`, `claude-skills/generate`

### `claude-skills/pw-review`

Ревью качества Playwright-тестов.

- **Ключевые навыки:** лучшие практики; анти-паттерны.
- **Задачи:** улучшить существующие тесты.
- **Сочетается с:** `claude-skills/pw`

### `claude-skills/pw`

Всё про Playwright — тесты, флаки, миграция, CI, TestRail.

- **Ключевые навыки:** маршрутизация по задачам Playwright.
- **Задачи:** любая работа с E2E-тестами.
- **Сочетается с:** `claude-skills/pw-init`, `claude-skills/generate`, `claude-skills/fix`

### `ecc/python-testing`

Тестирование на Python с pytest по TDD.

- **Ключевые навыки:** фикстуры; моки; параметризация; требования к покрытию.
- **Задачи:** писать тесты Python-проекта.
- **Сочетается с:** `ecc/python-patterns`, `ecc/tdd-workflow`

### `ecc/quarkus-tdd`

TDD для Quarkus.

- **Ключевые навыки:** JUnit 5; Mockito; REST Assured; тесты Camel; покрытие JaCoCo.
- **Задачи:** писать тесты при разработке фич и исправлении багов.
- **Сочетается с:** `ecc/quarkus-patterns`, `ecc/tdd-workflow`

### `ecc/quarkus-verification`

Цикл проверки Quarkus-проекта.

- **Ключевые навыки:** сборка; Checkstyle, PMD, SpotBugs; тесты с покрытием; OWASP-проверка зависимостей и контейнеров.
- **Задачи:** финальная проверка перед релизом.
- **Сочетается с:** `ecc/quarkus-tdd`, `ecc/quarkus-security`

### `ecc/react-testing`

Тестирование React-компонентов.

- **Ключевые навыки:** React Testing Library; Vitest и Jest; MSW для сети; проверки доступности axe.
- **Задачи:** покрыть тестами интерфейс на React.
- **Сочетается с:** `ecc/react-patterns`, `ecc/e2e-testing`

### `claude-skills/red-green-proof`

Доказательство бага — проверка причины, тест, падающий на текущем коде, затем исправление.

- **Ключевые навыки:** проверка гипотезы о причине; red-green.
- **Задачи:** исправлять баги только с доказательством.
- **Сочетается с:** `ecc/orch-fix-defect`, `ecc/tdd-workflow`

### `claude-skills/report`

Сводка результатов Playwright-тестов.

- **Ключевые навыки:** отчёт о прогоне.
- **Задачи:** узнать, как прошли тесты.
- **Сочетается с:** `claude-skills/pw`

### `ecc/rust-testing`

Тестирование на Rust по TDD.

- **Ключевые навыки:** модульные и интеграционные тесты; асинхронные тесты; property-based; моки; покрытие.
- **Задачи:** писать тесты Rust-проекта.
- **Сочетается с:** `ecc/rust-patterns`, `ecc/tdd-workflow`

### `ecc/santa-method`

Состязательная проверка двумя независимыми ревьюерами с одной рубрикой.

- **Ключевые навыки:** оба должны одобрить; цикл исправления и повторного ревью.
- **Задачи:** выпускать только то, что прошло двойную независимую проверку.
- **Сочетается с:** `ecc/agent-self-evaluation`, `ecc/verification-loop`

### `claude-skills/senior-qa`

Тесты для React и Next.js — Jest, React Testing Library, MSW, Playwright, покрытие.

- **Ключевые навыки:** стратегия тестирования фронтенда.
- **Задачи:** покрыть тестами фронтенд.
- **Сочетается с:** `ecc/react-testing`, `claude-skills/pw`

### `ecc/springboot-tdd`

TDD для Spring Boot.

- **Ключевые навыки:** JUnit 5; Mockito; MockMvc; Testcontainers; JaCoCo.
- **Задачи:** вести разработку Spring-сервиса через тесты.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/tdd-workflow`

### `ecc/springboot-verification`

Полный цикл проверки Spring Boot-проекта.

- **Ключевые навыки:** сборка Maven или Gradle; SpotBugs, PMD, Checkstyle; тесты с Testcontainers; покрытие.
- **Задачи:** финальная проверка перед релизом.
- **Сочетается с:** `ecc/springboot-tdd`, `ecc/springboot-security`

### `ecc/swift-protocol-di-testing`

Внедрение зависимостей через протоколы для тестируемого Swift-кода.

- **Ключевые навыки:** моки файловой системы, сети и внешних API; Swift Testing.
- **Задачи:** сделать Swift-код тестируемым.
- **Сочетается с:** `ecc/swiftui-patterns`, `ecc/tdd-workflow`

### `claude-skills/tdd-guide`

TDD и генерация тестов для Jest, Pytest, JUnit, Vitest, Mocha.

- **Ключевые навыки:** red-green-refactor; фикстуры; моки; пробелы покрытия.
- **Задачи:** писать тесты прежде кода.
- **Сочетается с:** `ecc/tdd-workflow`, `claude-skills/coverage`

### `ecc/tdd-workflow`

Разработка через тесты — падающий тест, минимальная реализация, рефакторинг с покрытием 80%+.

- **Ключевые навыки:** модульные, интеграционные и E2E-тесты; цикл red-green-refactor.
- **Задачи:** вести любую фичу или исправление через тесты.
- **Сочетается с:** `ecc/verification-loop`, `ecc/e2e-testing`, `ecc/python-testing`

### `ecc/test-collaboration`

Инвентаризация и управление тестовыми активами проекта.

- **Ключевые навыки:** связь требований, правил, рисков и багов с TEST-ID; исполняемые проверки.
- **Задачи:** понять, что покрыто тестами и чего не хватает.
- **Сочетается с:** `ecc/tdd-workflow`, `ecc/module-regression`

### `claude-skills/testrail`

Синхронизация Playwright-тестов с TestRail.

- **Ключевые навыки:** импорт и экспорт кейсов; публикация результатов.
- **Задачи:** связать автотесты с тест-менеджментом.
- **Сочетается с:** `claude-skills/pw`

### `ecc/verification-loop`

Шестиэтапная проверка работы сессии — сборка, типы, линт, тесты с покрытием, поиск секретов, ревью диффа.

- **Ключевые навыки:** отчёт о готовности; поиск проблем перед сдачей.
- **Задачи:** проверить результат перед PR.
- **Сочетается с:** `ecc/tdd-workflow`, `ecc/delivery-gate`, `ecc/security-review`

### `ecc/windows-desktop-e2e`

E2E-тесты нативных Windows-приложений (WPF, WinForms, Win32, Qt).

- **Ключевые навыки:** pywinauto; Windows UI Automation.
- **Задачи:** автоматизировать тестирование десктопного приложения.
- **Сочетается с:** `ecc/dotnet-patterns`, `ecc/generating-python-installer`

---

<a id="cat-security"></a>
## Безопасность

**Область применения.** Безопасность приложений, агентов, облака и смарт-контрактов; аудит, пентест-подготовка, секреты, зависимости, MCP-серверы.

**Решаемые задачи.** Поиск уязвимостей (OWASP); ревью аутентификации и авторизации; защита ИИ-агентов от prompt injection; аудит цепочки поставок; подготовка к баг-баунти; харднинг конфигураций.

**Типовые связки.** security-scan (быстрый скан) → security-review (глубокий разбор) → *-security фреймворка → исправление → повторная проверка; для агентов — agent-security-hardening + safety-guard.

Навыков в категории: 26.

### `ecc/agent-security-hardening`

Защита агентных систем, которые обрабатывают недоверенный контент, вызывают инструменты, пишут файлы и работают с секретами.

- **Ключевые навыки:** защита от prompt injection; изоляция инструментов; обращение с учётными данными; мультиарендная изоляция; безопасная память агента.
- **Задачи:** ревью безопасности агентного рантайма, шлюза инструментов или сервиса памяти.
- **Сочетается с:** `ecc/safety-guard`, `ecc/mcp-dependency-review`, `ecc/security-review`

### `claude-skills/ai-security`

Оценка безопасности ИИ/ML-систем и LLM-агентов.

- **Ключевые навыки:** prompt injection; джейлбрейки; инверсия модели; отравление данных; злоупотребление инструментами; MITRE ATLAS.
- **Задачи:** провести аудит безопасности ИИ-системы.
- **Сочетается с:** `ecc/agent-security-hardening`, `claude-skills/red-team`

### `claude-skills/ciso-advisor`

Советник по руководству безопасностью.

- **Ключевые навыки:** программа безопасности; обоснование бюджета в деньгах; дорожная карта SOC 2, ISO 27001, HIPAA; отчёты совету.
- **Задачи:** выстроить безопасность компании на уровне руководства.
- **Сочетается с:** `claude-skills/ciso-review`, `claude-skills/compliance-os`

### `claude-skills/ciso-review`

Критика плана, затрагивающего данные клиентов, комплаенс или доступ к продакшену.

- **Ключевые навыки:** позиция директора по безопасности.
- **Задачи:** проверить план на риски безопасности.
- **Сочетается с:** `claude-skills/ciso-advisor`

### `claude-skills/cloud-security`

Поиск ошибок конфигурации безопасности в AWS, Azure и GCP.

- **Ключевые навыки:** эскалация привилегий IAM; публичные бакеты; открытые группы безопасности; пробелы в IaC.
- **Задачи:** проверить облако на уязвимые настройки.
- **Сочетается с:** `claude-skills/aws-solution-architect`, `claude-skills/ciso-advisor`

### `claude-skills/dependency-auditor`

Аудит зависимостей проекта на уязвимости CVE и лицензии с планом безопасного обновления.

- **Ключевые навыки:** сканирование пакетов; проверка лицензий; план апгрейда.
- **Задачи:** убедиться, что зависимости безопасны перед релизом.
- **Сочетается с:** `claude-skills/senior-secops`, `ecc/security-scan`

### `ecc/django-security`

Безопасность Django — аутентификация, авторизация, CSRF, SQL-инъекции, XSS, безопасный деплой.

- **Ключевые навыки:** настройки безопасности; права доступа; защита от инъекций.
- **Задачи:** ревью безопасности Django-проекта.
- **Сочетается с:** `ecc/django-patterns`, `ecc/security-review`, `ecc/django-verification`

### `claude-skills/env-secrets-manager`

Аудит .env, ротация учётных данных, поиск пропавших переменных, защита от утечек секретов.

- **Ключевые навыки:** проверка секретов; план ротации.
- **Задачи:** навести порядок с секретами проекта.
- **Сочетается с:** `claude-skills/secrets-vault-manager`, `ecc/security-review`

### `claude-skills/incident-response`

Реагирование на подозрение во взломе по NIST SP 800-61.

- **Ключевые навыки:** триаж; уровни SEV1–SEV4; эскалация; сбор цифровых улик.
- **Задачи:** действовать при подозрении на утечку или атаку.
- **Сочетается с:** `claude-skills/threat-detection`, `claude-skills/senior-secops`

### `ecc/laravel-security`

Безопасность Laravel.

- **Ключевые навыки:** аутентификация и авторизация; безопасный Eloquent; CSRF; XSS; API; безопасный деплой.
- **Задачи:** ревью безопасности Laravel-приложения.
- **Сочетается с:** `ecc/laravel-patterns`, `ecc/security-review`

### `ecc/mcp-dependency-review`

Статическая проверка конфигурации MCP на изменяемые ссылки на пакеты без запуска серверов.

- **Ключевые навыки:** анализ .mcp.json и конфигов Cursor; риски цепочки поставок.
- **Задачи:** проверить MCP-конфиг перед одобрением или в CI.
- **Сочетается с:** `ecc/agent-security-hardening`, `ecc/security-scan`

### `ecc/perl-security`

Безопасность Perl.

- **Ключевые навыки:** taint mode; валидация ввода; безопасный запуск процессов; параметризованные запросы DBI; XSS, SQLi, CSRF; perlcritic.
- **Задачи:** ревью безопасности Perl-приложения.
- **Сочетается с:** `ecc/perl-patterns`, `ecc/security-review`

### `ecc/quarkus-security`

Безопасность Quarkus.

- **Ключевые навыки:** JWT и OIDC; RBAC через @RolesAllowed; Bean Validation; защита эндпоинтов.
- **Задачи:** реализовать и проверить безопасность Quarkus-сервиса.
- **Сочетается с:** `ecc/quarkus-patterns`, `ecc/security-review`

### `claude-skills/red-team`

Авторизованные red team-операции и анализ путей атаки.

- **Ключевые навыки:** kill chain; MITRE ATT&CK; планирование.
- **Задачи:** проверить защиту глазами атакующего.
- **Сочетается с:** `claude-skills/security-pen-testing`, `claude-skills/threat-detection`

### `ecc/safety-guard`

Защита от разрушительных операций агента.

- **Ключевые навыки:** перехват опасных команд (rm -rf, push --force, DROP TABLE); заморозка путей; режимы защиты.
- **Задачи:** работать с агентом на важных системах без риска потерь.
- **Сочетается с:** `ecc/hookify-rules`, `ecc/agent-security-hardening`

### `claude-skills/secrets-vault-manager`

Хранилища секретов — HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager.

- **Ключевые навыки:** настройка; ротация; аудит доступа.
- **Задачи:** централизовать хранение секретов.
- **Сочетается с:** `claude-skills/env-secrets-manager`

### `ecc/security-bounty-hunter`

Поиск эксплуатируемых уязвимостей уровня баг-баунти в репозиториях.

- **Ключевые навыки:** удалённо достижимые уязвимости; отсев шума; подготовка отчёта.
- **Задачи:** найти реальные уязвимости для отчёта.
- **Сочетается с:** `ecc/security-review`, `ecc/security-scan`

### `claude-skills/security-guidance`

Хук безопасности, предупреждающий перед записью кода с инъекциями, XSS, SQLi, небезопасной десериализацией.

- **Ключевые навыки:** установка и настройка хука.
- **Задачи:** ловить уязвимости в момент написания.
- **Сочетается с:** `ecc/safety-guard`, `ecc/security-review`

### `claude-skills/security-pen-testing`

Авторизованный пентест приложения или API.

- **Ключевые навыки:** сканы уязвимостей; OWASP Top 10; аудит зависимостей; отчёт.
- **Задачи:** проверить приложение на взлом.
- **Сочетается с:** `claude-skills/red-team`, `ecc/security-bounty-hunter`

### `ecc/security-review`

Чек-лист безопасности при работе с аутентификацией, вводом пользователя, секретами, API и платежами.

- **Ключевые навыки:** OWASP; хранение секретов; валидация ввода; безопасность платежей.
- **Задачи:** проверить безопасность фичи перед релизом.
- **Сочетается с:** `ecc/security-scan`, `ecc/agent-security-hardening`, `ecc/production-audit`

### `ecc/security-scan`

Сканирование конфигурации Claude Code (.claude/) на уязвимости через AgentShield.

- **Ключевые навыки:** проверка CLAUDE.md, хуков, MCP; риски инъекций.
- **Задачи:** убедиться, что настройки агента безопасны.
- **Сочетается с:** `ecc/mcp-dependency-review`, `ecc/security-review`

### `claude-skills/senior-secops`

Поиск и исправление проблем безопасности приложений.

- **Ключевые навыки:** ревью; исправление CVE; харднинг; секреты и авторизация; SOC 2, PCI-DSS, HIPAA, GDPR.
- **Задачи:** закрыть уязвимости приложения.
- **Сочетается с:** `claude-skills/senior-security`, `claude-skills/dependency-auditor`

### `claude-skills/senior-security`

Оценка безопасности дизайна или кода — модель угроз STRIDE, оценка рисков DREAD, поиск утечек секретов.

- **Ключевые навыки:** моделирование угроз.
- **Задачи:** понять, что может пойти не так с безопасностью.
- **Сочетается с:** `claude-skills/senior-secops`, `ecc/security-review`

### `claude-skills/skill-security-auditor`

Проверка безопасности навыка или плагина из недоверенного источника перед установкой.

- **Ключевые навыки:** скан скриптов, SKILL.md и зависимостей.
- **Задачи:** убедиться, что навык безопасен.
- **Сочетается с:** `ecc/security-scan`, `ecc/mcp-dependency-review`

### `ecc/springboot-security`

Spring Security.

- **Ключевые навыки:** аутентификация и авторизация; валидация; CSRF; секреты; заголовки; rate limiting.
- **Задачи:** защитить Spring Boot-сервис.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/security-review`

### `claude-skills/threat-detection`

Поиск угроз, проверка индикаторов компрометации и аномалий в логах.

- **Ключевые навыки:** сигналы по MITRE ATT&CK; z-score аномалии.
- **Задачи:** найти следы атаки.
- **Сочетается с:** `claude-skills/incident-response`, `claude-skills/red-team`

---

<a id="cat-devops"></a>
## DevOps, инфраструктура, деплой и мониторинг

**Область применения.** CI/CD, Docker, Kubernetes, облака (AWS, GCP, Azure), Terraform, наблюдаемость, инциденты, производительность в проде.

**Решаемые задачи.** Настройка пайплайнов и деплоя; контейнеризация; дашборды и алерты; мониторинг после релиза; разбор инцидентов; оптимизация затрат на облако.

**Типовые связки.** docker-patterns → deployment-patterns / kubernetes-patterns → canary-watch после релиза → dashboard-builder для мониторинга → incident-разбор при сбоях.

Навыков в категории: 35.

### `claude-skills/aws-solution-architect`

Проектирование и расчёт стоимости архитектуры AWS.

- **Ключевые навыки:** serverless, Lambda, API Gateway, DynamoDB, ECS, Aurora; CloudFormation; миграция в AWS.
- **Задачи:** спроектировать решение в AWS и оценить затраты.
- **Сочетается с:** `claude-skills/cloud-security`, `claude-skills/azure-cloud-architect`

### `claude-skills/azure-cloud-architect`

Проектирование и расчёт стоимости архитектуры Azure.

- **Ключевые навыки:** AKS, App Service, Functions, Cosmos DB; Bicep и ARM; Azure DevOps; миграция.
- **Задачи:** спроектировать решение в Azure.
- **Сочетается с:** `claude-skills/aws-solution-architect`, `claude-skills/cloud-security`

### `ecc/benchmark-optimization-loop`

Превращение просьбы «сделай быстрее» в измеряемый цикл оптимизации с проверкой корректности.

- **Ключевые навыки:** замер базовой линии; варианты с одной гипотезой; контроль корректности; воспроизводимые команды.
- **Задачи:** ускорить код или систему и выбрать лучший вариант по цифрам.
- **Сочетается с:** `ecc/benchmark`, `ecc/latency-critical-systems`, `ecc/data-throughput-accelerator`

### `ecc/benchmark`

Базовые замеры производительности и поиск регрессий — Core Web Vitals, задержки API, скорость сборки и тестов.

- **Ключевые навыки:** LCP, INP, CLS и вес страницы; перцентили задержек API; сравнение до/после; хранение замеров в git.
- **Задачи:** проверить скорость страниц; разобрать жалобу «тормозит»; сравнить варианты стека.
- **Сочетается с:** `ecc/benchmark-optimization-loop`, `ecc/react-performance`, `ecc/canary-watch`

### `ecc/canary-watch`

Мониторинг и проверка развёрнутого URL после релиза.

- **Ключевые навыки:** проверки HTTP-эндпоинтов и SSE; статические ресурсы; ошибки консоли; регрессии производительности.
- **Задачи:** post-deploy smoke-проверка после релиза, мержа или обновления зависимостей.
- **Сочетается с:** `ecc/browser-qa`, `ecc/benchmark`, `ecc/deployment-patterns`

### `claude-skills/chaos-engineering`

Хаос-эксперименты, геймдеи и внесение сбоев.

- **Ключевые навыки:** устойчивое состояние; критерии прерывания; отчёт после эксперимента.
- **Задачи:** проверить устойчивость системы к сбоям.
- **Сочетается с:** `claude-skills/incident-commander`, `ecc/kubernetes-patterns`

### `claude-skills/ci-cd-pipeline-builder`

Генерация CI/CD-конвейера по стеку репозитория — линт, тесты, сборка, деплой.

- **Ключевые навыки:** определение стека; workflow для CI.
- **Задачи:** добавить CI в репозиторий, где его нет.
- **Сочетается с:** `ecc/deployment-patterns`, `ecc/github-ops`

### `ecc/dashboard-builder`

Дашборды мониторинга в Grafana, SigNoz и аналогах, отвечающие на реальные вопросы операторов.

- **Ключевые навыки:** выбор метрик; структура панелей; уход от «витринных» дашбордов.
- **Задачи:** превратить метрики в рабочий дашборд.
- **Сочетается с:** `ecc/canary-watch`, `ecc/clickhouse-io`, `ecc/kubernetes-patterns`

### `ecc/deployment-patterns`

Деплой веб-приложений — CI/CD, Docker, health checks, откат, готовность к продакшену.

- **Ключевые навыки:** пайплайны CI/CD; контейнеризация; стратегии отката; чек-листы.
- **Задачи:** настроить конвейер поставки и деплой.
- **Сочетается с:** `ecc/docker-patterns`, `ecc/kubernetes-patterns`, `ecc/canary-watch`

### `claude-skills/docker-development`

Написание, оптимизация и ревью Dockerfile и docker-compose.

- **Ключевые навыки:** слои и кэширование; размер образа; безопасность.
- **Задачи:** сделать контейнер меньше, быстрее и безопаснее.
- **Сочетается с:** `ecc/docker-patterns`, `claude-skills/senior-devops`

### `ecc/docker-patterns`

Docker и Docker Compose — локальная разработка, безопасность контейнеров, сети, тома, многосервисные стеки.

- **Ключевые навыки:** Dockerfile; compose; харднинг; сети и тома.
- **Задачи:** создать или отревьюить Docker-конфигурацию.
- **Сочетается с:** `ecc/deployment-patterns`, `ecc/kubernetes-patterns`, `ecc/security-scan`

### `claude-skills/feature-flags-architect`

Флаги функций и аварийные выключатели — внедрение, раскатка, удаление.

- **Ключевые навыки:** план раскатки; борьба с долгом флагов.
- **Задачи:** безопасно выкатывать фичи постепенно.
- **Сочетается с:** `ecc/deployment-patterns`, `claude-skills/experiment-designer`

### `ecc/flox-environments`

Воспроизводимые кроссплатформенные окружения разработки на Flox (на базе Nix).

- **Ключевые навыки:** декларативные окружения; тулчейны проекта; одинаковая среда на macOS и Linux.
- **Задачи:** настроить окружение проекта, которое одинаково работает у всех.
- **Сочетается с:** `ecc/docker-patterns`

### `claude-skills/gcp-cloud-architect`

Проектирование, развёртывание и снижение стоимости в Google Cloud.

- **Ключевые навыки:** Cloud Run, GKE, Functions, Cloud SQL, BigQuery; миграция в GCP.
- **Задачи:** построить решение в GCP.
- **Сочетается с:** `claude-skills/aws-solution-architect`, `claude-skills/cloud-security`

### `scientific/get-available-resources`

Оценка реально доступных вычислительных ресурсов до тяжёлого запуска.

- **Ключевые навыки:** CPU/RAM/disk; лимиты контейнера; ускорители
- **Задачи:** Составить консервативный план вычислений по фактическим ограничениям.
- **Сочетается с:** `scientific/optimize-for-gpu`

### `ecc/github-ops`

Операции с репозиториями GitHub через gh CLI.

- **Ключевые навыки:** разбор issues; управление PR; CI/CD; релизы; мониторинг безопасности.
- **Задачи:** автоматизировать рутину по GitHub-репозиторию.
- **Сочетается с:** `ecc/git-workflow`, `ecc/issue-review`, `ecc/deployment-patterns`

### `claude-skills/helm-chart-builder`

Создание, ревью и защита Helm-чартов.

- **Ключевые навыки:** values.yaml; шаблоны; сабчарты; RBAC; безопасность подов.
- **Задачи:** упаковать приложение для Kubernetes.
- **Сочетается с:** `ecc/kubernetes-patterns`, `claude-skills/kubernetes-operator`

### `claude-skills/incident-commander`

Управление инцидентом в продакшене и разбор после него.

- **Ключевые навыки:** классификация серьёзности; координация; post-incident review.
- **Задачи:** провести команду через сбой и сделать выводы.
- **Сочетается с:** `claude-skills/runbook-generator`, `claude-skills/observability-designer`

### `claude-skills/kubernetes-operator`

Создание Kubernetes-операторов и CRD.

- **Ключевые навыки:** controller-runtime, kubebuilder, operator-sdk, KOPF; валидация.
- **Задачи:** автоматизировать управление сервисом в кластере.
- **Сочетается с:** `ecc/kubernetes-patterns`, `claude-skills/helm-chart-builder`

### `ecc/kubernetes-patterns`

Kubernetes для продакшена.

- **Ключевые навыки:** ресурсы; RBAC; пробы; автомасштабирование; ConfigMap и Secret; отладка kubectl.
- **Задачи:** развернуть и отладить приложение в кластере.
- **Сочетается с:** `ecc/docker-patterns`, `ecc/deployment-patterns`, `ecc/dashboard-builder`

### `ecc/latency-critical-systems`

Оптимизация систем, чувствительных к задержкам — realtime-дашборды, рыночные данные, стриминг, очереди.

- **Ключевые навыки:** отслеживание p50/p95/p99; хвосты задержек; кэши и очереди.
- **Задачи:** снизить и подтвердить задержки в критичной системе.
- **Сочетается с:** `ecc/benchmark-optimization-loop`, `ecc/redis-patterns`

### `scientific/modal`

Запуск Python и GPU-вычислений в облаке Modal.

- **Ключевые навыки:** serverless jobs; model serving; batch и SDK
- **Задачи:** Подготовить облачный вычислительный процесс с явной конфигурацией.
- **Сочетается с:** `scientific/get-available-resources`

### `claude-skills/monorepo-navigator`

Монорепозитории — Turborepo, Nx, pnpm-workspace, Lerna.

- **Ключевые навыки:** сборка только затронутого; удалённый кэш; переезд в монорепозиторий.
- **Задачи:** настроить или ускорить монорепозиторий.
- **Сочетается с:** `ecc/vite-patterns`

### `claude-skills/ms365-tenant-manager`

Администрирование Microsoft 365 — Entra ID, Exchange Online, Teams, лицензии, условный доступ.

- **Ключевые навыки:** управление пользователями; отчёты комплаенса.
- **Задачи:** администрировать M365 в организации.
- **Сочетается с:** `claude-skills/google-workspace-cli`

### `claude-skills/observability-designer`

Метрики, логи и трейсы для сервиса, борьба с шумными алертами, дашборды.

- **Ключевые навыки:** SLI; настройка алертов.
- **Задачи:** сделать сервис наблюдаемым.
- **Сочетается с:** `claude-skills/slo-architect`, `ecc/dashboard-builder`

### `scientific/optimize-for-gpu`

Ускорение научного Python на NVIDIA GPU с проверкой результата и времени.

- **Ключевые навыки:** CUDA-профилирование; CuPy/cuDF; память и transfer
- **Задачи:** Подтвердить численную корректность и фактическое ускорение процесса.
- **Сочетается с:** `scientific/get-available-resources`

### `claude-skills/performance-profiler`

Профилирование медленного эндпоинта, утечки памяти, нагрузки на CPU или большого бандла в Node.js, Python, Go.

- **Ключевые навыки:** замеры до оптимизации; поиск горячих точек; бюджеты производительности.
- **Задачи:** найти и устранить причину тормозов.
- **Сочетается с:** `ecc/benchmark-optimization-loop`, `ecc/benchmark`

### `ecc/production-audit`

Аудит готовности к продакшену по локальным данным без отправки кода наружу.

- **Ключевые навыки:** «что сломается в проде»; проверка перед запуском и после мержа.
- **Задачи:** оценить, готово ли приложение к реальным пользователям.
- **Сочетается с:** `ecc/security-review`, `ecc/deployment-patterns`, `ecc/canary-watch`

### `claude-skills/runbook-generator`

Ранбуки для деплоя, инцидентов, обслуживания и отката.

- **Ключевые навыки:** инструкции по окружениям.
- **Задачи:** подготовить сервис к эксплуатации до запуска.
- **Сочетается с:** `claude-skills/incident-commander`, `claude-skills/knowledge-ops`

### `claude-skills/senior-devops`

CI/CD, инфраструктура как код, контейнеры и деплой в AWS, GCP, Azure.

- **Ключевые навыки:** пайплайны сборки и деплоя.
- **Задачи:** настроить поставку и инфраструктуру.
- **Сочетается с:** `claude-skills/ci-cd-pipeline-builder`, `claude-skills/terraform-patterns`

### `claude-skills/ship-gate`

Предполётная проверка перед деплоем.

- **Ключевые навыки:** сканирование кода на блокеры релиза.
- **Задачи:** ответить на вопрос «можно ли выпускать».
- **Сочетается с:** `ecc/production-audit`, `ecc/verification-loop`

### `claude-skills/slo-architect`

SLO, SLI, бюджеты ошибок и алерты по скорости сжигания бюджета.

- **Ключевые навыки:** проектирование SLO; многооконные алерты.
- **Задачи:** определить уровни надёжности сервиса.
- **Сочетается с:** `claude-skills/observability-designer`

### `ecc/terminal-ops`

Исполнение задач в репозитории с доказательствами — запуск команд, проверки, отладка CI, точечные исправления.

- **Ключевые навыки:** точные команды; фиксация результатов; узкие правки.
- **Задачи:** проверить репозиторий или разобрать падение CI.
- **Сочетается с:** `ecc/github-ops`, `ecc/verification-loop`

### `claude-skills/terraform-patterns`

Модули Terraform, бэкенды состояния, провайдеры, ревью безопасности IaC.

- **Ключевые навыки:** анализ модулей; лучшие практики.
- **Задачи:** писать надёжную инфраструктуру как код.
- **Сочетается с:** `claude-skills/senior-devops`, `claude-skills/cloud-security`

### `ecc/uncloud`

Управление кластером Uncloud.

- **Ключевые навыки:** деплой сервисов; ingress Caddy; прокси-маршруты; публикация портов; масштабирование.
- **Задачи:** развернуть сервисы на собственных серверах.
- **Сочетается с:** `ecc/docker-patterns`

---

<a id="cat-data"></a>
## Базы данных, данные и аналитика

**Область применения.** PostgreSQL, MySQL, ClickHouse, Redis, ORM (Prisma, JPA, MyBatis, Exposed), ETL и пайплайны данных, аналитика и BI.

**Решаемые задачи.** Проектирование схем; оптимизация запросов; безопасные миграции; загрузка и выгрузка больших объёмов; сбор данных; метрики и отчёты.

**Типовые связки.** *-patterns СУБД → database-migrations → data-throughput-accelerator для объёмов → dashboard-builder / аналитические навыки для отчётов.

Навыков в категории: 37.

### `claude-skills/browser-automation`

Автоматизация браузера — парсинг сайтов, заполнение форм, извлечение данных.

- **Ключевые навыки:** скрейпинг; заполнение веб-форм; структурированные данные со страниц.
- **Задачи:** собрать данные с сайта или автоматизировать действия в браузере.
- **Сочетается с:** `ecc/data-scraper-agent`, `ecc/browser-qa`

### `claude-skills/chief-data-officer-advisor`

Советник по стратегии данных.

- **Ключевые навыки:** обучение на данных клиентов; хранилище, lakehouse или mesh; ценность данных для M&A; найм.
- **Задачи:** принять решение по архитектуре и использованию данных.
- **Сочетается с:** `claude-skills/cdo-review`, `claude-skills/database-designer`

### `ecc/clickhouse-io`

ClickHouse для высоконагруженной аналитики — схемы, оптимизация запросов, инженерия данных.

- **Ключевые навыки:** движки таблиц; партиционирование; оптимизация медленных аналитических запросов.
- **Задачи:** спроектировать схему или ускорить аналитический запрос в ClickHouse.
- **Сочетается с:** `ecc/data-throughput-accelerator`, `ecc/dashboard-builder`

### `scientific/dask`

Обработка массивов и таблиц за пределами памяти или на кластере с Dask.

- **Ключевые навыки:** DataFrame/Array; Futures; чанки и scheduler
- **Задачи:** Распределить вычисления с учётом зависимостей и памяти.
- **Сочетается с:** `scientific/get-available-resources`, `scientific/zarr-python`

### `claude-skills/data-quality-auditor`

Профилирование данных перед анализом или обучением модели.

- **Ключевые навыки:** пропуски; выбросы; распределения; качество данных.
- **Задачи:** проверить датасет до использования.
- **Сочетается с:** `ecc/mle-workflow`, `claude-skills/database-designer`

### `ecc/data-scraper-agent`

Автоматический ИИ-агент сбора данных из публичных источников по расписанию на GitHub Actions.

- **Ключевые навыки:** парсинг вакансий, цен, новостей; обогащение бесплатной LLM; хранение в Notion, Sheets, Supabase; обучение на обратной связи.
- **Задачи:** следить за источником данных и автоматически собирать результаты.
- **Сочетается с:** `ecc/exa-search`, `ecc/deep-research`, `ecc/regex-vs-llm-structured-text`

### `ecc/data-throughput-accelerator`

Диагностика и ускорение перемещения больших объёмов данных — загрузка, бэкфилл, экспорт, ETL.

- **Ключевые навыки:** поиск настоящего узкого места; бенчмарк вариантов; синхронизация таблиц.
- **Задачи:** ускорить медленную загрузку или выгрузку данных.
- **Сочетается с:** `ecc/benchmark-optimization-loop`, `ecc/postgres-patterns`, `ecc/clickhouse-io`

### `claude-skills/database-designer`

Проектирование схемы БД — таблицы, связи, индексы, нормализация, SQL или NoSQL, план миграции.

- **Ключевые навыки:** моделирование данных; выбор типа БД.
- **Задачи:** спроектировать хранение данных приложения.
- **Сочетается с:** `claude-skills/database-schema-designer`, `ecc/postgres-patterns`, `ecc/database-migrations`

### `scientific/database-lookup`

Воспроизводимые запросы к документированным публичным базам данных.

- **Ключевые навыки:** endpoint и фильтры; пагинация; provenance
- **Задачи:** Получить факты из заданного источника вместо предположений.
- **Сочетается с:** `scientific/paper-lookup`

### `ecc/database-migrations`

Безопасные обратимые миграции БД без простоя.

- **Ключевые навыки:** expand-contract; конкурентные индексы; пакетные бэкфиллы; инструменты PostgreSQL, Prisma и др.
- **Задачи:** провести миграцию на продакшене без остановки сервиса.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/change-impact`, `ecc/prisma-patterns`

### `claude-skills/database-schema-designer`

ER-диаграмма, нормализация и план миграции схемы.

- **Ключевые навыки:** ERD; нормализованный DDL; шаги миграции.
- **Задачи:** получить схему БД с диаграммой.
- **Сочетается с:** `claude-skills/database-designer`, `ecc/database-migrations`

### `scientific/exploratory-data-analysis`

Ограниченный локальный разведочный анализ поддерживаемых научных форматов.

- **Ключевые навыки:** профили CSV/JSON; пропуски; утечки и выбросы
- **Задачи:** Подготовить проверяемый EDA-отчёт без неявной поддержки неизвестных форматов.
- **Сочетается с:** `scientific/statistical-analysis`

### `scientific/geomaster`

Геопространственные исследования и обработка данных наблюдения Земли.

- **Ключевые навыки:** растры и векторы; STAC; пространственная статистика
- **Задачи:** Согласовать координаты и сетки для воспроизводимого GIS-анализа.
- **Сочетается с:** `scientific/geopandas`

### `scientific/geopandas`

Анализ векторных геоданных непосредственно в GeoPandas.

- **Ключевые навыки:** GeoDataFrame; spatial join; CRS и ввод-вывод
- **Задачи:** Проверить геометрию и выполнить пространственные операции.
- **Сочетается с:** `scientific/geomaster`

### `ecc/jpa-patterns`

JPA и Hibernate в Spring Boot.

- **Ключевые навыки:** дизайн сущностей; связи; оптимизация запросов; транзакции; индексы; пагинация; пулы соединений.
- **Задачи:** спроектировать слой данных на JPA.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/postgres-patterns`

### `ecc/kotlin-exposed-patterns`

ORM Exposed от JetBrains.

- **Ключевые навыки:** DSL-запросы; DAO; транзакции; HikariCP; миграции Flyway.
- **Задачи:** работать с БД в Kotlin-сервисе.
- **Сочетается с:** `ecc/kotlin-ktor-patterns`, `ecc/postgres-patterns`

### `claude-skills/migration-architect`

План миграции схем, БД и сервисов без простоя.

- **Ключевые навыки:** поэтапный план; проверка совместимости; скрипты отката.
- **Задачи:** переехать без остановки сервиса.
- **Сочетается с:** `ecc/database-migrations`, `ecc/change-impact`

### `ecc/mybatis-patterns`

MyBatis и MyBatis-Spring.

- **Ключевые навыки:** дизайн мапперов; SQL в XML и аннотациях; динамический SQL; транзакции; пакетная обработка.
- **Задачи:** работать с БД через MyBatis.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/mysql-patterns`

### `ecc/mysql-patterns`

MySQL и MariaDB для продакшена.

- **Ключевые навыки:** схемы; запросы; индексы; транзакции; репликация; пулы соединений.
- **Задачи:** спроектировать схему или ускорить запросы MySQL.
- **Сочетается с:** `ecc/database-migrations`, `ecc/mybatis-patterns`

### `scientific/networkx`

Построение и анализ сетей и графов с NetworkX.

- **Ключевые навыки:** пути и центральность; сообщества; модели графов
- **Задачи:** Исследовать структуру социальной, биологической или иной сети.
- **Сочетается с:** `scientific/torch-geometric`

### `scientific/polars`

Быстрая табличная обработка и ETL на Polars.

- **Ключевые навыки:** выражения; lazy/streaming; Arrow
- **Задачи:** Преобразовать большие таблицы и перенести pandas-процессы.
- **Сочетается с:** `scientific/polars-bio`, `scientific/dask`

### `ecc/postgres-patterns`

PostgreSQL по лучшим практикам Supabase.

- **Ключевые навыки:** оптимизация запросов; проектирование схем; индексы; безопасность (RLS).
- **Задачи:** спроектировать схему или ускорить запросы PostgreSQL.
- **Сочетается с:** `ecc/database-migrations`, `ecc/prisma-patterns`, `ecc/redis-patterns`

### `ecc/prisma-patterns`

Prisma ORM для TypeScript-бэкендов.

- **Ключевые навыки:** дизайн схем; оптимизация запросов; транзакции; пагинация; известные ловушки Prisma.
- **Задачи:** работать с БД через Prisma без сюрпризов.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/database-migrations`, `ecc/typescript-patterns`

### `scientific/pymc`

Построение и проверка байесовских моделей в PyMC.

- **Ключевые навыки:** NUTS/MCMC; posterior predictive; PSIS-LOO
- **Задачи:** Оценить распределения параметров и неопределённость с диагностикой модели.
- **Сочетается с:** `scientific/statistical-analysis`

### `ecc/redis-patterns`

Redis в продакшене.

- **Ключевые навыки:** структуры данных; стратегии кэширования; распределённые блокировки; rate limiting; pub/sub.
- **Задачи:** добавить кэш, очереди или блокировки на Redis.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/django-celery`

### `scientific/scikit-survival`

Модели выживаемости с цензурированием и конкурирующими рисками.

- **Ключевые навыки:** patient-safe preprocessing; survival metrics; выбор модели
- **Задачи:** Проверить прогнозы времени до события с учётом цензурирования.
- **Сочетается с:** `scientific/statistical-analysis`, `scientific/pyhealth`

### `claude-skills/senior-data-engineer`

Конвейеры данных — Airflow, Spark, dbt, Kafka, ETL/ELT, проверки качества.

- **Ключевые навыки:** отладка падающих DAG; качество данных.
- **Задачи:** построить или починить пайплайн данных.
- **Сочетается с:** `ecc/data-throughput-accelerator`, `claude-skills/data-quality-auditor`

### `claude-skills/senior-data-scientist`

Дизайн экспериментов и анализ табличных данных.

- **Ключевые навыки:** A/B-тесты; причинный вывод; признаки; оценка моделей.
- **Задачи:** ответить на бизнес-вопрос данными.
- **Сочетается с:** `claude-skills/statistical-analyst`, `claude-skills/experiment-designer`

### `claude-skills/snowflake-development`

Разработка в Snowflake.

- **Ключевые навыки:** SQL; Dynamic Tables; Streams и Tasks; Cortex AI; Snowpark Python; dbt.
- **Задачи:** строить аналитику и данные в Snowflake.
- **Сочетается с:** `claude-skills/senior-data-engineer`

### `claude-skills/sql-database-assistant`

Написание, исправление и ускорение SQL.

- **Ключевые навыки:** планы EXPLAIN; индексы; миграции ORM (Prisma, Drizzle, SQLAlchemy).
- **Задачи:** ускорить медленный запрос.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/database-migrations`

### `scientific/statistical-analysis`

Выбор статистических методов и анализ исследовательских данных.

- **Ключевые навыки:** проверка предпосылок; размеры эффектов; APA-отчётность
- **Задачи:** Проанализировать группы, связи или регрессии с оценкой неопределённости.
- **Сочетается с:** `scientific/statistical-power`, `scientific/statsmodels`

### `claude-skills/statistical-analyst`

Реальна ли разница — тесты значимости, доверительные интервалы, размер выборки, длительность теста.

- **Ключевые навыки:** статистика для A/B.
- **Задачи:** проверить результат эксперимента.
- **Сочетается с:** `claude-skills/experiment-designer`, `claude-skills/senior-data-scientist`

### `scientific/statistical-power`

Расчёт размера выборки и мощности до сбора данных.

- **Ключевые навыки:** MDE; кривые мощности; Monte Carlo
- **Задачи:** Обосновать число участников или реплик под выбранный дизайн.
- **Сочетается с:** `scientific/experimental-design`, `scientific/statistical-analysis`

### `scientific/statsmodels`

Оценка и диагностика статистических моделей с statsmodels.

- **Ключевые навыки:** OLS/GLM; mixed models; ARIMA/SARIMAX
- **Задачи:** Проверить коэффициенты, остатки и интервалы прогноза.
- **Сочетается с:** `scientific/statistical-analysis`

### `claude-skills/universal-scraping-architect`

Скрейпер для сайтов, PDF и API с пагинацией с проверкой полей (Firecrawl или Python).

- **Ключевые навыки:** извлечение; валидация данных.
- **Задачи:** собрать структурированные данные из источника.
- **Сочетается с:** `claude-skills/browser-automation`, `ecc/data-scraper-agent`

### `scientific/vaex`

Обработка таблиц больше оперативной памяти с Vaex.

- **Ключевые навыки:** виртуальные выражения; потоковые статистики; binning
- **Задачи:** Получить ограниченные агрегаты без случайной материализации всего набора.
- **Сочетается с:** `scientific/dask`, `scientific/polars`

### `scientific/zarr-python`

Хранение многомерных научных массивов в Zarr-Python 3.

- **Ключевые навыки:** чанки и sharding; codecs; S3/GCS
- **Задачи:** Настроить формат и ограниченный ввод-вывод с сохранением метаданных.
- **Сочетается с:** `scientific/dask`, `scientific/anndata`

---

<a id="cat-ai-agents"></a>
## AI, LLM и агентные системы

**Область применения.** Проектирование ИИ-агентов, мультиагентных систем, автономных циклов, RAG, промптов; оценка и стоимость LLM; ML-пайплайны.

**Решаемые задачи.** Построение агента и набора инструментов; оркестрация нескольких агентов; оценка качества (eval); снижение стоимости токенов; память агента; отладка сбоев агента.

**Типовые связки.** agent-harness-construction (инструменты агента) → autonomous-agent-harness / continuous-agent-loop (цикл) → eval-harness / agent-eval (оценка) → cost-aware-llm-pipeline (стоимость) → agent-security-hardening (защита).

Навыков в категории: 98.

### `scientific/aeon`

Машинное обучение на временных рядах с aeon.

- **Ключевые навыки:** классификация; forecasting; сегментация и сходство
- **Задачи:** Выбрать временную модель вместо неспециализированного ML-подхода.
- **Сочетается с:** `scientific/scikit-learn`, `scientific/timesfm-forecasting`

### `ecc/agent-architecture-audit`

Полная диагностика ИИ-агентов и LLM-приложений по 12 слоям стека с ранжированием проблем по критичности.

- **Ключевые навыки:** поиск регрессий обёрток; загрязнение памяти агента; нарушения дисциплины инструментов; скрытые циклы самоисправления; искажения при выводе.
- **Задачи:** найти слой, в котором ломается агент; аудит агента перед выпуском; список исправлений в коде.
- **Сочетается с:** `ecc/agent-introspection-debugging`, `ecc/eval-harness`, `ecc/agent-security-hardening`

### `claude-skills/agent-designer`

Проектирование мультиагентных систем (супервизор, рой, конвейер) и схем инструментов.

- **Ключевые навыки:** выбор топологии; дизайн инструментов; поиск узких мест по логам запусков.
- **Задачи:** разделить работу между агентами; ускорить медленный запуск.
- **Сочетается с:** `claude-skills/agent-workflow-designer`, `ecc/agent-harness-construction`

### `ecc/agent-eval`

Сравнение кодовых агентов (Claude Code, Aider, Codex и др.) на ваших задачах по доле успеха, стоимости, времени и стабильности.

- **Ключевые навыки:** постановка сравнительных задач; метрики pass rate и стоимости; повторные прогоны для оценки стабильности.
- **Задачи:** выбрать агента для команды; измерить эффект изменения настроек агента цифрами, а не впечатлением.
- **Сочетается с:** `ecc/eval-harness`, `ecc/cost-tracking`, `ecc/benchmark`

### `ecc/agent-harness-construction`

Проектирование набора инструментов, пространства действий и формата наблюдений ИИ-агента для повышения доли успешных задач.

- **Ключевые навыки:** дизайн инструментов и их описаний; форматирование ответов инструментов; сокращение лишних действий.
- **Задачи:** создать или переработать набор инструментов агента; повысить надёжность выполнения задач.
- **Сочетается с:** `ecc/mcp-server-patterns`, `ecc/agent-eval`, `ecc/agentic-engineering`

### `claude-skills/agent-harness`

Доведение цели в одном из доменов репозитория до проверенного завершения через план задач.

- **Ключевые навыки:** компиляция цели в план; проверка завершения.
- **Задачи:** поручить агенту задачу с гарантированной проверкой результата.
- **Сочетается с:** `claude-skills/agent-designer`, `ecc/continuous-agent-loop`

### `ecc/agent-introspection-debugging`

Структурированная самодиагностика сбоев ИИ-агента — фиксация, диагноз, ограниченное восстановление и отчёт.

- **Ключевые навыки:** сбор контекста сбоя; гипотезы о причине; безопасный повторный запуск; отчёт с выводами.
- **Задачи:** разобрать неудачный запуск агента воспроизводимо, а не простым повтором.
- **Сочетается с:** `ecc/agent-architecture-audit`, `ecc/continuous-agent-loop`

### `claude-skills/agent-launcher-orchestrator`

Создание, запуск, оценка и расписание Claude Managed Agents в вашем аккаунте Anthropic.

- **Ключевые навыки:** сборка агента; ночные запуски; оценка качества.
- **Задачи:** запустить своего облачного агента по расписанию.
- **Сочетается с:** `claude-skills/agent-designer`, `claude-skills/agent-regression-evals`

### `claude-skills/agent-memory`

Управление памятью агента — продвижение исправлений в правила, чистка разросшегося CLAUDE.md.

- **Ключевые навыки:** отслеживание происхождения правил; удаление дублей; структура памяти.
- **Задачи:** перестать повторять агенту одни и те же исправления.
- **Сочетается с:** `ecc/continuous-learning-v2`, `ecc/ck`

### `pm-skills/agent-orchestration-advisor`

Проектирование мультиагентных ИИ-процессов для продуктовых задач.

- **Ключевые навыки:** границы агентов; передачи; мониторинг.
- **Задачи:** распределить сложную PM-задачу между агентами.
- **Сочетается с:** `ecc/team-agent-orchestration`, `claude-skills/agent-designer`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/agent-regression-evals`

Регрессионные оценки перед выпуском изменений агента, промпта, модели или инструмента.

- **Ключевые навыки:** повторные прогоны; сравнение кандидата с базой; вердикт о падении качества.
- **Задачи:** убедиться, что изменение не ухудшило агента.
- **Сочетается с:** `ecc/eval-harness`, `ecc/agent-eval`

### `claude-skills/agent-run-forensics`

Расследование прошлых запусков агента по фактам из логов.

- **Ключевые навыки:** что изменил агент; действительно ли прошли тесты; проверка итоговой сводки.
- **Задачи:** понять, почему агент сделал то, что сделал.
- **Сочетается с:** `ecc/agent-introspection-debugging`, `claude-skills/collab-proof`

### `ecc/agent-runtime-gateway-smoke-test`

Дымовая проверка связки локального API агента, временного туннеля-шлюза и обратного вызова из удалённой песочницы.

- **Ключевые навыки:** проверка без инструментов; восстановление исходного подключения приложения.
- **Задачи:** убедиться, что агентная инфраструктура связана правильно, перед реальной работой.
- **Сочетается с:** `ecc/enterprise-agent-ops`, `ecc/canary-watch`

### `ecc/agent-self-evaluation`

Самооценка агентом результата после задачи по пяти осям — точность, полнота, ясность, применимость, краткость.

- **Ключевые навыки:** оценочная карта 1–5 с доказательствами; конкретные предложения по улучшению.
- **Задачи:** проверить качество своего ответа перед сдачей; найти слабые места результата.
- **Сочетается с:** `ecc/verification-loop`, `ecc/santa-method`

### `claude-skills/agent-workflow-designer`

Архитектура многошаговых LLM- и агентных конвейеров.

- **Ключевые навыки:** выбор одного или нескольких агентов; борьба с разрастанием контекста; передачи между шагами.
- **Задачи:** спроектировать конвейер или починить сломанные передачи.
- **Сочетается с:** `claude-skills/agent-designer`, `ecc/blueprint`

### `claude-skills/agenthub`

Запуск нескольких агентов параллельно на одну задачу с выбором лучшего результата.

- **Ключевые навыки:** параллельные варианты кода, текстов и исследований; сравнение результатов.
- **Задачи:** получить лучший вариант из нескольких попыток.
- **Сочетается с:** `claude-skills/board`, `ecc/gan-style-harness`

### `ecc/agentic-engineering`

Работа в роли агентного инженера — сначала оценки (eval), декомпозиция и маршрутизация моделей по стоимости.

- **Ключевые навыки:** eval-first подход; разбиение работы на задачи для агентов; выбор модели под сложность задачи.
- **Задачи:** спланировать и выполнить инженерную работу силами агентов от начала до конца.
- **Сочетается с:** `ecc/blueprint`, `ecc/eval-harness`, `ecc/cost-aware-llm-pipeline`

### `ecc/agentic-os`

Построение постоянной мультиагентной «операционной системы» на Claude Code — ядро, агенты-специалисты, команды, файловая память, расписания.

- **Ключевые навыки:** архитектура ядра; память в файлах; slash-команды; автоматизация по расписанию; состояние без внешних БД.
- **Задачи:** создать личную систему агентов со своей памятью и регулярными задачами.
- **Сочетается с:** `ecc/autonomous-agent-harness`, `ecc/unified-memory`, `ecc/team-agent-orchestration`

### `claude-skills/ar-loop`

Запуск эксперимента autoresearch по расписанию — от 10 минут до раза в месяц.

- **Ключевые навыки:** регулярные итерации улучшения.
- **Задачи:** поставить автоматическую оптимизацию на поток.
- **Сочетается с:** `claude-skills/autoresearch-agent`, `claude-skills/ar-status`

### `claude-skills/ar-resume`

Продолжение приостановленного эксперимента autoresearch с его ветки и истории.

- **Ключевые навыки:** восстановление состояния эксперимента.
- **Задачи:** вернуться к оптимизации после паузы.
- **Сочетается с:** `claude-skills/autoresearch-agent`

### `claude-skills/ar-run`

Одна ручная итерация autoresearch — правка, оценка, сохранить или отбросить.

- **Ключевые навыки:** шаг эксперимента с метрикой.
- **Задачи:** сделать один шаг улучшения вручную.
- **Сочетается с:** `claude-skills/autoresearch-agent`

### `claude-skills/ar-status`

Результаты и прогресс экспериментов autoresearch.

- **Ключевые навыки:** сводка метрик; история итераций.
- **Задачи:** узнать, как идёт эксперимент.
- **Сочетается с:** `claude-skills/autoresearch-agent`

### `scientific/arbor`

Управление исследовательскими экспериментами по Arbor Hypothesis Tree Refinement.

- **Ключевые навыки:** деревья гипотез; изолированные прогоны; held-out сравнение
- **Задачи:** Вести проверяемый поиск улучшений модели или агентной системы.
- **Сочетается с:** `scientific/hypothesis-generation`

### `ecc/autonomous-agent-harness`

Превращение Claude Code в автономную агентную систему с постоянной памятью, расписаниями, computer use и очередью задач.

- **Ключевые навыки:** встроенные расписания и диспетчеризация; память; MCP-инструменты; очередь задач.
- **Задачи:** настроить агента, который работает непрерывно и сам ставит себе задачи.
- **Сочетается с:** `ecc/agentic-os`, `ecc/continuous-agent-loop`, `ecc/enterprise-agent-ops`

### `ecc/autonomous-loops`

Архитектуры автономных циклов Claude Code — от простых конвейеров до мультиагентных графов (оставлен для совместимости).

- **Ключевые навыки:** последовательные пайплайны; RFC-управляемые DAG-системы.
- **Задачи:** справка по старым схемам циклов; для новых задач используйте continuous-agent-loop.
- **Сочетается с:** `ecc/continuous-agent-loop`, `ecc/ralphinho-rfc-pipeline`

### `claude-skills/autoresearch-agent`

Измеримое улучшение файла методом проб — скорость кода, размер бандла, доля прохождения, оценка промпта.

- **Ключевые навыки:** метрика цели; итерации; сохранение только улучшений.
- **Задачи:** оптимизировать что-то по числовой метрике автоматически.
- **Сочетается с:** `claude-skills/ar-run`, `claude-skills/ar-loop`, `ecc/benchmark-optimization-loop`

### `ecc/bengali-nlp`

Обработка текста на бенгальском языке для ИИ-приложений.

- **Ключевые навыки:** нормализация Unicode; определение письменности; токенизация; лигатуры.
- **Задачи:** подготовить бенгальские тексты для NLP и LLM.
- **Сочетается с:** `ecc/regex-vs-llm-structured-text`

### `claude-skills/board`

Доска сообщений AgentHub для координации конкурирующих агентов.

- **Ключевые навыки:** публикация и чтение сообщений между агентами.
- **Задачи:** координировать параллельных агентов.
- **Сочетается с:** `claude-skills/agenthub`

### `claude-skills/chief-ai-officer-advisor`

Советник по ИИ-стратегии — API, дообучение или своя модель; классификация рисков; найм в ИИ.

- **Ключевые навыки:** EU AI Act и законы штатов США; окупаемость своего хостинга; порядок найма.
- **Задачи:** принять стратегическое решение по ИИ в компании.
- **Сочетается с:** `claude-skills/caio-review`, `claude-skills/ai-act-readiness`

### `ecc/claude-devfleet`

Оркестрация параллельных кодовых агентов через Claude DevFleet в изолированных worktree.

- **Ключевые навыки:** планирование проекта; запуск агентов; мониторинг прогресса; структурированные отчёты.
- **Задачи:** распараллелить разработку между несколькими агентами.
- **Сочетается с:** `ecc/dmux-workflows`, `ecc/team-agent-orchestration`, `ecc/blueprint`

### `pm-skills/context-engineering-advisor`

Диагностика «напихивания» контекста против грамотной инженерии контекста.

- **Ключевые навыки:** разгрузка промптов; управляемость ИИ-процессов.
- **Задачи:** когда ИИ-процесс раздут и нестабилен.
- **Сочетается с:** `ecc/context-budget`, `claude-skills/senior-prompt-engineer`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `ecc/continuous-agent-loop`

Непрерывные автономные циклы агентов с гейтами качества, оценками и восстановлением.

- **Ключевые навыки:** самопроверка; eval-гейты; восстановление после сбоев.
- **Задачи:** запустить агента в цикле, который сам себя контролирует.
- **Сочетается с:** `ecc/autonomous-agent-harness`, `ecc/eval-harness`, `ecc/loop-design-check`

### `ecc/cost-aware-llm-pipeline`

Снижение затрат на LLM API — маршрутизация моделей по сложности, бюджеты, ретраи, кэширование промптов.

- **Ключевые навыки:** выбор модели под задачу; учёт бюджета; логика повторов; prompt caching.
- **Задачи:** уменьшить расходы на LLM; распределить задачи по уровням моделей.
- **Сочетается с:** `ecc/prompt-caching-strategy`, `ecc/cost-tracking`, `ecc/token-budget-advisor`

### `ecc/counterparty-channel-discipline`

Правила поведения агента в общих каналах с внешними участниками.

- **Ключевые навыки:** отвечать только при упоминании; молчаливое наблюдение; защита внутреннего контекста; рискованное — только черновиком на одобрение.
- **Задачи:** безопасно подключить агента к групповым чатам и каналам с клиентами.
- **Сочетается с:** `ecc/operator-approval-loop`, `ecc/messages-ops`, `ecc/agent-security-hardening`

### `claude-skills/deep-learning-book`

Изучение и применение учебника «Deep Learning» Гудфеллоу, Бенжио и Курвилля с оценкой актуальности советов.

- **Ключевые навыки:** указатель по всем 20 главам; что устарело, а что работает.
- **Задачи:** разобраться в теории глубокого обучения.
- **Сочетается с:** `ecc/pytorch-patterns`, `claude-skills/spinning-up-deep-rl`

### `ecc/dmux-workflows`

Оркестрация нескольких агентов в панелях tmux через dmux.

- **Ключевые навыки:** параллельная работа Claude Code, Codex, OpenCode; разделение задач по панелям.
- **Задачи:** запустить несколько агентов одновременно и следить за ними.
- **Сочетается с:** `ecc/claude-devfleet`, `ecc/team-agent-orchestration`, `ecc/terminal-ops`

### `ecc/dynamic-workflow-mode`

Локальные для задачи обвязки, eval-гейты и извлечение навыков в адаптивных агентных режимах.

- **Ключевые навыки:** обвязка под задачу; оценочные гейты; извлечение переиспользуемого навыка.
- **Задачи:** построить временную обвязку для сложной задачи агента.
- **Сочетается с:** `ecc/eval-harness`, `ecc/continuous-learning-v2`

### `ecc/enterprise-agent-ops`

Операционный контроль долгоживущих и облачных агентных систем.

- **Ключевые навыки:** жизненный цикл; логи, метрики, трейсы; минимальные права; аварийный выключатель.
- **Задачи:** эксплуатировать агентов в продакшене безопасно и наблюдаемо.
- **Сочетается с:** `ecc/autonomous-agent-harness`, `ecc/agent-security-hardening`, `ecc/dashboard-builder`

### `ecc/eval-harness`

Разработка через оценки (EDD) для ИИ-сессий — сначала определяются проверки возможностей и регрессий, затем пишется код.

- **Ключевые навыки:** оценки кодом, моделью, правилами и человеком; метрики pass@k; регрессионные eval.
- **Задачи:** формально проверять, что ИИ-разработка достигает цели и ничего не ломает.
- **Сочетается с:** `ecc/agent-eval`, `ecc/tdd-workflow`, `ecc/verification-loop`

### `claude-skills/eval`

Ранжирование агентов AgentHub по метрике или решению судьи.

- **Ключевые навыки:** сравнение результатов агентов.
- **Задачи:** определить, какой агент победил.
- **Сочетается с:** `claude-skills/agenthub`, `claude-skills/merge`

### `claude-skills/fable-goal`

Написание промпта-цели для команды /goal вместо самой реализации.

- **Ключевые навыки:** формулировка цели; критерии готовности.
- **Задачи:** поставить агенту долгую цель правильно.
- **Сочетается с:** `ecc/prompt-optimizer`

### `ecc/gan-style-harness`

Обвязка «генератор–оценщик» по мотивам GAN для автономного создания качественных приложений.

- **Ключевые навыки:** агент-генератор и агент-критик; итерации до прохождения оценки.
- **Задачи:** собрать фичу, где важна высокая планка качества, без постоянного участия человека.
- **Сочетается с:** `ecc/eval-harness`, `ecc/santa-method`, `ecc/continuous-agent-loop`

### `claude-skills/grade-iterate`

Оценка запущенного управляемого агента по рубрике и его улучшение.

- **Ключевые навыки:** рубрика результата; итерации улучшения.
- **Задачи:** понять, достаточно ли хорош агент.
- **Сочетается с:** `claude-skills/agent-launcher-orchestrator`, `claude-skills/run-without-you`

### `claude-skills/hivemind`

Делегирование рутины бесплатным воркерам opencode вместо токенов Claude.

- **Ключевые навыки:** один воркер или рой разведчик–кодер–тестировщик.
- **Задачи:** сэкономить на рутинных задачах.
- **Сочетается с:** `ecc/cost-aware-llm-pipeline`, `ecc/dmux-workflows`

### `claude-skills/hub-init`

Старт соревнования агентов AgentHub — задача, число агентов, критерии оценки.

- **Ключевые навыки:** настройка соревнования.
- **Задачи:** запустить конкурс решений между агентами.
- **Сочетается с:** `claude-skills/hub-run`, `claude-skills/agenthub`

### `claude-skills/hub-run`

Полный прогон соревнования AgentHub — инициализация, базовая линия, запуск, оценка, слияние.

- **Ключевые навыки:** сквозной конвейер соревнования.
- **Задачи:** получить лучшее решение из нескольких агентов.
- **Сочетается с:** `claude-skills/hub-init`, `claude-skills/eval`, `claude-skills/merge`

### `claude-skills/hub-status`

Прогресс агентов AgentHub, ветки и состояние графа.

- **Ключевые навыки:** мониторинг соревнования.
- **Задачи:** узнать, как идут агенты.
- **Сочетается с:** `claude-skills/hub-run`

### `scientific/hugging-science`

Поиск научных моделей, наборов данных и Spaces в Hugging Science.

- **Ключевые навыки:** каталог ресурсов; версии; проверка интерфейсов
- **Задачи:** Выбрать подходящий научный ML-ресурс и проверить способ его использования.
- **Сочетается с:** `scientific/transformers`

### `scientific/hypogenic`

Планирование и аудит LLM-генерации гипотез из размеченных текстов в HypoGeniC.

- **Ключевые навыки:** HypoRefine; task configs; банки гипотез
- **Задачи:** Подготовить проверяемый эксперимент на размеченных текстовых данных.
- **Сочетается с:** `scientific/hypothesis-generation`

### `claude-skills/interview`

Интервью для определения рамок агента перед запуском.

- **Ключевые навыки:** одна задача агента; лист сборки.
- **Задачи:** продумать агента до его создания.
- **Сочетается с:** `claude-skills/stage-launch`, `claude-skills/agent-launcher-orchestrator`

### `ecc/iterative-retrieval`

Пошаговое уточнение поиска контекста для субагентов.

- **Ключевые навыки:** итеративный поиск; дополнение недостающего контекста.
- **Задачи:** обеспечить субагенту контекст, которого ему не хватает.
- **Сочетается с:** `ecc/search-first`, `ecc/team-agent-orchestration`

### `ecc/ito-compute`

Аренда GPU через Itô — инвентарь, заявки RFQ, статус закупки.

- **Ключевые навыки:** запрос вычислительных ресурсов; управление учётными данными устройств.
- **Задачи:** забронировать GPU для обучения или инференса.
- **Сочетается с:** `ecc/ito-training`, `ecc/ito-inference`

### `ecc/ito-inference`

Запуск сервинга моделей на забронированных мощностях Itô.

- **Ключевые навыки:** проверка доступности; подтверждённая передача задачи.
- **Задачи:** развернуть модель на арендованных GPU.
- **Сочетается с:** `ecc/ito-compute`

### `ecc/ito-training`

Запуск обучения моделей на забронированных мощностях Itô.

- **Ключевые навыки:** проверка доступности; передача задачи обучения.
- **Задачи:** обучить модель на арендованных GPU.
- **Сочетается с:** `ecc/ito-compute`, `ecc/mle-workflow`

### `claude-skills/llm-cost-optimizer`

Контроль затрат на LLM-функции — выбор модели, кэширование, лимиты токенов, расходы по фичам.

- **Ключевые навыки:** маршрутизация; бюджеты; мониторинг затрат.
- **Задачи:** удержать стоимость ИИ-функций под контролем.
- **Сочетается с:** `ecc/cost-aware-llm-pipeline`, `ecc/prompt-caching-strategy`

### `ecc/loop-design-check`

Проектирование или ревью целевого цикла агента на типичные сбои.

- **Ключевые навыки:** зацикливание; «обман» проверяющего; доведение неверного ответа до конца; машинно-проверяемые критерии остановки.
- **Задачи:** убедиться, что агентный цикл сходится к правильному результату.
- **Сочетается с:** `ecc/continuous-agent-loop`, `ecc/eval-harness`

### `claude-skills/loop-library`

Каталог повторяемых циклов ИИ-агентов — поиск, сравнение, аудит, адаптация, проектирование.

- **Ключевые навыки:** триггеры; действия; проверка; условия остановки.
- **Задачи:** подобрать или спроектировать надёжный агентный цикл.
- **Сочетается с:** `ecc/loop-design-check`, `ecc/continuous-agent-loop`

### `claude-skills/mcp-oauth-triage`

Диагностика MCP-коннектора, который перестал проходить авторизацию.

- **Ключевые навыки:** ошибки 401; обновление токена; аномалии OAuth.
- **Задачи:** починить сломанный MCP-коннектор.
- **Сочетается с:** `claude-skills/mcp-server-builder`, `ecc/mcp-server-patterns`

### `claude-skills/mcp-server-builder`

Превращение API в MCP-сервер на Python или TypeScript.

- **Ключевые навыки:** генерация обёрток инструментов; каркас сервера.
- **Задачи:** подключить свой API к агентам.
- **Сочетается с:** `ecc/mcp-server-patterns`, `claude-skills/mcp-oauth-triage`

### `ecc/mcp-server-patterns`

Создание MCP-серверов на Node/TypeScript SDK.

- **Ключевые навыки:** инструменты, ресурсы, промпты; валидация Zod; stdio и Streamable HTTP.
- **Задачи:** написать свой MCP-сервер для подключения сервиса к агенту.
- **Сочетается с:** `ecc/agent-harness-construction`, `ecc/mcp-dependency-review`

### `claude-skills/memory-engineering`

Проектирование памяти агента — длинный контекст, RAG, граф или агентная память, что забывать.

- **Ключевые навыки:** выбор архитектуры памяти; политика устаревания.
- **Задачи:** добавить агенту память правильно.
- **Сочетается с:** `claude-skills/rag-architect`, `ecc/unified-memory`

### `claude-skills/merge`

Слияние победившей ветки AgentHub, архивирование остальных и чистка worktree.

- **Ключевые навыки:** финализация соревнования.
- **Задачи:** забрать лучший результат.
- **Сочетается с:** `claude-skills/eval`, `claude-skills/hub-run`

### `ecc/ml-adoption-playbook`

Методика добавления машинного обучения в существующий код без ML.

- **Ключевые навыки:** постановка задачи; готовность данных; архитектура; оценка; внедрение.
- **Задачи:** понять, нужна ли модель, и встроить её.
- **Сочетается с:** `ecc/mle-workflow`, `ecc/pytorch-patterns`

### `ecc/mle-workflow`

Продакшен-процесс ML-инженерии.

- **Ключевые навыки:** контракты данных; воспроизводимое обучение; оценка; деплой; мониторинг; откат.
- **Задачи:** вывести ML-модель в продакшен и сопровождать её.
- **Сочетается с:** `ecc/ml-adoption-playbook`, `ecc/pytorch-patterns`, `ecc/recsys-pipeline-architect`

### `ecc/openclaw-persona-forge`

Создание персонажа для агента OpenClaw (навык на китайском).

- **Ключевые навыки:** идентичность; описание «души» (SOUL.md); ролевые правила; имя.
- **Задачи:** придумать характер и правила поведения агента.
- **Сочетается с:** `ecc/agentic-os`

### `ecc/operator-approval-loop`

Контракт одобрения оператором исходящих сообщений, подготовленных агентом.

- **Ключевые навыки:** хеширование черновиков; решения с эпохами; квитанции доставки; аудит.
- **Задачи:** агент пишет, человек одобряет перед отправкой.
- **Сочетается с:** `ecc/counterparty-channel-discipline`, `ecc/email-ops`

### `ecc/parallel-execution-optimizer`

Ускорение задачи через граф параллельных «дорожек» работы.

- **Ключевые навыки:** матрица дорожек; пакетные чтения и проверки; изоляция записей по файлам и worktree.
- **Задачи:** разбить большую задачу на параллельные потоки агентов.
- **Сочетается с:** `ecc/team-agent-orchestration`, `ecc/claude-devfleet`, `ecc/blueprint`

### `ecc/prompt-caching-strategy`

Повышение доли попаданий в кэш промптов для снижения стоимости и задержек LLM.

- **Ключевые навыки:** анализ структуры промпта; разделение кэшируемого и изменяемого; рекомендации.
- **Задачи:** удешевить и ускорить работу LLM-приложения.
- **Сочетается с:** `ecc/cost-aware-llm-pipeline`, `ecc/token-budget-advisor`

### `claude-skills/prompt-governance`

Промпты в продакшене — версии, реестр, A/B-тесты, регрессии, eval-конвейер.

- **Ключевые навыки:** процесс выпуска промптов.
- **Задачи:** управлять промптами как кодом.
- **Сочетается с:** `claude-skills/senior-prompt-engineer`, `ecc/eval-harness`

### `ecc/prompt-optimizer`

Анализ черновика промпта и выдача улучшенной версии.

- **Ключевые навыки:** определение намерения; поиск недостающего контекста; подбор команд, навыков и агентов ECC.
- **Задачи:** превратить сырой запрос в сильный промпт.
- **Сочетается с:** `ecc/ecc-recipes`, `ecc/search-first`

### `scientific/pufferlib`

Версионно корректная работа с RL-средами и обучением PufferLib.

- **Ключевые навыки:** vectorization; PuffeRL; checkpoint review
- **Задачи:** Подготовить RL-эксперимент с учётом различий API 3/4/5.
- **Сочетается с:** `scientific/stable-baselines3`

### `scientific/pytorch-lightning`

Организация обучения нейросетей с PyTorch Lightning.

- **Ключевые навыки:** LightningModule; Trainer; DDP/FSDP и callbacks
- **Задачи:** Собрать воспроизводимый обучающий процесс и мониторинг.
- **Сочетается с:** `scientific/get-available-resources`

### `ecc/pytorch-patterns`

Глубокое обучение на PyTorch.

- **Ключевые навыки:** пайплайны обучения; архитектуры моделей; загрузка данных; воспроизводимость.
- **Задачи:** построить и обучить нейросеть.
- **Сочетается с:** `ecc/mle-workflow`, `ecc/ml-adoption-playbook`

### `claude-skills/rag-architect`

Проектирование RAG-конвейера.

- **Ключевые навыки:** размер чанков; модель эмбеддингов; векторная БД; метрики качества поиска.
- **Задачи:** построить поиск по своим документам с ИИ.
- **Сочетается с:** `claude-skills/memory-engineering`, `ecc/iterative-retrieval`

### `ecc/ralphinho-rfc-pipeline`

Разбиение RFC на граф задач для нескольких агентов.

- **Ключевые навыки:** рабочие единицы с зависимостями и тестами приёмки; исследование, план, реализация, тест, ревью.
- **Задачи:** реализовать большой RFC силами агентов.
- **Сочетается с:** `ecc/team-agent-orchestration`, `ecc/blueprint`

### `ecc/recsys-pipeline-architect`

Проектирование рекомендательных, ранжирующих и ленточных систем по шестиэтапной схеме.

- **Ключевые навыки:** Source, Hydrator, Filter, Scorer, Selector, SideEffect.
- **Задачи:** построить ленту рекомендаций или ранжирование.
- **Сочетается с:** `ecc/mle-workflow`, `ecc/redis-patterns`

### `ecc/regex-vs-llm-structured-text`

Выбор между регулярными выражениями и LLM для разбора структурированного текста.

- **Ключевые навыки:** гибридный конвейер — regex для 95% случаев, LLM для остального.
- **Задачи:** дёшево и точно разбирать анкеты, счета, чеки, таблицы.
- **Сочетается с:** `ecc/cost-aware-llm-pipeline`, `ecc/data-scraper-agent`

### `claude-skills/run-without-you`

Запуск оценённого управляемого агента по расписанию, событию или по запросу.

- **Ключевые навыки:** проверка cron; триггеры.
- **Задачи:** чтобы агент работал сам каждое утро.
- **Сочетается с:** `claude-skills/grade-iterate`, `claude-skills/wrap-up`

### `scientific/scikit-learn`

Классическое машинное обучение и воспроизводимые pipeline в scikit-learn.

- **Ключевые навыки:** preprocessing; CV; подбор гиперпараметров
- **Задачи:** Обучить и оценить модель с корректным разбиением данных.
- **Сочетается с:** `scientific/shap`, `scientific/statistical-analysis`

### `claude-skills/self-eval`

Честная оценка завершённой работы по двум осям с проходом «адвоката дьявола».

- **Ключевые навыки:** защита от завышения оценки.
- **Задачи:** понять, насколько хорошо выполнена задача.
- **Сочетается с:** `ecc/agent-self-evaluation`

### `claude-skills/senior-computer-vision`

Модели компьютерного зрения — детекция, сегментация, обучение своей модели, оптимизация инференса.

- **Ключевые навыки:** YOLO, DETR, SAM, ONNX.
- **Задачи:** решить задачу распознавания изображений.
- **Сочетается с:** `ecc/pytorch-patterns`, `claude-skills/senior-ml-engineer`

### `claude-skills/senior-ml-engineer`

Вывод ML-моделей и LLM-функций в продакшен.

- **Ключевые навыки:** MLOps; мониторинг дрейфа; RAG; стоимость и ретраи LLM API.
- **Задачи:** эксплуатировать ML в продакшене.
- **Сочетается с:** `ecc/mle-workflow`, `claude-skills/rag-architect`

### `claude-skills/senior-prompt-engineer`

Улучшение промптов и измерение качества LLM.

- **Ключевые навыки:** исправление нестабильных промптов; наборы для оценки; оценка поиска RAG; настройки инструментов агента.
- **Задачи:** сделать ответы LLM стабильными и измеримыми.
- **Сочетается с:** `claude-skills/prompt-governance`, `ecc/prompt-optimizer`

### `claude-skills/setup`

Запуск нового эксперимента autoresearch — цель, команда оценки, метрика, направление.

- **Ключевые навыки:** настройка эксперимента.
- **Задачи:** начать автоматическую оптимизацию.
- **Сочетается с:** `claude-skills/autoresearch-agent`

### `scientific/shap`

Объяснение и аудит прогнозов машинного обучения с SHAP.

- **Ключевые навыки:** explainers и maskers; атрибуции; multi-output
- **Задачи:** Проверить интерпретацию локальных и глобальных вкладов признаков.
- **Сочетается с:** `scientific/scikit-learn`

### `claude-skills/spawn`

Запуск соревнующихся агентов AgentHub в изолированных worktree.

- **Ключевые навыки:** параллельный запуск.
- **Задачи:** стартовать соревнование агентов.
- **Сочетается с:** `claude-skills/hub-run`

### `claude-skills/spinning-up-deep-rl`

Глубокое обучение с подкреплением по OpenAI Spinning Up.

- **Ключевые навыки:** policy gradients; VPG, PPO, SAC, TD3, DDPG, TRPO.
- **Задачи:** обучить RL-агента.
- **Сочетается с:** `claude-skills/deep-learning-book`, `ecc/pytorch-patterns`

### `scientific/stable-baselines3`

Обучение одиночного RL-агента с Stable Baselines3.

- **Ключевые навыки:** PPO/SAC/DQN; Gymnasium; normalization и checkpoints
- **Задачи:** Подготовить воспроизводимые rollout и оценку политики.
- **Сочетается с:** `scientific/pufferlib`

### `claude-skills/stage-launch`

Запуск управляемого агента по готовому листу сборки.

- **Ключевые навыки:** генерация и проверка API-запросов.
- **Задачи:** задеплоить агента.
- **Сочетается с:** `claude-skills/interview`, `claude-skills/grade-iterate`

### `ecc/team-agent-orchestration`

Командная оркестрация отрядов агентов.

- **Ключевые навыки:** рабочие задачи с владельцами; канбан агентов; изоляция веток; гейты слияния.
- **Задачи:** организовать работу нескольких агентов как команды.
- **Сочетается с:** `ecc/claude-devfleet`, `ecc/team-builder`, `ecc/parallel-execution-optimizer`

### `ecc/team-builder`

Интерактивный подбор команды агентов-персон под задачу.

- **Ключевые навыки:** поиск доступных персон; группировка по доменам; выбор состава.
- **Задачи:** собрать команду агентов для проекта.
- **Сочетается с:** `ecc/team-agent-orchestration`, `ecc/dev-team`

### `scientific/timesfm-forecasting`

Прогнозирование временных рядов с TimesFM и проверкой на отложенном периоде.

- **Ключевые навыки:** регулярная сетка; квантили; XReg
- **Задачи:** Подготовить прогноз с явной версией модели и условиями лицензии весов.
- **Сочетается с:** `scientific/aeon`, `scientific/statsmodels`

### `scientific/torch-geometric`

Графовые нейросети в PyTorch Geometric.

- **Ключевые навыки:** GCN/GAT/GraphSAGE; heterogeneous graphs; sampling
- **Задачи:** Собрать и проверить модель для узлов, рёбер или целых графов.
- **Сочетается с:** `scientific/networkx`, `scientific/torchdrug`

### `scientific/transformers`

Загрузка, вывод и дообучение моделей Hugging Face Transformers.

- **Ключевые навыки:** AutoModel/tokenizers; pipeline; Trainer
- **Задачи:** Реализовать NLP, vision, audio или мультимодальную задачу.
- **Сочетается с:** `scientific/hugging-science`, `scientific/pytorch-lightning`

### `scientific/umap-learn`

Нелинейное снижение размерности с UMAP-learn.

- **Ключевые навыки:** 2D/3D; DensMAP; supervised/parametric UMAP
- **Задачи:** Получить исследовательские эмбеддинги и проверить чувствительность представления.
- **Сочетается с:** `scientific/scikit-learn`, `scientific/scanpy`

### `ecc/unified-memory`

Общая память и передача контекста между Claude, Codex, Cursor и другими агентами через ECC Memory Vault.

- **Ключевые навыки:** долговечный проверяемый контекст; передача задач между агентами.
- **Задачи:** продолжить работу другим агентом без потери контекста.
- **Сочетается с:** `ecc/ck`, `ecc/knowledge-ops`

### `claude-skills/workflow-builder`

Скрипты Workflow для Claude Code — fan-out, конвейеры, циклы, панели судей субагентов.

- **Ключевые навыки:** оркестрация субагентов кодом.
- **Задачи:** автоматизировать многоагентный процесс.
- **Сочетается с:** `ecc/team-agent-orchestration`

### `claude-skills/wrap-up`

Завершение работы над управляемым агентом — инвентаризация созданного.

- **Ключевые навыки:** что вы теперь владеете; документация.
- **Задачи:** аккуратно закрыть проект агента.
- **Сочетается с:** `claude-skills/run-without-you`

---

<a id="cat-eng-process"></a>
## Архитектура, планирование и процесс разработки

**Область применения.** Архитектурные решения, декомпозиция задач, планы на несколько PR, git-процессы, оценка влияния изменений, работа с унаследованным кодом.

**Решаемые задачи.** План реализации фичи; ADR и фиксация решений; анализ влияния изменений; онбординг в чужой код; стандарты кода; сообщения коммитов; ретроспективы.

**Типовые связки.** codebase-onboarding → blueprint / plan-* (план) → architecture-decision-records → реализация → change-impact → conventional-commit-review → git-workflow.

Навыков в категории: 49.

### `ecc/ai-first-engineering`

Операционная модель команды, где значительную часть кода пишут ИИ-агенты.

- **Ключевые навыки:** процессы ревью ИИ-кода; правила владения кодом; quality gates.
- **Задачи:** настроить процесс команды и ответственность для кодовой базы, написанной агентами.
- **Сочетается с:** `ecc/agentic-engineering`, `ecc/ai-regression-testing`, `ecc/delivery-gate`

### `ecc/architecture-decision-records`

Фиксация архитектурных решений в нумерованных ADR-файлах в docs/adr с контекстом, альтернативами и последствиями.

- **Ключевые навыки:** формат ADR; индекс решений; описание компромиссов.
- **Задачи:** записать решение о выборе фреймворка или БД; объяснить, почему кодовая база устроена именно так.
- **Сочетается с:** `ecc/context-and-decisions`, `ecc/blueprint`, `ecc/change-impact`

### `ecc/blueprint`

Превращение цели из одной строки в пошаговый план для многосессионных и мультиагентных проектов.

- **Ключевые навыки:** шаги размером в один PR; брифы с контекстом; граф зависимостей и параллельные шаги; состязательное ревью плана.
- **Задачи:** спланировать крупную фичу, рефакторинг или roadmap на несколько PR.
- **Сочетается с:** `ecc/plan-orchestrate`, `ecc/architecture-decision-records`, `ecc/team-agent-orchestration`

### `ecc/brownfield-retrospective`

Ретроспективный прогон инженерного процесса ECC по существующему проекту с реестром пробелов.

- **Ключевые навыки:** аудит текущего состояния; реконструкция прошлых решений; реестр пробелов по 4 осям; исправления через план–TDD–ревью.
- **Задачи:** подключить процесс в середине проекта; принять унаследованную кодовую базу.
- **Сочетается с:** `ecc/codebase-onboarding`, `ecc/change-impact`, `ecc/tdd-workflow`

### `ecc/change-impact`

Анализ влияния изменения до его внесения и сверка плана с фактическим диффом после.

- **Ключевые навыки:** пути вызовов; данные и схемы; API-контракты; тесты, документация, деплой, откат.
- **Задачи:** оценить «радиус поражения» рискованного изменения — миграции, авторизации, публичного API.
- **Сочетается с:** `ecc/database-migrations`, `ecc/architecture-decision-records`, `ecc/module-regression`

### `claude-skills/changelog-generator`

Release notes и CHANGELOG.md из коммитов с выбором следующей версии semver.

- **Ключевые навыки:** группировка изменений; определение версии.
- **Задачи:** подготовить релиз и описание изменений.
- **Сочетается с:** `claude-skills/commit-craft`, `ecc/github-ops`

### `claude-skills/codebase-onboarding`

Объяснение незнакомого репозитория — архитектурный бриф и документы для онбординга.

- **Ключевые навыки:** структура проекта; точки входа; соглашения.
- **Задачи:** быстро разобраться в новом проекте.
- **Сочетается с:** `ecc/codebase-onboarding`, `claude-skills/code-tour`

### `ecc/codebase-onboarding`

Анализ незнакомой кодовой базы и создание руководства для входа с картой архитектуры и стартовым CLAUDE.md.

- **Ключевые навыки:** карта архитектуры; ключевые точки входа; соглашения проекта.
- **Задачи:** быстро войти в новый проект; настроить Claude Code для репозитория.
- **Сочетается с:** `ecc/code-tour`, `ecc/repo-scan`, `ecc/brownfield-retrospective`

### `ecc/coding-standards`

Базовые межпроектные соглашения по коду — именование, читаемость, неизменяемость.

- **Ключевые навыки:** правила именования; читаемость; ревью качества кода.
- **Задачи:** ревью кода, когда нет специализированного навыка под фреймворк.
- **Сочетается с:** `ecc/codehealth-mcp`, `ecc/error-handling`

### `claude-skills/commit-craft`

Превращение смеси изменений в чистые коммиты с хорошими сообщениями.

- **Ключевые навыки:** разбиение на логичные коммиты; блокировка секретов и .env.
- **Задачи:** аккуратно закоммитить работу.
- **Сочетается с:** `ecc/conventional-commit-review`, `claude-skills/changelog-generator`

### `ecc/contract-first`

Согласование фронтенда, бэкенда и сервисов через единый машинно-проверяемый контракт.

- **Ключевые навыки:** OpenAPI, AsyncAPI, Protobuf, JSON Schema; генерация типов; проверка интеграции по контракту.
- **Задачи:** вести параллельную разработку без расхождения полей и моков.
- **Сочетается с:** `ecc/api-design`, `ecc/typescript-patterns`, `ecc/e2e-testing`

### `ecc/conventional-commit-review`

Ревью изменений в индексе и черновик сообщения коммита по Conventional Commits.

- **Ключевые навыки:** выбор типа и scope; длина и формат сообщения.
- **Задачи:** написать или исправить сообщение коммита.
- **Сочетается с:** `ecc/git-workflow`, `ecc/github-ops`

### `claude-skills/cto-advisor`

Решения CTO — техдолг, архитектура, масштабирование инженерной команды, выбор технологий, метрики DORA.

- **Ключевые навыки:** оценка технологий; рост команды; метрики поставки.
- **Задачи:** принять техническое решение уровня руководства.
- **Сочетается с:** `claude-skills/cto-review`, `ecc/architecture-decision-records`

### `claude-skills/cto-review`

Критика архитектурной ставки, плана масштабирования в 10 раз или решения переписать против купить.

- **Ключевые навыки:** позиция технического директора.
- **Задачи:** проверить технический план.
- **Сочетается с:** `claude-skills/cto-advisor`

### `ecc/dev-team`

Имитация командной сессии с ролями PM, архитектор, разработчик и QA над одной задачей.

- **Ключевые навыки:** взгляд с разных ролей; обсуждение компромиссов.
- **Задачи:** спроектировать фичу; отревьюить решение с нескольких сторон.
- **Сочетается с:** `ecc/council`, `ecc/blueprint`, `ecc/product-lens`

### `claude-skills/engineering-advanced-skills`

Выбор подходящего продвинутого инженерного навыка — агенты, RAG, MCP, CI/CD, БД, наблюдаемость, релизы.

- **Ключевые навыки:** маршрутизация по навыкам.
- **Задачи:** понять, какой навык использовать.
- **Сочетается с:** `claude-skills/engineering-skills`

### `claude-skills/engineering-skills`

Выбор инженерного навыка под задачу — архитектура, фронтенд, бэкенд, QA, DevOps, безопасность, ML, данные, облака.

- **Ключевые навыки:** маршрутизация по навыкам инженерной команды.
- **Задачи:** найти правильного «специалиста» для задачи.
- **Сочетается с:** `claude-skills/engineering-advanced-skills`

### `claude-skills/focused-fix`

Исправление целиком сломанной фичи или модуля.

- **Ключевые навыки:** карта всех файлов и зависимостей; сквозное исправление.
- **Задачи:** заставить работать сломанный модуль.
- **Сочетается с:** `claude-skills/red-green-proof`, `ecc/orch-fix-defect`

### `ecc/git-workflow`

Git-процессы — ветвление, соглашения коммитов, чистая история, merge и rebase, конфликты.

- **Ключевые навыки:** стратегии веток; приведение коммитов в порядок; разрешение конфликтов.
- **Задачи:** настроить командный git-процесс; навести порядок в истории перед мержем.
- **Сочетается с:** `ecc/conventional-commit-review`, `ecc/github-ops`

### `claude-skills/git-worktree-manager`

Параллельная работа нескольких веток или агентов в одном репозитории через worktree.

- **Ключевые навыки:** изолированные порты и окружения.
- **Задачи:** запустить несколько агентов без конфликтов.
- **Сочетается с:** `ecc/claude-devfleet`, `ecc/team-agent-orchestration`

### `claude-skills/grill-me`

Неустанные вопросы о плане или дизайне до полного взаимопонимания.

- **Ключевые навыки:** проход по дереву решений.
- **Задачи:** проверить, всё ли продумано в плане.
- **Сочетается с:** `claude-skills/grill-with-docs`, `ecc/council`

### `claude-skills/grill-with-docs`

Стресс-тест плана против собственной документации проекта — глоссария и ADR.

- **Ключевые навыки:** сверка с CONTEXT.md и docs/adr.
- **Задачи:** убедиться, что план не противоречит принятым решениям.
- **Сочетается с:** `claude-skills/grill-me`, `ecc/context-and-decisions`

### `ecc/hexagonal-architecture`

Архитектура «порты и адаптеры» с чёткими границами домена.

- **Ключевые навыки:** инверсия зависимостей; оркестрация use case; тестируемость.
- **Задачи:** спроектировать или переработать систему с изолированным доменом.
- **Сочетается с:** `ecc/android-clean-architecture`, `ecc/architecture-decision-records`

### `claude-skills/human-gate`

Страница ревью для одобрения человеком перед необратимым действием.

- **Ключевые навыки:** план, спецификация, отчёт, миграция на подпись.
- **Задачи:** получить явное одобрение перед выпуском.
- **Сочетается с:** `ecc/operator-approval-loop`, `ecc/plan-canvas`

### `ecc/inherit-legacy-style`

Защита от «стилевого дрейфа» ИИ в легаси-проекте.

- **Ключевые навыки:** выявление неявных соглашений; разбор конфликтов с владельцем; запись правил стиля.
- **Задачи:** чтобы агент писал так же, как написан старый код.
- **Сочетается с:** `ecc/coding-standards`, `ecc/codebase-onboarding`

### `ecc/intent-driven-development`

Превращение размытых или важных изменений в проверяемые критерии приёмки.

- **Ключевые навыки:** уточнение намерения; измеримые критерии; связь с реализацией.
- **Задачи:** прояснить требования до начала работы.
- **Сочетается с:** `ecc/blueprint`, `ecc/product-capability`, `ecc/tdd-workflow`

### `ecc/issue-review`

Ревью GitHub-issue по аналогии с ревью PR.

- **Ключевые навыки:** сверка с текущим кодом; поиск дублей и прошлых PR; вывод о состоятельности.
- **Задачи:** разобрать новый баг-репорт или запрос.
- **Сочетается с:** `ecc/github-ops`, `ecc/change-impact`

### `claude-skills/minimalist`

Писать минимум кода — без переусложнения и лишних зависимостей.

- **Ключевые навыки:** YAGNI; переиспользование; лестница упрощения.
- **Задачи:** сделать решение проще.
- **Сочетается с:** `claude-skills/karpathy-coder`

### `ecc/module-governance`

Локальные инструкции агента, доменный контекст и владение интерфейсами для бизнес-модуля.

- **Ключевые навыки:** инструкции на уровне модуля; ссылки на контекст; владельцы интерфейсов.
- **Задачи:** создать новый модуль или изменить зону его ответственности.
- **Сочетается с:** `ecc/module-regression`, `ecc/context-and-decisions`

### `ecc/opensource-pipeline`

Подготовка приватного проекта к публикации в open source — форк, очистка, упаковка.

- **Ключевые навыки:** удаление секретов и приватных данных; упаковка; три агента по этапам.
- **Задачи:** безопасно выложить свой проект публично.
- **Сочетается с:** `ecc/security-scan`, `ecc/hermes-imports`

### `ecc/orch-add-feature`

Оркестрация новой фичи от исследования до коммита через агентов ECC.

- **Ключевые навыки:** исследование; план; TDD-реализация; ревью; коммит с проверкой.
- **Задачи:** собрать фичу целиком по отлаженному конвейеру.
- **Сочетается с:** `ecc/orch-pipeline`, `ecc/tdd-workflow`, `ecc/blueprint`

### `ecc/orch-build-mvp`

Сборка рабочего MVP по документу дизайна или спецификации.

- **Ключевые навыки:** тонкие вертикальные срезы; каркас первого среза; итеративное доведение.
- **Задачи:** превратить PRD или SDD в работающий прототип.
- **Сочетается с:** `ecc/orch-pipeline`, `ecc/orch-add-feature`, `ecc/blueprint`

### `ecc/orch-change-feature`

Оркестрация изменения существующей работающей фичи под новое поведение.

- **Ключевые навыки:** обновление тестов под новую спецификацию; изменение реализации; ревью; коммит с проверкой.
- **Задачи:** переделать фичу, не сломав остальное.
- **Сочетается с:** `ecc/orch-pipeline`, `ecc/change-impact`

### `ecc/orch-fix-defect`

Оркестрация исправления бага — воспроизведение падающим тестом, исправление, ревью, коммит.

- **Ключевые навыки:** регрессионный тест на баг; минимальное исправление; ревью.
- **Задачи:** надёжно исправить ошибку, чтобы она не вернулась.
- **Сочетается с:** `ecc/orch-pipeline`, `ecc/tdd-workflow`

### `ecc/orch-pipeline`

Общий движок семейства orch-* — конвейер «исследование, план, TDD, ревью, коммит» с гейтами.

- **Ключевые навыки:** классификатор размера задачи; карта агентов и команд; гейты между этапами.
- **Задачи:** основа для всех orch-навыков; выбор подходящего конвейера.
- **Сочетается с:** `ecc/orch-add-feature`, `ecc/orch-fix-defect`, `ecc/orch-refine-code`

### `ecc/orch-refine-code`

Оркестрация рефакторинга без изменения поведения.

- **Ключевые навыки:** проверка, что тесты зелёные; реструктуризация; сохранение зелёных тестов; ревью.
- **Задачи:** улучшить структуру кода без риска.
- **Сочетается с:** `ecc/orch-pipeline`, `ecc/codehealth-mcp`

### `ecc/plan-canvas`

Просмотр планов и HTML-артефактов в локальном браузерном «холсте» с аннотациями и одобрением.

- **Ключевые навыки:** комментарии к элементам; чат; одобрение или запрос правок.
- **Задачи:** согласовать план с человеком визуально.
- **Сочетается с:** `ecc/blueprint`, `ecc/plan-orchestrate`

### `ecc/plan-orchestrate`

Разбор документа-плана на шаги с готовой командой ECC для каждого шага.

- **Ключевые навыки:** декомпозиция; классификация шагов; генерация slash-команд.
- **Задачи:** исполнить план пошагово готовыми командами.
- **Сочетается с:** `ecc/blueprint`, `ecc/orch-pipeline`

### `ecc/repo-scan`

Установка внешнего навыка repo-scan с зафиксированного коммита.

- **Ключевые навыки:** проверяемая установка; кросс-стековое сканирование репозитория.
- **Задачи:** подготовить инструмент для анализа репозитория.
- **Сочетается с:** `ecc/codebase-onboarding`

### `ecc/search-first`

Сначала поиск готовых решений, потом код.

- **Ключевые навыки:** поиск в npm, PyPI, MCP, навыках и GitHub; решение — взять, доработать или написать.
- **Задачи:** не изобретать велосипед.
- **Сочетается с:** `ecc/documentation-lookup`, `ecc/skill-scout`

### `claude-skills/senior-architect`

Архитектурные решения с письменным обоснованием — монолит или микросервисы, выбор БД, пределы масштабирования.

- **Ключевые навыки:** ADR; диаграммы Mermaid.
- **Задачи:** принять и задокументировать архитектурное решение.
- **Сочетается с:** `ecc/architecture-decision-records`, `claude-skills/tech-stack-evaluator`

### `claude-skills/spec-driven-workflow`

Сначала спецификация, потом код — критерии приёмки и тесты из спецификации.

- **Ключевые навыки:** генерация спецификации; тесты по ней.
- **Задачи:** разработка фичи по спецификации.
- **Сочетается с:** `ecc/intent-driven-development`, `ecc/tdd-workflow`

### `claude-skills/strict-api`

Никаких выдуманных API — проверка функций и версий библиотек перед использованием.

- **Ключевые навыки:** сверка с документацией.
- **Задачи:** исключить галлюцинации в коде.
- **Сочетается с:** `claude-skills/zero-hallucination-coder`, `ecc/documentation-lookup`

### `claude-skills/tc-tracker`

Учёт технических изменений в виде записей и передача работы между сессиями.

- **Ключевые навыки:** создание и проверка записей изменений.
- **Задачи:** вести журнал изменений между сессиями ИИ.
- **Сочетается с:** `claude-skills/session-handoff`

### `claude-skills/tech-debt-tracker`

Поиск, ранжирование и учёт техдолга.

- **Ключевые навыки:** приоритизация рефакторинга; модернизация легаси.
- **Задачи:** решить, что рефакторить первым.
- **Сочетается с:** `ecc/codehealth-mcp`, `ecc/orch-refine-code`

### `claude-skills/tech-stack-evaluator`

Сравнение фреймворков и стеков перед выбором.

- **Ключевые навыки:** балльная оценка; совокупная стоимость; здоровье экосистемы; риски миграции.
- **Задачи:** выбрать технологию обоснованно.
- **Сочетается с:** `claude-skills/senior-architect`

### `claude-skills/vpe-advisor`

Советник VP of Engineering — скорость поставки, найм, структура команды, когда вводить менеджера.

- **Ключевые навыки:** метрики поставки; оргдизайн инженерии.
- **Задачи:** ускорить и масштабировать разработку.
- **Сочетается с:** `claude-skills/vpe-review`, `claude-skills/cto-advisor`

### `claude-skills/vpe-review`

Критика плана по скорости поставки, найму, структуре или дежурствам.

- **Ключевые навыки:** позиция VP of Engineering.
- **Задачи:** проверить инженерный план.
- **Сочетается с:** `claude-skills/vpe-advisor`

### `claude-skills/zero-hallucination-coder`

Аккуратное кодирование в рискованных задачах (авторизация, БД, миграции) без выдуманных API.

- **Ключевые навыки:** дисциплина планирования; проверка фактов.
- **Задачи:** многофайловые изменения без ошибок.
- **Сочетается с:** `claude-skills/strict-api`, `ecc/gateguard`

---

<a id="cat-claude-setup"></a>
## Настройка Claude Code и экосистемы ECC

**Область применения.** Конфигурация Claude Code и других агентных оболочек — навыки, хуки, память, контекст, стоимость, установка ECC.

**Решаемые задачи.** Установка и настройка ECC; чистка конфигурации; контроль контекста и токенов; память между сессиями; создание и проверка навыков; хуки контроля качества.

**Типовые связки.** configure-ecc → agent-sort (что оставить) → context-budget / token-budget-advisor → config-gc (чистка) → skill-stocktake (ревизия навыков).

Навыков в категории: 44.

### `ecc/agent-sort`

План установки ECC под конкретный репозиторий — сортировка навыков, команд, правил и хуков на «ежедневные» и «библиотечные».

- **Ключевые навыки:** анализ репозитория; параллельные проходы ревью; обоснование каждого выбора.
- **Задачи:** урезать ECC до того, что реально нужно проекту; выбрать избранные навыки.
- **Сочетается с:** `ecc/configure-ecc`, `ecc/skill-stocktake`, `ecc/context-budget`

### `ecc/automation-audit-ops`

Инвентаризация автоматизаций — какие задания, хуки, коннекторы и MCP-серверы живы, сломаны, дублируются или отсутствуют.

- **Ключевые навыки:** сбор доказательств; поиск пересечений; карта автоматизаций.
- **Задачи:** понять состояние автоматизаций прежде, чем что-то чинить.
- **Сочетается с:** `ecc/config-gc`, `ecc/workspace-surface-audit`

### `scientific/autoskill`

Поиск повторяющихся исследовательских процессов в явно разрешённой истории Screenpipe.

- **Ключевые навыки:** локальная кластеризация; подбор навыков; черновики
- **Задачи:** Предложить навык или связку по запросу пользователя без скрытого анализа истории.
- **Сочетается с:** `scientific/scientific-critical-thinking`

### `claude-skills/book-to-skill`

Превращение книги, папки документации или спецификаций в навык агента.

- **Ключевые навыки:** извлечение из PDF, EPUB, DOCX, HTML, Markdown; структура навыка.
- **Задачи:** сделать навык из книги или документации.
- **Сочетается с:** `claude-skills/extract`, `ecc/skill-scout`

### `ecc/ck`

Постоянная память проекта для Claude Code (Context Keeper) через команды /ck и хук начала сессии.

- **Ключевые навыки:** сохранение состояния и следующих шагов; возобновление работы; краткий бриф проекта при старте.
- **Задачи:** продолжить проект в новой сессии без повторных объяснений.
- **Сочетается с:** `ecc/unified-memory`, `ecc/strategic-compact`

### `claude-skills/claude-coach`

Коучинг по эффективному использованию Claude.

- **Ключевые навыки:** оценка ваших промптов; приёмы опытных пользователей.
- **Задачи:** научиться работать с Claude продуктивнее.
- **Сочетается с:** `ecc/prompt-optimizer`

### `claude-skills/coding-agent-rollout`

Внедрение Claude Code в команде.

- **Ключевые навыки:** общие и управляемые настройки; одобрение MCP и плагинов; многоуровневый CLAUDE.md; принятие командой.
- **Задачи:** настроить Claude Code для всей команды.
- **Сочетается с:** `ecc/configure-ecc`, `claude-skills/claude-coach`

### `ecc/config-gc`

«Сборка мусора» в конфигурации Claude Code — поиск лишних, устаревших и бесполезных навыков, памяти, хуков и MCP.

- **Ключевые навыки:** сканирование ~/.claude; классификация находок; удаление с подтверждением каждого пункта.
- **Задачи:** почистить раздутую конфигурацию; периодический аудит настроек.
- **Сочетается с:** `ecc/skill-stocktake`, `ecc/context-budget`, `ecc/automation-audit-ops`

### `ecc/configure-ecc`

Мастер установки и настройки ECC в диалоге — область установки, режим хуков, проверка.

- **Ключевые навыки:** инвентаризация установки; выбор scope; профили хуков; превью и применение.
- **Задачи:** установить, обновить, перенастроить или починить ECC.
- **Сочетается с:** `ecc/agent-sort`, `ecc/ecc-guide`, `ecc/skill-host-compat`

### `ecc/context-budget`

Проверка оставшегося контекста через встроенный счётчик и, по запросу, аудит затрат контекста на компоненты.

- **Ключевые навыки:** замер контекста; статический аудит навыков и правил.
- **Задачи:** узнать, сколько контекста осталось и что его съедает.
- **Сочетается с:** `ecc/token-budget-advisor`, `ecc/strategic-compact`, `ecc/config-gc`

### `ecc/continuous-learning-v2`

Система обучения на основе «инстинктов» — наблюдает за сессиями и превращает выводы в навыки, команды и агентов.

- **Ключевые навыки:** атомарные инстинкты с оценкой уверенности; привязка к проекту; продвижение в навыки.
- **Задачи:** сохранять уроки из сессий; постепенно наращивать собственные навыки.
- **Сочетается с:** `ecc/skill-stocktake`, `ecc/rules-distill`

### `ecc/continuous-learning`

Устаревшая версия извлечения навыков из сессий; используйте continuous-learning-v2.

- **Ключевые навыки:** хук на остановку сессии.
- **Задачи:** только для совместимости.
- **Сочетается с:** `ecc/continuous-learning-v2`

### `ecc/cost-tracking`

Отчёты по расходу токенов, затратам и бюджетам Claude Code из локального журнала ECC.

- **Ключевые навыки:** разбивка по моделям, сессиям и датам; бюджеты.
- **Задачи:** узнать, сколько потрачено и на что.
- **Сочетается с:** `ecc/cost-aware-llm-pipeline`, `ecc/token-budget-advisor`

### `ecc/deepseek-harness-setup`

Установка и работа ECC в оболочке DeepSeek Harness.

- **Ключевые навыки:** корни навыков; мост хуков; совместимость команд.
- **Задачи:** перенести настройки ECC в DeepSeek Harness.
- **Сочетается с:** `ecc/configure-ecc`, `ecc/skill-host-compat`

### `ecc/ecc-guide`

Ответы на вопросы о составе ECC по живому содержимому репозитория.

- **Ключевые навыки:** агенты, навыки, команды, хуки, правила, профили установки.
- **Задачи:** узнать, что входит в ECC и как этим пользоваться.
- **Сочетается с:** `ecc/ecc-recipes`, `ecc/configure-ecc`

### `ecc/ecc-recipes`

Подбор группы команд ECC под описанный процесс с порядком запуска и условием остановки.

- **Ключевые навыки:** рецепты команд; справочные семейства команд.
- **Задачи:** понять, какие команды ECC запускать для своей задачи.
- **Сочетается с:** `ecc/ecc-guide`

### `ecc/ecc-tools-cost-audit`

Аудит затрат и биллинга ECC Tools.

- **Ключевые навыки:** поиск лавины PR; обход квот; утечка дорогих моделей; дубли задач.
- **Задачи:** расследовать всплеск затрат GitHub App.
- **Сочетается с:** `ecc/cost-tracking`

### `claude-skills/extract`

Превращение повторяющегося исправления или паттерна в переиспользуемый навык.

- **Ключевые навыки:** SKILL.md; справочные документы; примеры.
- **Задачи:** сохранить находку как навык.
- **Сочетается с:** `claude-skills/write-a-skill`, `claude-skills/promote`

### `ecc/hermes-imports`

Конвертация локальных процессов Hermes в очищенные навыки ECC.

- **Ключевые навыки:** удаление приватных данных; упаковка навыков для публикации.
- **Задачи:** подготовить свой процесс к публичному переиспользованию.
- **Сочетается с:** `ecc/opensource-pipeline`

### `ecc/hookify-rules`

Правила hookify — markdown-файлы, которые предупреждают или блокируют действия агента по шаблонам.

- **Ключевые навыки:** события bash, файлов, промптов и остановки; регулярные выражения и условия.
- **Задачи:** ввести защитные правила для агента без программирования хуков.
- **Сочетается с:** `ecc/delivery-gate`, `ecc/gateguard`, `ecc/safety-guard`

### `claude-skills/memory-review`

Ревью авто-памяти агента — что сделать постоянным правилом, что удалить, что объединить.

- **Ключевые навыки:** продвижение правил; чистка устаревшего.
- **Задачи:** поддерживать память агента в порядке.
- **Сочетается с:** `claude-skills/memory-status`, `claude-skills/promote`

### `claude-skills/memory-status`

Проверка здоровья авто-памяти — объём, файлы тем, устаревшие записи.

- **Ключевые навыки:** метрики памяти; рекомендации по чистке.
- **Задачи:** узнать, насколько заполнена память.
- **Сочетается с:** `claude-skills/memory-review`

### `ecc/nanoclaw-repl`

NanoClaw — REPL от ECC без зависимостей с сессиями в markdown.

- **Ключевые навыки:** переключение моделей; загрузка навыков; управление сессиями.
- **Задачи:** работать с моделями через лёгкий REPL.
- **Сочетается с:** `ecc/ecc-guide`

### `ecc/nasiko-control-plane`

Управление экспериментальным CLI Nasiko через ECC.

- **Ключевые навыки:** проверка статуса; установка с согласия и предпросмотром.
- **Задачи:** установить и контролировать Nasiko.
- **Сочетается с:** `ecc/configure-ecc`

### `scientific/pi-agent`

Настройка и расширение терминального агентного инструмента Pi.

- **Ключевые навыки:** провайдеры; SDK/RPC; skills и extensions
- **Задачи:** Подготовить конфигурацию или интеграцию агентного процесса Pi.
- **Сочетается с:** `scientific/arbor`

### `pm-skills/pm-skill-creator`

Создание нового PM-навыка через диалог.

- **Ключевые навыки:** превращение идеи в навык по стандартам.
- **Задачи:** написать свой продуктовый навык.
- **Сочетается с:** `pm-skills/skill-authoring-workflow`, `claude-skills/write-a-skill`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/promote`

Перевод проверенного паттерна из авто-памяти в CLAUDE.md или правила.

- **Ключевые навыки:** постоянные правила агента.
- **Задачи:** закрепить полезное правило.
- **Сочетается с:** `claude-skills/memory-review`, `claude-skills/remember`

### `claude-skills/remember`

Сохранение важного в авто-память с датой и контекстом.

- **Ключевые навыки:** записи памяти.
- **Задачи:** чтобы агент запомнил что-то на будущее.
- **Сочетается с:** `claude-skills/promote`, `claude-skills/memory-review`

### `ecc/rules-distill`

Извлечение сквозных принципов из навыков и превращение их в правила.

- **Ключевые навыки:** поиск повторяющихся принципов; создание и правка файлов правил.
- **Задачи:** обобщить опыт из навыков в единые правила.
- **Сочетается с:** `ecc/continuous-learning-v2`, `ecc/skill-stocktake`

### `claude-skills/self-improving-agent`

Превращение выученного агентом в долговечные знания проекта.

- **Ключевые навыки:** ревью MEMORY.md; продвижение в правила.
- **Задачи:** чтобы агент становился лучше со временем.
- **Сочетается с:** `claude-skills/memory-review`, `claude-skills/promote`

### `pm-skills/skill-authoring-workflow`

Превращение сырого PM-контента в готовый к публикации навык.

- **Ключевые навыки:** соблюдение стандартов репозитория.
- **Задачи:** оформить навык правильно.
- **Сочетается с:** `pm-skills/pm-skill-creator`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `ecc/skill-comply`

Проверка, действительно ли агенты следуют навыкам и правилам.

- **Ключевые навыки:** сценарии на трёх уровнях строгости; прогон агентов; классификация соблюдения.
- **Задачи:** измерить, работает ли навык на практике.
- **Сочетается с:** `ecc/skill-stocktake`, `ecc/eval-harness`

### `ecc/skill-host-compat`

Проверка навыков на совместимость с Codex и Cursor.

- **Ключевые навыки:** безопасный frontmatter; замена конструкций только для Claude.
- **Задачи:** подготовить навык к публикации для разных оболочек.
- **Сочетается с:** `ecc/skill-stocktake`

### `claude-skills/skill-retro`

Оценка навыков по реальной истории сессий — какие действительно работают.

- **Ключевые навыки:** доказательная оценка навыков.
- **Задачи:** понять, какие навыки оставить.
- **Сочетается с:** `ecc/skill-stocktake`, `ecc/skill-comply`

### `ecc/skill-scout`

Поиск существующих навыков перед созданием нового.

- **Ключевые навыки:** поиск локально, в маркетплейсах, на GitHub и в вебе.
- **Задачи:** найти готовый навык вместо написания своего.
- **Сочетается с:** `ecc/search-first`, `ecc/skill-stocktake`

### `ecc/skill-stocktake`

Аудит качества навыков и команд.

- **Ключевые навыки:** быстрый скан изменённых; полная ревизия пакетами субагентов.
- **Задачи:** найти слабые, устаревшие и дублирующиеся навыки.
- **Сочетается с:** `ecc/config-gc`, `ecc/skill-comply`, `ecc/agent-sort`

### `claude-skills/skill-tester`

Проверка навыка перед выпуском — структура, запуск скриптов, оценка.

- **Ключевые навыки:** валидатор навыков.
- **Задачи:** выпустить качественный навык.
- **Сочетается с:** `claude-skills/write-a-skill`, `ecc/skill-host-compat`

### `claude-skills/skillopt-sleep`

Ночной офлайн-цикл самоулучшения агента по прошлому опыту.

- **Ключевые навыки:** «сон» для оптимизации памяти и навыков.
- **Задачи:** чтобы агент улучшался между сессиями.
- **Сочетается с:** `claude-skills/self-improving-agent`

### `ecc/strategic-compact`

Подсказки сжать контекст в логичные моменты работы.

- **Ключевые навыки:** сохранение важного перед сжатием; переходы между фазами.
- **Задачи:** не терять контекст в длинной сессии.
- **Сочетается с:** `ecc/context-budget`, `ecc/ck`

### `ecc/terminal-opener`

Запуск программы в видимом окне терминала по безопасному плану.

- **Ключевые навыки:** dry-run; JSON-план; определение возможностей системы.
- **Задачи:** открыть процесс в отдельном терминале.
- **Сочетается с:** `ecc/terminal-ops`

### `ecc/token-budget-advisor`

Выбор глубины ответа (25–100%) с оценкой токенов перед ответом.

- **Ключевые навыки:** оценка объёма; управление длиной ответа.
- **Задачи:** экономить токены и контролировать подробность.
- **Сочетается с:** `ecc/context-budget`, `ecc/cost-tracking`

### `ecc/token-card`

Карточка статистики токенов по логам Claude Code, Codex, Gemini CLI и OpenCode.

- **Ключевые навыки:** сбор логов; визуализация; сохранение в репозиторий.
- **Задачи:** показать статистику использования ИИ.
- **Сочетается с:** `ecc/cost-tracking`

### `ecc/workspace-surface-audit`

Аудит репозитория, MCP-серверов, плагинов и окружения с рекомендациями ECC.

- **Ключевые навыки:** инвентаризация; выбор самых полезных навыков, хуков и агентов.
- **Задачи:** понять, что подключить для этого проекта.
- **Сочетается с:** `ecc/agent-sort`, `ecc/automation-audit-ops`

### `claude-skills/write-a-skill`

Создание новых навыков с правильной структурой и ресурсами.

- **Ключевые навыки:** прогрессивное раскрытие; вложенные ресурсы.
- **Задачи:** написать свой навык.
- **Сочетается с:** `claude-skills/skill-tester`, `claude-skills/extract`

---

<a id="cat-docs"></a>
## Документация и управление знаниями

**Область применения.** Техническая документация, README, база знаний, живые документы, справочники по библиотекам, локализация.

**Решаемые задачи.** Написание и актуализация документации; аудит документов; база знаний команды; поиск актуальной документации фреймворков; синхронизация переводов.

**Типовые связки.** documentation-lookup (актуальные доки) → написание → docs-governance / living-docs-governance (аудит) → knowledge-ops (база знаний).

Навыков в категории: 20.

### `claude-skills/code-tour`

Экскурсии по коду в формате CodeTour.

- **Ключевые навыки:** туры под роль; онбординг; архитектура; ревью PR.
- **Задачи:** объяснить устройство кода пошагово.
- **Сочетается с:** `ecc/code-tour`, `claude-skills/codebase-onboarding`

### `ecc/code-tour`

Создание пошаговых экскурсий по коду в формате CodeTour с привязкой к файлам и строкам.

- **Ключевые навыки:** туры под роль читателя; экскурсии по архитектуре, PR и разбору инцидентов.
- **Задачи:** онбординг нового разработчика; объяснить, как работает подсистема.
- **Сочетается с:** `ecc/codebase-onboarding`, `ecc/architecture-decision-records`

### `ecc/context-and-decisions`

Ведение стабильного доменного контекста в CONTEXT.md и передача трудно обратимых решений в ADR.

- **Ключевые навыки:** глоссарий домена; разведение значений терминов; границы модулей.
- **Задачи:** зафиксировать доменные термины, которые постоянно приходится объяснять.
- **Сочетается с:** `ecc/architecture-decision-records`, `ecc/docs-governance`

### `claude-skills/design-system`

Настройка брендовых параметров перед конвертацией markdown в HTML.

- **Ключевые навыки:** онбординг из 10 вопросов; цвета, шрифты, стиль страниц.
- **Задачи:** задать единый стиль для HTML-документов.
- **Сочетается с:** `claude-skills/markdown-html-orchestrator`, `claude-skills/md-document`

### `ecc/docs-governance`

Маршрутизация задач по управлению документацией и аудит ролей документов, ссылок и индексов ADR.

- **Ключевые навыки:** аудит ссылок; индекс ADR; проверка доказательных ссылок.
- **Задачи:** проверить состояние документации проекта.
- **Сочетается с:** `ecc/living-docs-governance`, `ecc/architecture-decision-records`, `ecc/context-and-decisions`

### `ecc/documentation-lookup`

Актуальная документация библиотек и фреймворков через Context7 MCP вместо устаревших знаний модели.

- **Ключевые навыки:** справочник API; примеры кода; вопросы настройки.
- **Задачи:** получить точный ответ по свежей версии React, Next.js и других.
- **Сочетается с:** `ecc/search-first`

### `claude-skills/i18n-localization`

Интернационализация приложения — новые строки, новые языки, ревью переводов.

- **Ключевые навыки:** пропущенные ключи; плейсхолдеры; встраивание i18n.
- **Задачи:** подготовить приложение к нескольким языкам.
- **Сочетается с:** `ecc/i18n-sync`

### `ecc/i18n-sync`

Перевод и синхронизация JSON-файлов локализации приложения.

- **Ключевые навыки:** учёт использования ключей; терминология проекта; валидация.
- **Задачи:** добавить язык или новые ключи и обновить переводы.
- **Сочетается с:** `ecc/visa-doc-translate`

### `claude-skills/knowledge-ops`

Написание, проверка и чистка регламентов (SOP) и ранбуков.

- **Ключевые навыки:** генерация SOP; проверка полноты 5W2H; ссылки.
- **Задачи:** навести порядок в инструкциях компании.
- **Сочетается с:** `claude-skills/process-mapper`, `claude-skills/runbook-generator`

### `ecc/knowledge-ops`

Управление базой знаний на нескольких уровнях хранения — файлы, MCP-память, векторные БД, git.

- **Ключевые навыки:** загрузка и синхронизация знаний; поиск; дедупликация.
- **Задачи:** собрать и поддерживать личную или командную базу знаний.
- **Сочетается с:** `ecc/unified-memory`, `ecc/google-workspace-ops`

### `scientific/liteparse`

Локальное извлечение текста и пространственной разметки из документов.

- **Ключевые навыки:** PDF/Office; OCR; bounding boxes и JSON
- **Задачи:** Подготовить документы к поиску или RAG с сохранением структуры.
- **Сочетается с:** `scientific/markitdown`

### `ecc/living-docs-governance`

Защита документации долгоживущего проекта от устаревания.

- **Ключевые навыки:** роли документов (конституция, карта, статус, история); связка с инструкциями агента.
- **Задачи:** поддерживать документацию актуальной на протяжении жизни проекта.
- **Сочетается с:** `ecc/docs-governance`, `ecc/architecture-decision-records`

### `claude-skills/llm-wiki`

«Второй мозг» в Obsidian, который поддерживает LLM.

- **Ключевые навыки:** загрузка статей, книг, работ; связи между заметками.
- **Задачи:** вести личную базу знаний с помощью ИИ.
- **Сочетается с:** `claude-skills/deepread`, `ecc/knowledge-ops`

### `claude-skills/markdown-html-orchestrator`

Превращение markdown в одностраничный интерактивный HTML — документ, код-ревью или слайды.

- **Ключевые навыки:** классификация документа; выбор шаблона.
- **Задачи:** сделать из markdown красивую веб-страницу.
- **Сочетается с:** `claude-skills/md-document`, `claude-skills/md-slides`, `claude-skills/md-review`

### `scientific/markdown-mermaid-writing`

Научная документация в Markdown и структурные диаграммы Mermaid.

- **Ключевые навыки:** схемы; шаблоны; проверка рендеринга
- **Задачи:** Описать процесс или взаимосвязи в редактируемом текстовом виде.
- **Сочетается с:** `scientific/scientific-writing`

### `scientific/markitdown`

Преобразование поддерживаемых документов и медиа в Markdown с MarkItDown.

- **Ключевые навыки:** Office/PDF; конвертеры; проверка потерь
- **Задачи:** Получить текстовую версию файла для анализа и поиска.
- **Сочетается с:** `scientific/liteparse`

### `claude-skills/md-document`

Длинный markdown (спецификация, RFC, отчёт) в HTML с оглавлением, поиском и копированием кода.

- **Ключевые навыки:** разбор структуры; навигация.
- **Задачи:** сделать документ удобным для чтения в браузере.
- **Сочетается с:** `claude-skills/markdown-html-orchestrator`

### `claude-skills/md-review`

Markdown-ревью кода с диффами в двухколоночную HTML-страницу.

- **Ключевые навыки:** разбор диффов; выделение критичности.
- **Задачи:** красиво оформить ревью кода.
- **Сочетается с:** `claude-skills/markdown-html-orchestrator`, `claude-skills/code-reviewer`

### `scientific/open-notebook`

Организация исследовательских источников через Open Notebook REST API.

- **Ключевые навыки:** импорт источников; поиск; заметки и cited chat
- **Задачи:** Настроить исследовательский блокнот и проверяемое получение материалов.
- **Сочетается с:** `scientific/paper-lookup`

### `scientific/pyzotero`

Программное управление библиографической библиотекой Zotero через pyzotero.

- **Ключевые навыки:** items/collections; теги; вложения и экспорт
- **Задачи:** Подготовить авторизованную автоматизацию ссылок и коллекций.
- **Сочетается с:** `scientific/citation-management`

---

<a id="cat-content"></a>
## Контент, тексты и бренд

**Область применения.** Статьи, посты, рассылки, голос бренда, публикации в соцсетях, редактура.

**Решаемые задачи.** Длинные тексты в заданном стиле; контент-планы; адаптация под платформы; профиль голоса бренда; кросспостинг; редактура и вычитка.

**Типовые связки.** brand-discovery → brand-voice → article-writing / content-engine → crosspost / social-publisher.

Навыков в категории: 17.

### `ecc/article-writing`

Статьи, гайды, посты, туториалы и рассылки в узнаваемом голосе на основе примеров или брендбука.

- **Ключевые навыки:** перенос стиля из образцов; структура длинного текста; достоверность и аргументация.
- **Задачи:** написать качественный длинный текст в едином голосе автора или бренда.
- **Сочетается с:** `ecc/brand-voice`, `ecc/content-engine`, `ecc/seo`

### `ecc/brand-discovery`

Многосессионное интервью об идентичности бренда по 8 модулям с итоговым брендбуком.

- **Ключевые навыки:** техники лэддеринга и «5 почему»; проективные вопросы; сохранение ответов между сессиями.
- **Задачи:** создать или переосмыслить бренд; подготовить бриф для дизайнеров и копирайтеров.
- **Сочетается с:** `ecc/brand-voice`, `ecc/article-writing`, `ecc/frontend-design-direction`

### `claude-skills/brand-guidelines`

Создание и применение брендбука — цвета, типографика, логотип, изображения, тон голоса.

- **Ключевые навыки:** правила бренда; проверка материалов на соответствие.
- **Задачи:** собрать брендбук или проверить макет по нему.
- **Сочетается с:** `ecc/brand-voice`, `ecc/brand-discovery`

### `ecc/brand-voice`

Профиль стиля письма на основе реальных текстов автора для повторного использования в контенте и переписке.

- **Ключевые навыки:** анализ образцов; профиль голоса; защита от шаблонного «ИИ-стиля».
- **Задачи:** писать тексты, неотличимые по стилю от автора.
- **Сочетается с:** `ecc/article-writing`, `ecc/content-engine`, `ecc/crosspost`

### `ecc/connections-optimizer`

Ревизия сети контактов в X и LinkedIn — чистка подписок, рекомендации и тёплые сообщения в вашем голосе.

- **Ключевые навыки:** анализ сети; рекомендации кого добавить; черновики сообщений.
- **Задачи:** перестроить соцсеть под текущие цели.
- **Сочетается с:** `ecc/social-graph-ranker`, `ecc/brand-voice`, `ecc/lead-intelligence`

### `claude-skills/content-creator`

Устаревший псевдоним — передаёт написание в content-production, а планирование в content-strategy.

- **Ключевые навыки:** перенаправление.
- **Задачи:** только для совместимости.
- **Сочетается с:** `claude-skills/content-production`, `claude-skills/content-strategy`

### `ecc/content-engine`

Системы контента под каждую платформу — X, LinkedIn, TikTok, YouTube, рассылки.

- **Ключевые навыки:** посты и треды; сценарии; контент-календари; переупаковка одного материала под разные платформы.
- **Задачи:** построить регулярный контент-поток; адаптировать материал под площадки.
- **Сочетается с:** `ecc/crosspost`, `ecc/brand-voice`, `ecc/social-publisher`

### `claude-skills/content-humanizer`

Делает черновик менее «ИИ-шным» — ритм, конкретика, личность, голос бренда.

- **Ключевые навыки:** устранение шаблонных оборотов; живой стиль.
- **Задачи:** когда текст звучит как написанный ИИ.
- **Сочетается с:** `claude-skills/copy-editing`, `ecc/brand-voice`

### `claude-skills/content-production`

Статья или гайд от начала до конца — исследование, план, черновик, SEO, проверки качества.

- **Ключевые навыки:** сквозной процесс производства контента.
- **Задачи:** написать пост для блога целиком.
- **Сочетается с:** `claude-skills/content-strategy`, `claude-skills/content-humanizer`, `ecc/seo`

### `claude-skills/copy-editing`

Редактура и вычитка маркетинговых текстов в несколько проходов.

- **Ключевые навыки:** ясность; голос; орфография; конкретика; читаемость; следы ИИ.
- **Задачи:** довести готовый текст до блеска.
- **Сочетается с:** `claude-skills/content-humanizer`, `marketing/copy-editing`

### `marketing/copy-editing`

Редактура, сокращение и вычитка существующего текста без переписывания с нуля.

- **Ключевые навыки:** решения по каждой строке — оставить, убрать, изменить.
- **Задачи:** улучшить уже написанный текст.
- **Сочетается с:** `marketing/copywriting`, `claude-skills/copy-editing`

### `ecc/crosspost`

Распространение контента по X, LinkedIn, Threads и Bluesky с адаптацией под каждую площадку.

- **Ключевые навыки:** адаптация формата; запрет одинаковых постов на разных площадках.
- **Задачи:** опубликовать материал сразу на нескольких платформах.
- **Сочетается с:** `ecc/content-engine`, `ecc/social-publisher`, `ecc/x-api`

### `claude-skills/linkedin-content`

Посты для LinkedIn — истории, how-to, карусели, сценарии видео, опросы.

- **Ключевые навыки:** хуки; формат; ревью черновика.
- **Задачи:** написать сильный пост для LinkedIn.
- **Сочетается с:** `claude-skills/linkedin-strategy`, `ecc/brand-voice`

### `claude-skills/social-content`

Посты для LinkedIn, X, Instagram, TikTok, Facebook с учётом формата площадки.

- **Ключевые навыки:** хуки; длина; формат.
- **Задачи:** написать пост для соцсети.
- **Сочетается с:** `marketing/social`, `ecc/content-engine`

### `ecc/social-publisher`

Планирование и публикация постов в 13 соцсетях через SocialClaw.

- **Ключевые навыки:** X, LinkedIn, Instagram, Facebook и другие; расписание публикаций.
- **Задачи:** автоматизировать публикации в соцсетях.
- **Сочетается с:** `ecc/content-engine`, `ecc/crosspost`

### `marketing/social`

Органический контент для LinkedIn, X, Instagram, TikTok, Facebook.

- **Ключевые навыки:** что публиковать; какой формат выбрать; с какой площадки начать.
- **Задачи:** вести соцсети бренда.
- **Сочетается с:** `claude-skills/social-content`, `ecc/content-engine`

### `ecc/x-api`

Интеграция с API X (Twitter).

- **Ключевые навыки:** публикация постов и тредов; чтение ленты; поиск; аналитика; OAuth; лимиты.
- **Задачи:** автоматизировать работу с X.
- **Сочетается с:** `ecc/crosspost`, `ecc/content-engine`

---

<a id="cat-marketing"></a>
## Маркетинг, SEO и рост

**Область применения.** SEO и AEO, копирайтинг, конверсия (CRO), реклама, email-маркетинг, запуски, аналитика маркетинга, growth.

**Решаемые задачи.** SEO-аудит и стратегия; тексты лендингов; оптимизация конверсии страниц и форм; рекламные кампании; email-цепочки; ценообразование; запуск продукта; конкурентный анализ.

**Типовые связки.** product-marketing-context (база знаний о продукте) → стратегия (content-strategy, launch-strategy) → тексты (copywriting) → CRO (page-cro) → аналитика (analytics-tracking) → A/B-тесты.

Навыков в категории: 90.

### `claude-skills/ab-test-setup`

Планирование и запуск A/B, сплит- и мультивариантных тестов с расчётом выборки.

- **Ключевые навыки:** расчёт размера выборки; гипотезы; статистическая значимость результата.
- **Задачи:** спланировать эксперимент; понять, значим ли результат.
- **Сочетается с:** `claude-skills/analytics-tracking`, `claude-skills/copywriting`, `marketing/ab-testing`

### `marketing/ab-testing`

Планирование, запуск и чтение A/B-тестов с ответами на спорные вопросы.

- **Ключевые навыки:** реален ли результат; можно ли остановить тест; какая версия победила; стоит ли тестировать.
- **Задачи:** провести эксперимент и правильно его интерпретировать.
- **Сочетается с:** `marketing/cro`, `claude-skills/statistical-analyst`

### `pm-skills/acquisition-channel-advisor`

Оценка каналов привлечения по юнит-экономике, качеству клиентов и масштабируемости.

- **Ключевые навыки:** масштабировать, тестировать или закрыть канал.
- **Задачи:** решить судьбу канала роста.
- **Сочетается с:** `marketing/attribution`, `pm-skills/saas-economics-efficiency-metrics`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/ad-creative`

Тексты рекламы для Google RSA, Meta, LinkedIn и TikTok с проверкой лимитов площадок.

- **Ключевые навыки:** заголовки и описания под ограничения символов; массовые вариации.
- **Задачи:** написать рекламные объявления для кампании.
- **Сочетается с:** `claude-skills/copywriting`, `claude-skills/campaign-analytics`, `marketing/ad-creative`

### `marketing/ad-creative`

Написание и оценка рекламных креативов — заголовки, основной текст, вариации для Google, Meta, LinkedIn.

- **Ключевые навыки:** выбор хуков и углов; какие объявления запускать или отключать.
- **Задачи:** сделать рекламу, которая работает.
- **Сочетается с:** `marketing/ads`, `claude-skills/ad-creative`

### `marketing/ads`

Планирование, запуск и исправление платной рекламы в Google, Meta и LinkedIn.

- **Ключевые навыки:** стоит ли реклама денег; выбор канала; структура и бюджет кампаний.
- **Задачи:** запустить или починить рекламу.
- **Сочетается с:** `marketing/ad-creative`, `marketing/conversion-tracking`, `claude-skills/paid-ads`

### `claude-skills/aeo`

Оптимизация контента под цитирование в ChatGPT, Perplexity, Claude и Gemini (AEO).

- **Ключевые навыки:** оценка E-E-A-T; структура ответов; переписывание под ответные движки.
- **Задачи:** добиться, чтобы ИИ-ассистенты ссылались на ваш контент.
- **Сочетается с:** `ecc/seo`, `claude-skills/content-production`, `marketing/ai-seo`

### `claude-skills/ai-decision-authority`

Политика самостоятельности ИИ в маркетинге — где агент может действовать без проверки человеком.

- **Ключевые навыки:** классификация процессов по уровню автономии ИИ; правила ревью.
- **Задачи:** решить, что можно доверить ИИ в маркетинге.
- **Сочетается с:** `claude-skills/marketing-ops`, `ecc/operator-approval-loop`

### `marketing/ai-seo`

Попадание в ответы ИИ — ChatGPT, Perplexity, AI Overviews.

- **Ключевые навыки:** почему ИИ цитирует конкурента; какой контент рекомендуется; оптимизация под ответы.
- **Задачи:** стать источником для ИИ-ассистентов.
- **Сочетается с:** `claude-skills/aeo`, `marketing/seo-audit`, `marketing/schema`

### `claude-skills/analytics-tracking`

Настройка, аудит и отладка GA4, Google Tag Manager и отслеживания конверсий.

- **Ключевые навыки:** план событий; теги; поиск сломанных событий.
- **Задачи:** настроить аналитику сайта правильно.
- **Сочетается с:** `claude-skills/campaign-analytics`, `claude-skills/ab-test-setup`, `marketing/analytics`

### `marketing/analytics`

Настройка и аудит аналитики, правильность расчёта метрик, план отслеживания и имена событий.

- **Ключевые навыки:** план трекинга; проверка метрик; соглашения по событиям.
- **Задачи:** доверять цифрам в аналитике.
- **Сочетается с:** `marketing/conversion-tracking`, `marketing/attribution`

### `claude-skills/app-store-optimization`

Оптимизация страниц приложения в App Store и Google Play (ASO).

- **Ключевые навыки:** оценка листинга; ключевые слова; рейтинги; работа с отзывами.
- **Задачи:** поднять приложение в поиске магазинов.
- **Сочетается с:** `claude-skills/copywriting`

### `marketing/aso`

Аудит и оптимизация страницы в App Store или Google Play.

- **Ключевые навыки:** название, ключевые слова, скриншоты; причины падения загрузок.
- **Задачи:** увеличить установки приложения.
- **Сочетается с:** `claude-skills/app-store-optimization`

### `marketing/attribution`

Какой маркетинг на самом деле приносит выручку.

- **Ключевые навыки:** модели атрибуции; каким цифрам доверять; распределение заслуг между каналами.
- **Задачи:** понять, какой канал реально работает.
- **Сочетается с:** `marketing/analytics`, `claude-skills/campaign-analytics`

### `claude-skills/business-name-fit`

Проверка названия компании, бренда или продукта, в том числе для зарубежных рынков.

- **Ключевые навыки:** культурные ассоциации; произношение; риски названия.
- **Задачи:** выбрать название до регистрации.
- **Сочетается с:** `claude-skills/brand-guidelines`, `ecc/brand-discovery`

### `claude-skills/campaign-analytics`

Анализ эффективности кампаний на ваших цифрах.

- **Ключевые навыки:** ROAS, CPA, ROI; мультиканальная атрибуция; провалы воронки.
- **Задачи:** понять, какой канал работает лучше.
- **Сочетается с:** `claude-skills/analytics-tracking`, `claude-skills/paid-ads`

### `claude-skills/cmo-advisor`

Советник по руководству маркетингом.

- **Ключевые навыки:** позиционирование; product-led, sales-led или community-led рост; распределение бюджета; команда маркетинга.
- **Задачи:** выстроить маркетинговую стратегию.
- **Сочетается с:** `claude-skills/cmo-review`, `claude-skills/marketing-strategy-pmm`

### `claude-skills/cmo-review`

Критика позиционирования, ICP, сообщений или микса каналов перед запуском.

- **Ключевые навыки:** позиция директора по маркетингу.
- **Задачи:** проверить маркетинговый план до запуска.
- **Сочетается с:** `claude-skills/cmo-advisor`

### `marketing/co-marketing`

Совместный маркетинг с партнёрами.

- **Ключевые навыки:** подходит ли партнёр; разница в размерах; разделение работы и лидов.
- **Задачи:** провести совместную кампанию.
- **Сочетается с:** `claude-skills/partnerships-architect`, `marketing/events`

### `marketing/community-marketing`

Создание и рост онлайн-сообщества.

- **Ключевые навыки:** стоит ли оно того; где размещать (Discord, Slack и др.); почему участники молчат.
- **Задачи:** построить живое сообщество вокруг продукта.
- **Сочетается с:** `marketing/social`, `marketing/events`

### `claude-skills/competitor-alternatives`

Страницы сравнения «X vs Y» и «альтернатива продукту».

- **Ключевые навыки:** матрица сравнения; структура страницы.
- **Задачи:** сделать SEO-страницу сравнения с конкурентом.
- **Сочетается с:** `marketing/competitors`, `ecc/seo`

### `marketing/competitors`

Страницы сравнения и альтернатив — «X vs Y», «альтернатива X», «лучшие альтернативы X».

- **Ключевые навыки:** что допустимо писать о конкуренте публично; структура страницы.
- **Задачи:** создать или проверить страницы сравнения.
- **Сочетается с:** `marketing/competitor-profiling`, `claude-skills/competitor-alternatives`

### `claude-skills/content-strategy`

Решение, какой контент создавать — темы, кластеры, контент-план.

- **Ключевые навыки:** карта тематических кластеров; приоритизация тем.
- **Задачи:** составить контент-план блога.
- **Сочетается с:** `marketing/content-strategy`, `claude-skills/content-production`

### `marketing/content-strategy`

Планирование контента — какие темы приоритетны, тематические кластеры.

- **Ключевые навыки:** о чём писать; почему посты не приводят клиентов.
- **Задачи:** составить контент-стратегию.
- **Сочетается с:** `claude-skills/content-strategy`, `marketing/seo-audit`

### `marketing/conversion-tracking`

Отслеживание конверсий в Google Ads, Meta, GA4, LinkedIn, TikTok.

- **Ключевые навыки:** настройка; аудит; почему конверсии пропадают или задваиваются.
- **Задачи:** наладить передачу конверсий в рекламные системы.
- **Сочетается с:** `marketing/analytics`, `marketing/ads`

### `claude-skills/copywriting`

Заголовки, слоганы, CTA, тексты лендингов, страниц цен и «о нас».

- **Ключевые навыки:** оценка вариантов заголовков; структура продающего текста.
- **Задачи:** написать конвертирующий текст для сайта.
- **Сочетается с:** `marketing/copywriting`, `claude-skills/copy-editing`, `claude-skills/ab-test-setup`

### `marketing/copywriting`

Тексты страниц — главная, лендинг, цены, фичи.

- **Ключевые навыки:** выбор заголовка, обещания и главного сообщения; диагностика.
- **Задачи:** написать или переписать текст страницы.
- **Сочетается с:** `marketing/product-marketing`, `marketing/cro`, `claude-skills/copywriting`

### `marketing/cro`

Больше конверсий со страницы или формы.

- **Ключевые навыки:** почему страница не конвертирует; что менять первым; добавлять ли поля.
- **Задачи:** поднять конверсию.
- **Сочетается с:** `marketing/copywriting`, `marketing/ab-testing`, `claude-skills/page-cro`

### `marketing/directory-submissions`

Размещение продукта в каталогах стартапов, SaaS, ИИ, MCP и отзовиков.

- **Ключевые навыки:** какие каталоги стоят усилий; работают ли размещения.
- **Задачи:** получить трафик и ссылки из каталогов.
- **Сочетается с:** `marketing/link-building`, `marketing/launch`

### `claude-skills/email-sequence`

Цепочки писем для подписчиков — приветственные, прогревающие, онбординг, реактивация.

- **Ключевые навыки:** тайминг; триггеры; содержание писем.
- **Задачи:** настроить автоматическую email-рассылку.
- **Сочетается с:** `marketing/emails`, `claude-skills/copywriting`

### `marketing/emails`

Автоматические email-цепочки — приветствие, онбординг и другие.

- **Ключевые навыки:** что отправлять и когда; работает ли цепочка.
- **Задачи:** создать или улучшить email-автоматизацию.
- **Сочетается с:** `claude-skills/email-sequence`, `marketing/onboarding`

### `marketing/events`

Планирование, проведение, спонсорство и выступления на событиях — вебинары, конференции, стенды, митапы.

- **Ключевые навыки:** окупаемость события; подготовка и фоллоу-ап.
- **Задачи:** решить, участвовать ли в событии, и получить результат.
- **Сочетается с:** `claude-skills/webinar-marketing`, `marketing/co-marketing`

### `claude-skills/form-cro`

Оптимизация форм заявки, контакта, демо и оформления заказа.

- **Ключевые навыки:** оценка трения полей; сокращение полей; тексты формы.
- **Задачи:** повысить конверсию формы.
- **Сочетается с:** `claude-skills/page-cro`, `marketing/cro`

### `claude-skills/free-tool-strategy`

Бесплатный инструмент как маркетинговый актив — калькулятор, грейдер, генератор.

- **Ключевые навыки:** оценка трафика, лидов и затрат.
- **Задачи:** решить, стоит ли делать бесплатный инструмент.
- **Сочетается с:** `marketing/free-tools`, `claude-skills/programmatic-seo`

### `marketing/free-tools`

Бесплатные инструменты как маркетинг — калькуляторы, грейдеры, генераторы.

- **Ключевые навыки:** стоит ли строить; какую идею выбрать.
- **Задачи:** привлекать трафик и лиды полезным инструментом.
- **Сочетается с:** `claude-skills/free-tool-strategy`, `marketing/lead-magnets`

### `marketing/influencer-marketing`

Партнёрства с креаторами, инфлюенсерами и амбассадорами.

- **Ключевые навыки:** подбор креаторов; оплата; права на контент; окупаемость интеграции.
- **Задачи:** запустить работу с блогерами.
- **Сочетается с:** `marketing/social`, `marketing/referrals`

### `claude-skills/launch-strategy`

План запуска продукта или фичи — оценка готовности и поэтапный план по каналам.

- **Ключевые навыки:** Product Hunt; поэтапный запуск; каналы.
- **Задачи:** спланировать запуск.
- **Сочетается с:** `marketing/launch`, `pm-setup/launch-checklist`

### `marketing/launch`

Запуск продукта или фичи.

- **Ключевые навыки:** готов ли продукт; когда объявлять; Product Hunt; бета и ранний доступ.
- **Задачи:** спланировать громкий запуск.
- **Сочетается с:** `claude-skills/launch-strategy`, `pm-setup/launch-checklist`

### `marketing/lead-magnets`

Лид-магниты — что отдавать за email и сколько спрашивать.

- **Ключевые навыки:** чек-листы, гайды, шаблоны; закрытие контента; поля формы.
- **Задачи:** собирать контакты потенциальных клиентов.
- **Сочетается с:** `marketing/emails`, `marketing/free-tools`

### `marketing/link-building`

Обратные ссылки и упоминания для роста позиций и цитирований ИИ.

- **Ключевые навыки:** безопасные тактики; как получить ссылки.
- **Задачи:** нарастить ссылочный профиль.
- **Сочетается с:** `marketing/directory-submissions`, `marketing/public-relations`

### `claude-skills/linkedin-analytics`

Анализ эффективности постов в LinkedIn.

- **Ключевые навыки:** почему упал охват; какие посты сработали; проверка гипотез.
- **Задачи:** понять, что работает в вашем LinkedIn.
- **Сочетается с:** `claude-skills/linkedin-content`, `claude-skills/linkedin-strategy`

### `claude-skills/linkedin-skills`

Маршрутизатор органического роста в LinkedIn с проверкой по правилам площадки.

- **Ключевые навыки:** стратегия, профиль, посты, ритм, аутрич, аналитика.
- **Задачи:** понять, какой LinkedIn-навык нужен.
- **Сочетается с:** `claude-skills/linkedin-strategy`, `claude-skills/linkedin-content`

### `claude-skills/linkedin-strategy`

План присутствия в LinkedIn — контентные столпы, позиционирование, ритм, рассылка.

- **Ключевые навыки:** стратегия личного бренда.
- **Задачи:** выстроить системное ведение LinkedIn.
- **Сочетается с:** `claude-skills/linkedin-content`, `claude-skills/linkedin-analytics`

### `claude-skills/local-seo-manager`

Локальное SEO — Google Business Profile, карты, страницы зон обслуживания, ответы на отзывы.

- **Ключевые навыки:** ранжирование на картах; каталоги; репутация.
- **Задачи:** привлекать клиентов из локального поиска.
- **Сочетается с:** `claude-skills/seo-audit`, `ecc/seo`

### `ecc/marketing-campaign`

Планирование и запуск маркетинговой кампании от начала до конца.

- **Ключевые навыки:** исследование аудитории; позиционирование; угол кампании; тексты лендинга; email-цепочки; посты.
- **Задачи:** провести кампанию под запуск или акцию.
- **Сочетается с:** `ecc/content-engine`, `ecc/brand-voice`, `ecc/seo`

### `claude-skills/marketing-context`

Общий маркетинговый контекст — ICP, позиционирование, голос бренда — до других маркетинговых навыков.

- **Ключевые навыки:** документ контекста продукта.
- **Задачи:** начать любой маркетинговый проект с общей основы.
- **Сочетается с:** `marketing/product-marketing`, `claude-skills/marketing-ops`

### `marketing/marketing-council`

Симуляция совета известных маркетологов (Сет Годин и др.) для решения.

- **Ключевые навыки:** несколько экспертных взглядов на вопрос.
- **Задачи:** получить разные точки зрения на маркетинговое решение.
- **Сочетается с:** `ecc/council`, `marketing/marketing-plan`

### `claude-skills/marketing-demand-acquisition`

Генерация спроса и платное привлечение в Google, LinkedIn, Meta, маркетинговый бюджет.

- **Ключевые навыки:** распределение бюджета; сравнение каналов.
- **Задачи:** спланировать привлечение клиентов.
- **Сочетается с:** `claude-skills/paid-ads`, `claude-skills/campaign-analytics`

### `claude-skills/marketing-ideas`

Идеи для маркетинга SaaS из 139 тактик по стадии, бюджету и каналу.

- **Ключевые навыки:** подбор тактик под ситуацию.
- **Задачи:** найти новые способы роста.
- **Сочетается с:** `marketing/marketing-ideas`, `claude-skills/marketing-ops`

### `marketing/marketing-ideas`

Идеи и тактики роста для софтверного продукта.

- **Ключевые навыки:** что попробовать с малым бюджетом; как получить первых клиентов.
- **Задачи:** найти новые способы привлечения.
- **Сочетается с:** `claude-skills/marketing-ideas`, `marketing/marketing-plan`

### `marketing/marketing-loops`

Регулярные маркетинговые задачи, которые ИИ-агент выполняет по расписанию или триггеру.

- **Ключевые навыки:** еженедельные и ежедневные автоматические проверки и действия.
- **Задачи:** автоматизировать маркетинговую рутину.
- **Сочетается с:** `claude-skills/ai-decision-authority`, `ecc/continuous-agent-loop`

### `claude-skills/marketing-ops`

Маршрутизатор сложных маркетинговых задач на несколько навыков.

- **Ключевые навыки:** кампании через контент, SEO, CRO и каналы.
- **Задачи:** скоординировать многоканальную кампанию.
- **Сочетается с:** `claude-skills/marketing-skills`, `claude-skills/marketing-context`

### `marketing/marketing-plan`

Полный маркетинговый или GTM-план для клиента, компании или своего продукта.

- **Ключевые навыки:** последовательность и приоритеты маркетинговой работы.
- **Задачи:** составить маркетинговый план.
- **Сочетается с:** `marketing/product-marketing`, `claude-skills/marketing-strategy-pmm`

### `claude-skills/marketing-psychology`

Этичное применение психологии убеждения к странице, предложению или кампании (70+ моделей).

- **Ключевые навыки:** поведенческая экономика; ментальные модели.
- **Задачи:** понять, почему люди не покупают, и что изменить.
- **Сочетается с:** `marketing/marketing-psychology`, `claude-skills/copywriting`

### `marketing/marketing-psychology`

Психология в маркетинге — почему покупатели ведут себя так, как ведут.

- **Ключевые навыки:** ментальные модели; честность тактик убеждения.
- **Задачи:** применить психологию этично.
- **Сочетается с:** `claude-skills/marketing-psychology`, `marketing/offers`

### `claude-skills/marketing-skills`

Каталог 44 маркетинговых навыков с маршрутизацией.

- **Ключевые навыки:** список навыков по группам.
- **Задачи:** найти нужный маркетинговый навык.
- **Сочетается с:** `claude-skills/marketing-ops`

### `claude-skills/marketing-strategy-pmm`

Продуктовое позиционирование, ICP, battlecards и план выхода на рынок по методу Эйприл Данфорд.

- **Ключевые навыки:** позиционирование; конкурентные карточки; GTM.
- **Задачи:** сформулировать позиционирование продукта.
- **Сочетается с:** `pm-skills/positioning-statement`, `claude-skills/competitive-intel`

### `marketing/offers`

Проектирование самого предложения — набор ценности, бонусы, гарантии, честная срочность.

- **Ключевые навыки:** почему предложение не продаётся.
- **Задачи:** сделать оффер неотразимым.
- **Сочетается с:** `marketing/pricing`, `marketing/copywriting`

### `claude-skills/onboarding-cro`

Активация пользователя и первый опыт после регистрации.

- **Ключевые навыки:** поиск провала активации; time-to-value.
- **Задачи:** улучшить онбординг продукта.
- **Сочетается с:** `marketing/onboarding`, `claude-skills/signup-flow-cro`

### `claude-skills/page-cro`

Аудит неконвертирующей страницы по секциям с ранжированием исправлений.

- **Ключевые навыки:** главная, лендинг, цены, фичи.
- **Задачи:** поднять конверсию страницы.
- **Сочетается с:** `marketing/cro`, `claude-skills/copywriting`

### `claude-skills/paid-ads`

Стратегия платной рекламы в Google, Meta, LinkedIn, X.

- **Ключевые навыки:** структура; таргетинг; ставки; ретаргетинг; бюджеты.
- **Задачи:** настроить рекламные кампании.
- **Сочетается с:** `marketing/ads`, `claude-skills/ad-creative`

### `claude-skills/paywall-upgrade-cro`

Пейволы, окна апгрейда, ограничения функций и экраны окончания триала.

- **Ключевые навыки:** паттерны момента апгрейда; тексты и дизайн.
- **Задачи:** повысить конверсию в платный план.
- **Сочетается с:** `marketing/paywalls`, `claude-skills/pricing-strategy`

### `marketing/paywalls`

Пейволы и моменты апгрейда в приложении.

- **Ключевые навыки:** когда и насколько настойчиво просить оплату.
- **Задачи:** конвертировать бесплатных пользователей в платных.
- **Сочетается с:** `claude-skills/paywall-upgrade-cro`, `marketing/pricing`

### `claude-skills/popup-cro`

Попапы, модальные окна, exit-intent, слайдеры и баннеры для конверсии.

- **Ключевые навыки:** триггеры; частота показа; оффер; текст.
- **Задачи:** сделать попап, который конвертирует и не раздражает.
- **Сочетается с:** `marketing/popups`, `claude-skills/page-cro`

### `marketing/popups`

Попапы, модальные окна, слайд-ины, липкие плашки и баннеры.

- **Ключевые навыки:** поможет или раздражает; когда показывать.
- **Задачи:** сделать полезный попап.
- **Сочетается с:** `claude-skills/popup-cro`, `marketing/lead-magnets`

### `pm-skills/positioning-statement`

Позиционирование в стиле Джеффри Мура.

- **Ключевые навыки:** для кого; какая проблема; категория; отличие.
- **Задачи:** сформулировать позиционирование.
- **Сочетается с:** `pm-skills/positioning-workshop`, `marketing/product-marketing`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/positioning-workshop`

Воркшоп по позиционированию.

- **Ключевые навыки:** целевой клиент; потребность; категория; выгоды; отличия.
- **Задачи:** когда сообщения о продукте звучат плоско.
- **Сочетается с:** `pm-skills/positioning-statement`, `claude-skills/marketing-strategy-pmm`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/pricing-strategy`

Тарифы SaaS — метрика ценности, упаковка, страница цен, повышение цен.

- **Ключевые навыки:** моделирование выручки по тарифам.
- **Задачи:** спроектировать тарифную сетку.
- **Сочетается с:** `marketing/pricing`, `claude-skills/pricing-strategist`

### `marketing/pricing`

Цены и упаковка — тарифы, метрика ценности.

- **Ключевые навыки:** сколько брать; поднимать ли цены; как перевести текущих клиентов.
- **Задачи:** выстроить ценообразование.
- **Сочетается с:** `claude-skills/pricing-strategy`, `pm-skills/finance-based-pricing-advisor`

### `marketing/product-marketing`

Документ продуктового маркетингового контекста — основа для всех маркетинговых навыков.

- **Ключевые навыки:** позиционирование, ICP, сообщения в одном файле.
- **Задачи:** создать или обновить общий маркетинговый контекст.
- **Сочетается с:** `claude-skills/marketing-context`, `pm-skills/positioning-statement`

### `claude-skills/programmatic-seo`

Массовое создание SEO-страниц по шаблону и данным — локации, интеграции, сравнения, каталоги.

- **Ключевые навыки:** шаблоны; качество данных; защита от тонкого контента.
- **Задачи:** масштабировать органический трафик.
- **Сочетается с:** `marketing/programmatic-seo`, `claude-skills/site-architecture`

### `marketing/programmatic-seo`

SEO-страницы в масштабе по шаблонам и данным.

- **Ключевые навыки:** будет ли набор страниц ранжироваться или выглядеть «тонким».
- **Задачи:** создать сотни полезных страниц.
- **Сочетается с:** `claude-skills/programmatic-seo`, `marketing/site-architecture`

### `claude-skills/prompt-engineer-toolkit`

Тестирование, версионирование и контроль маркетинговых промптов.

- **Ключевые навыки:** A/B-тесты промптов на кейсах; управление версиями.
- **Задачи:** навести порядок в промптах маркетинговой команды.
- **Сочетается с:** `claude-skills/prompt-governance`

### `marketing/public-relations`

Пресса и медиа — питчи, пресс-релизы, кризисы.

- **Ключевые навыки:** что говорить журналисту; есть ли новость; работа в кризисе.
- **Задачи:** получить публикации в СМИ.
- **Сочетается с:** `pm-skills/press-release`, `marketing/link-building`

### `claude-skills/referral-program`

Реферальные, партнёрские и амбассадорские программы.

- **Ключевые навыки:** модель выплат и ROI; механика.
- **Задачи:** запустить или починить реферальную программу.
- **Сочетается с:** `marketing/referrals`

### `marketing/referrals`

Реферальные и партнёрские программы, сарафанное радио.

- **Ключевые навыки:** что вознаграждать; сколько платить; с какой петли начать.
- **Задачи:** запустить рост через рекомендации.
- **Сочетается с:** `claude-skills/referral-program`, `marketing/influencer-marketing`

### `claude-skills/schema-markup`

Структурированные данные JSON-LD и schema.org для расширенных сниппетов.

- **Ключевые навыки:** валидация разметки.
- **Задачи:** получить расширенные результаты в поиске.
- **Сочетается с:** `marketing/schema`, `ecc/seo`

### `marketing/schema`

Разметка schema.org (JSON-LD) — добавление, исправление, проверка.

- **Ключевые навыки:** выбор типа; допустимость разметки.
- **Задачи:** получить расширенные сниппеты.
- **Сочетается с:** `claude-skills/schema-markup`, `marketing/seo-audit`

### `claude-skills/seo-audit`

Почему сайт не ранжируется — техническое SEO, on-page, мета-теги, здоровье сайта.

- **Ключевые навыки:** аудит сайта; приоритеты исправлений.
- **Задачи:** найти причины слабых позиций в Google.
- **Сочетается с:** `marketing/seo-audit`, `ecc/seo`

### `marketing/seo-audit`

Аудит и диагностика SEO.

- **Ключевые навыки:** почему упал трафик; почему страница не ранжируется; canonical, hreflang, редиректы.
- **Задачи:** найти и исправить SEO-проблемы.
- **Сочетается с:** `claude-skills/seo-audit`, `marketing/site-architecture`

### `ecc/seo`

Аудит, план и внедрение SEO.

- **Ключевые навыки:** техническое SEO; on-page; структурированные данные; Core Web Vitals; контент-стратегия.
- **Задачи:** улучшить видимость сайта в поиске.
- **Сочетается с:** `ecc/article-writing`, `ecc/benchmark`, `ecc/marketing-campaign`

### `claude-skills/signup-flow-cro`

Конверсия регистрации и старта триала.

- **Ключевые навыки:** поиск шага с наибольшим отвалом; упрощение формы.
- **Задачи:** увеличить число регистраций.
- **Сочетается с:** `marketing/signup`, `claude-skills/onboarding-cro`

### `marketing/signup`

Регистрация и старт триала.

- **Ключевые навыки:** какие поля и шаги убрать; требовать ли карту; SSO.
- **Задачи:** повысить число регистраций.
- **Сочетается с:** `claude-skills/signup-flow-cro`, `marketing/onboarding`

### `claude-skills/site-architecture`

Структура URL, навигация, перелинковка, хабы и «сиротские» страницы.

- **Ключевые навыки:** анализ sitemap; структурное SEO.
- **Задачи:** исправить структурные SEO-проблемы.
- **Сочетается с:** `marketing/site-architecture`, `claude-skills/seo-audit`

### `marketing/site-architecture`

Планирование и реструктуризация сайта.

- **Ключевые навыки:** иерархия; навигация; URL; какие страницы нужны.
- **Задачи:** спроектировать структуру сайта.
- **Сочетается с:** `claude-skills/site-architecture`, `marketing/seo-audit`

### `marketing/sms`

SMS, MMS и WhatsApp-маркетинг.

- **Ключевые навыки:** брошенная корзина, возврат клиентов, промо; что разрешено законом.
- **Задачи:** решить, стоит ли SMS-канал, и запустить его.
- **Сочетается с:** `marketing/emails`

### `claude-skills/social-media-analyzer`

Эффективность соцсетей — вовлечённость, охват, ROI, бенчмарки.

- **Ключевые навыки:** сравнение платформ.
- **Задачи:** понять, какая соцсеть работает лучше.
- **Сочетается с:** `claude-skills/social-media-manager`

### `claude-skills/social-media-manager`

Стратегия соцсетей, контент-календарь, работа с сообществом, рост подписчиков.

- **Ключевые навыки:** что и когда публиковать.
- **Задачи:** системно вести соцсети.
- **Сочетается с:** `claude-skills/social-content`, `claude-skills/social-media-analyzer`

### `claude-skills/webinar-marketing`

Вебинары и онлайн-события — регистрации, явка, фоллоу-ап, конверсия.

- **Ключевые навыки:** оценка этапов воронки.
- **Задачи:** провести вебинар с результатом.
- **Сочетается с:** `marketing/events`

### `claude-skills/x-twitter-growth`

Рост в X/Twitter — твиты, треды, аудит профиля, конкуренты, план публикаций.

- **Ключевые навыки:** аудит профиля; черновики.
- **Задачи:** расти в X.
- **Сочетается с:** `ecc/x-api`, `claude-skills/social-content`

---

<a id="cat-sales"></a>
## Продажи, клиенты и поддержка

**Область применения.** Продажи B2B, лидогенерация, работа с клиентами, customer success, биллинг клиентов, партнёрства.

**Решаемые задачи.** Поиск и квалификация лидов; холодные письма; подготовка к сделкам; удержание клиентов и снижение оттока; клиентская поддержка.

**Типовые связки.** lead-intelligence / поиск лидов → cold-email → sales-материалы → customer-success / churn-prevention.

Навыков в категории: 26.

### `pm-skills/battle-card-builder`

Конкурентная карточка для продавца на основе публичных данных с источниками.

- **Ключевые навыки:** проверяемые утверждения; полевые действия.
- **Задачи:** дать продажам оружие против конкурента.
- **Сочетается с:** `marketing/sales-enablement`, `pm-skills/competitive-research-snapshot`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/business-growth-skills`

Маршрутизатор задач роста между customer success, пресейлом, revenue operations и подготовкой договоров.

- **Ключевые навыки:** выбор подходящего навыка роста.
- **Задачи:** понять, какой навык роста бизнеса использовать.
- **Сочетается с:** `claude-skills/customer-success-manager`, `claude-skills/contract-and-proposal-writer`

### `claude-skills/channel-economics`

Сравнение прямых и партнёрских каналов продаж.

- **Ключевые навыки:** полная стоимость обслуживания; ROI канала; оптимальный микс.
- **Задачи:** решить, куда направлять продажи.
- **Сочетается с:** `claude-skills/commercial-forecaster`, `claude-skills/partnerships-architect`

### `claude-skills/chief-customer-officer-advisor`

Советник по стратегии удержания, сегментации и размеру команды customer success.

- **Ключевые навыки:** GRR и NRR; причины оттока; модели работы CSM.
- **Задачи:** выстроить стратегию удержания клиентов.
- **Сочетается с:** `claude-skills/customer-success-manager`, `claude-skills/cco-review`

### `claude-skills/churn-prevention`

Снижение оттока — сценарии отмены подписки, предложения удержания, опросы при уходе, письма о неудачной оплате.

- **Ключевые навыки:** оценка выручки под риском; save offers; dunning.
- **Задачи:** уменьшить отток клиентов.
- **Сочетается с:** `claude-skills/customer-success-manager`, `marketing/churn-prevention`

### `marketing/churn-prevention`

Снижение оттока — сценарии отмены, опросы при уходе, предложения удержания.

- **Ключевые навыки:** почему клиенты уходят; давать ли скидку или паузу.
- **Задачи:** удержать уходящих клиентов.
- **Сочетается с:** `claude-skills/churn-prevention`, `marketing/onboarding`

### `claude-skills/cold-email`

Холодные письма и цепочки фоллоу-апов для потенциальных клиентов.

- **Ключевые навыки:** оценка длины, персонализации и CTA; последовательности писем.
- **Задачи:** написать холодную рассылку, которая получает ответы.
- **Сочетается с:** `marketing/cold-email`, `ecc/lead-intelligence`, `claude-skills/copywriting`

### `marketing/cold-email`

Холодный B2B-аутрич — повод для письма, первые строки, цепочки.

- **Ключевые навыки:** почему никто не отвечает; что работает в холодных письмах.
- **Задачи:** написать и запустить холодную рассылку.
- **Сочетается с:** `marketing/prospecting`, `claude-skills/cold-email`

### `claude-skills/commercial-policy`

Правила скидок — матрица скидок, пороги одобрения, исключения.

- **Ключевые навыки:** дисциплина сделок; рамки для отдела продаж.
- **Задачи:** формализовать политику скидок.
- **Сочетается с:** `claude-skills/deal-desk`, `claude-skills/pricing-strategy`

### `claude-skills/commercial-skills`

Маршрутизатор коммерческих задач — цены, сделки, скидки, партнёры, каналы, тендеры, прогнозы.

- **Ключевые навыки:** выбор подходящего коммерческого навыка.
- **Задачи:** понять, какой навык нужен для коммерческого вопроса.
- **Сочетается с:** `claude-skills/deal-desk`, `claude-skills/commercial-policy`

### `claude-skills/contract-and-proposal-writer`

Договоры для фриланса, коммерческие предложения, SOW, NDA и MSA для США, ЕС, Великобритании и DACH.

- **Ключевые навыки:** структурированный markdown; конвертация в docx.
- **Задачи:** подготовить договор или КП.
- **Сочетается с:** `claude-skills/commercial-policy`, `ecc/master-agreement-generator`

### `claude-skills/cro-advisor`

Советник по B2B-выручке — прогнозы, квоты, модель продаж, NRR, отток, цены, мощность отдела.

- **Ключевые навыки:** модель прогноза выручки; планирование квот.
- **Задачи:** выстроить систему продаж.
- **Сочетается с:** `claude-skills/cro-review`, `claude-skills/commercial-forecaster`

### `claude-skills/cro-review`

Критика прогноза, падения конверсии или найма продавцов.

- **Ключевые навыки:** позиция директора по выручке.
- **Задачи:** проверить план продаж.
- **Сочетается с:** `claude-skills/cro-advisor`

### `claude-skills/customer-success-manager`

Оценка клиентских аккаунтов — здоровье, риск оттока, потенциал расширения.

- **Ключевые навыки:** health score; анализ риска оттока; возможности допродаж.
- **Задачи:** найти клиентов в зоне риска и под расширение.
- **Сочетается с:** `claude-skills/churn-prevention`, `claude-skills/chief-customer-officer-advisor`

### `claude-skills/deal-desk`

Проверка сделки со скидкой сверх полномочий, правками договора или неясной экономикой.

- **Ключевые навыки:** скоринг сделки; экономика сделки; одобрения.
- **Задачи:** решить, закрывать ли сделку на таких условиях.
- **Сочетается с:** `claude-skills/commercial-policy`, `claude-skills/cro-advisor`

### `ecc/lead-intelligence`

ИИ-конвейер разведки и аутрича по лидам вместо Apollo, Clay и ZoomInfo.

- **Ключевые навыки:** скоринг сигналов; поиск тёплых путей; обогащение данных; персонализированные сообщения.
- **Задачи:** найти и приоритизировать потенциальных клиентов или партнёров.
- **Сочетается с:** `ecc/exa-search`, `ecc/connections-optimizer`, `ecc/email-ops`

### `claude-skills/linkedin-engagement`

Комментарии, запросы на связь, личные сообщения и аутрич в LinkedIn.

- **Ключевые навыки:** выбор целей для комментариев; безопасные объёмы аутрича.
- **Задачи:** расширять сеть и находить клиентов в LinkedIn.
- **Сочетается с:** `claude-skills/linkedin-profile`, `ecc/connections-optimizer`

### `claude-skills/partnerships-architect`

Решение о партнёрстве — уровень (реферал, реселлер, OEM, интегратор, альянс), совместный GTM, разделение выручки.

- **Ключевые навыки:** оценка партнёров; модели партнёрства.
- **Задачи:** выстроить партнёрскую программу.
- **Сочетается с:** `claude-skills/channel-economics`, `marketing/co-marketing`

### `claude-skills/pricing-strategist`

Выбор модели цен — за место, по использованию, по ценности, freemium, гибрид.

- **Ключевые навыки:** анализ Van Westendorp; тарифы Good/Better/Best.
- **Задачи:** определить ценообразование продукта.
- **Сочетается с:** `claude-skills/pricing-strategy`, `pm-skills/finance-based-pricing-advisor`

### `marketing/prospecting`

Поиск и квалификация потенциальных клиентов для аутрича.

- **Ключевые навыки:** кого целить первым; какие сигналы покупки важнее.
- **Задачи:** составить список целевых клиентов.
- **Сочетается с:** `marketing/cold-email`, `ecc/lead-intelligence`

### `claude-skills/revenue-operations`

Проверка воронки и прогнозов — покрытие, точность прогноза, magic number, окупаемость CAC.

- **Ключевые навыки:** метрики RevOps.
- **Задачи:** понять, хватит ли воронки для плана.
- **Сочетается с:** `claude-skills/commercial-forecaster`, `marketing/revops`

### `marketing/revops`

Revenue operations — жизненный цикл лида, передача в продажи.

- **Ключевые навыки:** когда лид готов для продаж; согласование маркетинга и продаж.
- **Задачи:** выстроить процесс передачи лидов.
- **Сочетается с:** `claude-skills/revenue-operations`, `marketing/sales-enablement`

### `claude-skills/rfp-responder`

Ответы на RFP, RFI, RFQ и анкеты безопасности.

- **Ключевые навыки:** разбор обязательных и взвешенных требований; черновики ответов.
- **Задачи:** ответить на тендер.
- **Сочетается с:** `claude-skills/sales-engineer`, `claude-skills/contract-and-proposal-writer`

### `marketing/sales-enablement`

Материалы для продаж — презентации, one-pager, работа с возражениями.

- **Ключевые навыки:** что дать чемпиону или продавцу; ответы на возражения.
- **Задачи:** вооружить отдел продаж.
- **Сочетается с:** `pm-skills/battle-card-builder`, `marketing/revops`

### `claude-skills/sales-engineer`

Пресейл — пробелы в RFP, матрицы сравнения функций, планирование и оценка пилотов.

- **Ключевые навыки:** анализ требований; proof of concept.
- **Задачи:** помочь продажам технически.
- **Сочетается с:** `claude-skills/rfp-responder`, `claude-skills/competitive-intel`

### `ecc/social-graph-ranker`

Взвешенное ранжирование социального графа для поиска тёплых интро.

- **Ключевые навыки:** оценка «мостов»; анализ пробелов в сети X и LinkedIn.
- **Задачи:** найти, через кого выйти на нужного человека.
- **Сочетается с:** `ecc/connections-optimizer`, `ecc/lead-intelligence`

---

<a id="cat-product"></a>
## Продакт-менеджмент

**Область применения.** Работа продакт-менеджера от исследования проблемы до запуска — discovery, приоритизация, PRD, метрики, roadmap, позиционирование.

**Решаемые задачи.** Формулировка проблемы и гипотез; интервью и исследования пользователей; PRD и пользовательские истории; приоритизация бэклога; метрики продукта; roadmap; позиционирование и ценообразование.

**Типовые связки.** problem-statement / discovery → интервью (user-research) → PRD (prd-writer / prd-development) → приоритизация → roadmap → метрики (metrics-definer) → запуск (launch-checklist).

Навыков в категории: 61.

### `claude-skills/agile-product-owner`

Работа с бэклогом — пользовательские истории, критерии приёмки, разбиение эпиков, оценка.

- **Ключевые навыки:** истории в формате INVEST; критерии приёмки; приоритизация на спринт.
- **Задачи:** подготовить бэклог к спринту.
- **Сочетается с:** `pm-skills/user-story`, `pm-setup/sprint-planner`, `claude-skills/scrum-master`

### `pm-skills/ai-shaped-readiness-advisor`

Оценка зрелости продуктовой работы с ИИ — AI-first или AI-shaped.

- **Ключевые навыки:** диагностика зрелости; следующая способность команды.
- **Задачи:** понять, как развивать работу с ИИ в продуктовой команде.
- **Сочетается с:** `pm-skills/context-engineering-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/code-to-prd`

PRD или спецификация продукта по существующему коду.

- **Ключевые навыки:** обратное проектирование требований; страницы, поля, маршруты, эндпоинты.
- **Задачи:** задокументировать продукт, у которого нет спецификации.
- **Сочетается с:** `pm-setup/prd-writer`, `claude-skills/codebase-onboarding`

### `claude-skills/competitive-teardown`

Глубокий разбор конкурента по 12 измерениям — цены, отзывы, найм, SEO, UX.

- **Ключевые навыки:** SWOT; карты позиционирования.
- **Задачи:** понять, как устроен и чем силён конкурент.
- **Сочетается с:** `claude-skills/competitive-intel`, `pm-setup/competitive-analysis`

### `claude-skills/cpo-advisor`

Советник по руководству продуктом.

- **Ключевые навыки:** измерение PMF; видение продукта; инвестиции в портфель; продуктовая оргструктура; отчёты совету.
- **Задачи:** принять продуктовое решение уровня директора.
- **Сочетается с:** `claude-skills/cpo-review`, `claude-skills/product-strategist`

### `claude-skills/cpo-review`

Критика roadmap, заявления о PMF или закрытия фичи.

- **Ключевые навыки:** позиция директора по продукту.
- **Задачи:** проверить продуктовый план.
- **Сочетается с:** `claude-skills/cpo-advisor`

### `pm-skills/customer-journey-mapping-workshop`

Воркшоп по карте пути клиента с адаптивными вопросами.

- **Ключевые навыки:** этапы, боли, возможности.
- **Задачи:** провести командную сессию по CJM.
- **Сочетается с:** `pm-skills/customer-journey-map`, `pm-skills/workshop-facilitation`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/customer-journey-map`

Карта пути клиента — этапы, точки контакта, действия, эмоции, метрики.

- **Ключевые навыки:** диагностика сломанного опыта.
- **Задачи:** выровнять команду вокруг опыта клиента.
- **Сочетается с:** `pm-skills/customer-journey-mapping-workshop`, `claude-skills/ux-researcher-designer`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/derisk-measurement-advisor`

Что измерять и тестировать, чтобы снизить риск продуктовой или ИИ-идеи.

- **Ключевые навыки:** внутренние риски (DUFV) и внешние (PESTEL).
- **Задачи:** стресс-тест идеи до вложений.
- **Сочетается с:** `pm-skills/pol-probe`, `pm-skills/pestel-analysis`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/discovery-interview-prep`

Подготовка интервью с клиентами — цель, сегмент, ограничения, метод.

- **Ключевые навыки:** валидация проблемы; интервью об оттоке.
- **Задачи:** спланировать discovery-интервью.
- **Сочетается с:** `pm-skills/discovery-process`, `pm-setup/user-research`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/discovery-process`

Полный цикл discovery от гипотезы проблемы до проверенного решения.

- **Ключевые навыки:** постановка; интервью; синтез; эксперименты.
- **Задачи:** пройти discovery структурированно.
- **Сочетается с:** `pm-skills/problem-statement`, `pm-skills/opportunity-solution-tree`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-checklist`

Чек-лист закрытия продукта по фазам с владельцем на каждом пункте.

- **Ключевые навыки:** операционный план сворачивания.
- **Задачи:** закрыть продукт без потерь.
- **Сочетается с:** `pm-skills/eol-process`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-internal-enablement`

FAQ поддержки, тезисы для продаж и работа с возражениями перед объявлением о закрытии.

- **Ключевые навыки:** подготовка клиентских команд.
- **Задачи:** подготовить команду к закрытию продукта.
- **Сочетается с:** `pm-skills/eol-message`, `pm-skills/eol-process`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-message`

Объявление о закрытии продукта нужного масштаба.

- **Ключевые навыки:** обоснование; влияние на клиентов; следующие шаги.
- **Задачи:** сообщить клиентам о закрытии.
- **Сочетается с:** `pm-skills/eol-stakeholder-sequence`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-process`

Закрытие продукта целиком — решение, согласование, план, подготовка, объявление, закрытие.

- **Ключевые навыки:** сквозной процесс EOL.
- **Задачи:** провести закрытие продукта.
- **Сочетается с:** `pm-skills/eol-readiness-advisor`, `pm-skills/eol-checklist`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-readiness-advisor`

Оценка «закрывать или нет» и масштаб усилий на закрытие.

- **Ключевые навыки:** go/no-go для вывода продукта.
- **Задачи:** когда говорят «надо бы это убить», но никто не решает.
- **Сочетается с:** `pm-skills/lifecycle-play-advisor`, `pm-skills/eol-process`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/eol-stakeholder-sequence`

С кем и в каком порядке говорить о закрытии продукта.

- **Ключевые навыки:** последовательность разговоров; содержание каждого.
- **Задачи:** избежать конфликтов при закрытии.
- **Сочетается с:** `pm-skills/stakeholder-mapping`, `pm-skills/eol-message`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/epic-breakdown-advisor`

Разбиение эпиков на истории по паттернам Humanizing Work.

- **Ключевые навыки:** паттерны разбиения.
- **Задачи:** когда задача слишком велика для оценки и поставки.
- **Сочетается с:** `pm-skills/user-story-splitting`, `pm-skills/user-story`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/epic-hypothesis`

Формулировка эпика как проверяемой гипотезы.

- **Ключевые навыки:** целевой пользователь; ожидаемый результат; метод проверки.
- **Задачи:** определить крупную инициативу до roadmap.
- **Сочетается с:** `pm-skills/epic-breakdown-advisor`, `pm-skills/pol-probe`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/experiment-designer`

Планирование A/B-тестов и продуктовых экспериментов.

- **Ключевые навыки:** гипотезы; размер выборки; приоритет; чтение результатов.
- **Задачи:** понять, сколько гнать тест и победил ли вариант.
- **Сочетается с:** `claude-skills/statistical-analyst`, `claude-skills/ab-test-setup`

### `pm-skills/feature-investment-advisor`

Оценка инвестиции в фичу по выручке, затратам, ROI и стратегии.

- **Ключевые навыки:** экономическое обоснование фичи.
- **Задачи:** решить, стоит ли фича вложений.
- **Сочетается с:** `pm-skills/prioritization-advisor`, `claude-skills/business-investment-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/finance-based-pricing-advisor`

Оценка изменения цен по ARPU, конверсии, риску оттока, NRR и окупаемости.

- **Ключевые навыки:** финансовая проверка ценового решения.
- **Задачи:** решить, выпускать ли изменение цен.
- **Сочетается с:** `marketing/pricing`, `claude-skills/pricing-strategist`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/incoming-request-advisor`

Разбор входящего запроса — буквальная просьба против реальной «работы».

- **Ключевые навыки:** декодирование сообщений в Slack, email, указаний.
- **Задачи:** понять, что на самом деле нужно стейкхолдеру.
- **Сочетается с:** `pm-skills/jobs-to-be-done`, `pm-skills/problem-statement`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/jobs-to-be-done`

Выявление «работ», болей и выгод клиента в формате JTBD.

- **Ключевые навыки:** неудовлетворённые потребности; перепозиционирование.
- **Задачи:** понять, зачем клиенты «нанимают» продукт.
- **Сочетается с:** `pm-skills/problem-statement`, `pm-skills/positioning-statement`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-setup/launch-checklist`

Чек-лист готовности к запуску.

- **Ключевые навыки:** предзапусковая проверка.
- **Задачи:** убедиться, что всё готово к релизу.
- **Сочетается с:** `marketing/launch`, `claude-skills/launch-strategy`

### `pm-skills/lean-ux-canvas`

Lean UX Canvas v2.

- **Ключевые навыки:** бизнес-проблема; допущения; что изучить дальше.
- **Задачи:** структурировать продуктовую гипотезу.
- **Сочетается с:** `pm-skills/problem-framing-canvas`, `pm-skills/pol-probe`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/lifecycle-play-advisor`

Диагностика стадии жизненного цикла продукта и выбор хода — продлить, заменить, вывести.

- **Ключевые навыки:** оценка стадии; рекомендация.
- **Задачи:** решить судьбу угасающего продукта.
- **Сочетается с:** `pm-skills/product-lifecycle-plays`, `pm-skills/eol-readiness-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-setup/metrics-definer`

Определение метрик успеха фичи или инициативы.

- **Ключевые навыки:** KPI; что измерять.
- **Задачи:** понять, как измерить успех.
- **Сочетается с:** `claude-skills/product-analytics`

### `marketing/onboarding`

Онбординг и активация — первый опыт, «ага-момент».

- **Ключевые навыки:** почему новые пользователи не остаются; что делать в первой сессии.
- **Задачи:** улучшить удержание новичков.
- **Сочетается с:** `claude-skills/onboarding-cro`, `marketing/emails`

### `pm-skills/opportunity-solution-tree`

Дерево возможностей и решений от цели к тестам.

- **Ключевые навыки:** связь результата, возможностей, решений и экспериментов.
- **Задачи:** превратить запрос стейкхолдера в продуктовую задачу.
- **Сочетается с:** `pm-skills/discovery-process`, `pm-skills/problem-statement`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/pol-probe-advisor`

Выбор типа пробы под гипотезу, риск и ресурсы.

- **Ключевые навыки:** соответствие метода цели обучения.
- **Задачи:** подобрать правильный эксперимент.
- **Сочетается с:** `pm-skills/pol-probe`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/pol-probe`

«Проба жизнеспособности» для дешёвой проверки рискованной гипотезы.

- **Ключевые навыки:** суровая правда до разработки.
- **Задачи:** проверить идею без полноценного продукта.
- **Сочетается с:** `pm-skills/pol-probe-advisor`, `pm-skills/epic-hypothesis`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/prd-development`

Структурированный PRD — проблема, пользователи, решение, критерии успеха.

- **Ключевые навыки:** от заметок discovery к документу для разработки.
- **Задачи:** написать полноценный PRD.
- **Сочетается с:** `pm-setup/prd-writer`, `pm-skills/user-story`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-setup/prd-writer`

Короткий PRD на 2–3 страницы — чёткий, с примерами.

- **Ключевые навыки:** one-pager; спецификация фичи.
- **Задачи:** быстро написать PRD.
- **Сочетается с:** `pm-skills/prd-development`, `pm-skills/user-story`

### `pm-skills/press-release`

Пресс-релиз в стиле Amazon до начала разработки.

- **Ключевые навыки:** определение ценности для клиента заранее.
- **Задачи:** согласовать видение нового продукта.
- **Сочетается с:** `pm-skills/prd-development`, `marketing/public-relations`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/prioritization-advisor`

Выбор фреймворка приоритизации — RICE, ICE, ценность и усилия и др.

- **Ключевые навыки:** подбор метода под стадию и контекст.
- **Задачи:** решить, как приоритизировать бэклог.
- **Сочетается с:** `claude-skills/product-manager-toolkit`, `pm-skills/feature-investment-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/problem-framing-canvas`

Канва постановки проблемы MITRE.

- **Ключевые навыки:** чёткая формулировка проблемы до решений.
- **Задачи:** не бросаться к решению раньше времени.
- **Сочетается с:** `pm-skills/problem-statement`, `pm-skills/lean-ux-canvas`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/problem-statement`

Формулировка проблемы с позиции пользователя.

- **Ключевые навыки:** кто заблокирован; что пытается сделать; почему важно; что чувствует.
- **Задачи:** зафиксировать проблему для discovery.
- **Сочетается с:** `pm-skills/jobs-to-be-done`, `pm-skills/problem-framing-canvas`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/product-analytics`

Продуктовые KPI, дашборды метрик, когортный анализ и удержание.

- **Ключевые навыки:** выбор метрик; когорты; анализ принятия фич.
- **Задачи:** измерять продукт правильно.
- **Сочетается с:** `pm-setup/metrics-definer`, `claude-skills/experiment-designer`

### `ecc/product-capability`

Перевод PRD, запросов roadmap и обсуждений в инженерный план возможности.

- **Ключевые навыки:** ограничения и инварианты; интерфейсы; нерешённые вопросы.
- **Задачи:** превратить продуктовую идею в план для разработки.
- **Сочетается с:** `ecc/product-lens`, `ecc/blueprint`, `ecc/intent-driven-development`

### `claude-skills/product-discovery`

Проверка продуктовых идей — карта допущений, discovery-спринты, проверка соответствия проблемы и решения.

- **Ключевые навыки:** допущения; эксперименты; валидация.
- **Задачи:** понять, стоит ли строить идею.
- **Сочетается с:** `pm-skills/discovery-process`, `pm-skills/opportunity-solution-tree`

### `ecc/product-lens`

Проверка «зачем» до разработки через четыре продуктовые диагностики в стиле YC.

- **Ключевые навыки:** продуктовый бриф PRODUCT-BRIEF.md; рекомендация делать или нет.
- **Задачи:** решить, стоит ли вообще строить фичу или продукт.
- **Сочетается с:** `ecc/product-capability`, `ecc/market-research`, `ecc/council`

### `pm-skills/product-lifecycle-plays`

Стадия жизненного цикла продукта и выбор хода — продление, замена или вывод.

- **Ключевые навыки:** стратегии зрелых и угасающих продуктов.
- **Задачи:** решить, что делать со зрелым продуктом.
- **Сочетается с:** `pm-skills/lifecycle-play-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/product-manager-toolkit`

Набор продакт-менеджера — приоритизация RICE, синтез интервью, PRD, выход на рынок.

- **Ключевые навыки:** ранжирование фич; документы; GTM.
- **Задачи:** решить, что строить дальше.
- **Сочетается с:** `pm-skills/prioritization-advisor`, `pm-setup/prd-writer`

### `claude-skills/product-skills`

Маршрутизатор продуктовых навыков — приоритизация, OKR, UX, эксперименты, discovery, roadmap.

- **Ключевые навыки:** выбор навыка.
- **Задачи:** понять, какой продуктовый навык нужен.
- **Сочетается с:** `claude-skills/product-manager-toolkit`

### `claude-skills/product-strategist`

Head of Product — каскад OKR, видение продукта, roadmap, структура команды.

- **Ключевые навыки:** квартальные OKR; продуктовое видение.
- **Задачи:** выстроить продуктовую стратегию.
- **Сочетается с:** `claude-skills/cpo-advisor`, `pm-skills/roadmap-planning`

### `pm-skills/product-strategy-session`

Сквозная сессия продуктовой стратегии — позиционирование, discovery, roadmap.

- **Ключевые навыки:** проверенное направление до обязательств.
- **Задачи:** определить стратегию продукта.
- **Сочетается с:** `pm-skills/positioning-workshop`, `pm-skills/roadmap-planning`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/proto-persona`

Прото-персона на основе текущих данных и знаний команды.

- **Ключевые навыки:** рабочий профиль клиента до глубоких исследований.
- **Задачи:** быстро определить целевого пользователя.
- **Сочетается с:** `claude-skills/ux-researcher-designer`, `pm-skills/jobs-to-be-done`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/recommendation-canvas`

Оценка ИИ-идеи продукта по результатам, гипотезам, рискам и позиционированию.

- **Ключевые навыки:** стоит ли ИИ-решение инвестиций.
- **Задачи:** обосновать или отклонить ИИ-фичу.
- **Сочетается с:** `pm-skills/derisk-measurement-advisor`, `claude-skills/chief-ai-officer-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/roadmap-communicator`

Рассказ о roadmap, release notes, changelog и апдейты для стейкхолдеров.

- **Ключевые навыки:** подача планов руководству, инженерам и клиентам.
- **Задачи:** объяснить планы разным аудиториям.
- **Сочетается с:** `pm-skills/roadmap-planning`, `claude-skills/changelog-generator`

### `pm-skills/roadmap-planning`

Стратегический roadmap — приоритеты, эпики, согласование, последовательность.

- **Ключевые навыки:** от стратегии к плану релизов.
- **Задачи:** составить roadmap.
- **Сочетается с:** `pm-skills/prioritization-advisor`, `claude-skills/roadmap-communicator`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/stakeholder-engagement-advisor`

План взаимодействия с конкретным стейкхолдером.

- **Ключевые навыки:** подготовка к разговору; работа с сопротивлением.
- **Задачи:** выстроить важные отношения перед ключевым этапом.
- **Сочетается с:** `pm-skills/stakeholder-mapping`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/stakeholder-identification`

Выявление всех стейкхолдеров до начала взаимодействия.

- **Ключевые навыки:** полная карта заинтересованных сторон.
- **Задачи:** запустить инициативу без сюрпризов.
- **Сочетается с:** `pm-skills/stakeholder-mapping`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/stakeholder-mapping`

Приоритизация стейкхолдеров по двум сеткам.

- **Ключевые навыки:** стратегия вовлечения; чей голос усилить.
- **Задачи:** понять, с кем и как работать.
- **Сочетается с:** `pm-skills/stakeholder-identification`, `pm-skills/stakeholder-engagement-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/storyboard`

Сторибординг из шести кадров — путь пользователя от проблемы к решению.

- **Ключевые навыки:** быстрый визуальный нарратив.
- **Задачи:** согласовать концепцию с командой.
- **Сочетается с:** `pm-skills/customer-journey-map`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-setup/user-research`

Синтез исследований и интервью.

- **Ключевые навыки:** выводы из интервью; находки.
- **Задачи:** превратить интервью в инсайты.
- **Сочетается с:** `claude-skills/interview-mapper`, `pm-skills/discovery-interview-prep`

### `pm-skills/user-story-mapping-workshop`

Воркшоп по карте историй с адаптивными вопросами.

- **Ключевые навыки:** опорные активности; срезы релизов.
- **Задачи:** провести командную сессию по story mapping.
- **Сочетается с:** `pm-skills/user-story-mapping`, `pm-skills/workshop-facilitation`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/user-story-mapping`

Карта пользовательских историй — активности, шаги, задачи, релизные срезы.

- **Ключевые навыки:** планирование MVP вокруг пути пользователя.
- **Задачи:** спланировать бэклог.
- **Сочетается с:** `pm-skills/user-story-mapping-workshop`, `pm-skills/user-story`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/user-story-splitting`

Разбиение большой истории или эпика на поставляемые части.

- **Ключевые навыки:** проверенные паттерны разбиения.
- **Задачи:** когда история слишком велика.
- **Сочетается с:** `pm-skills/epic-breakdown-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/user-story`

Пользовательские истории в формате Майка Кона с критериями приёмки на Gherkin.

- **Ключевые навыки:** истории, готовые к разработке.
- **Задачи:** превратить потребности в задачи.
- **Сочетается с:** `pm-skills/user-story-splitting`, `claude-skills/agile-product-owner`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/ux-researcher-designer`

UX-исследования — персоны, карты пути, планы юзабилити-тестов, синтез.

- **Ключевые навыки:** понимание пользователей.
- **Задачи:** узнать, кто пользователи и почему им трудно.
- **Сочетается с:** `pm-skills/customer-journey-map`, `pm-skills/proto-persona`

---

<a id="cat-project"></a>
## Управление проектами и командами

**Область применения.** Планирование и ведение проектов, Agile/Scrum, Jira/Confluence, ресурсы и риски, управление командами разработки.

**Решаемые задачи.** Планирование спринтов; статус-отчёты; управление рисками; ретроспективы; работа с Jira и Confluence; оргструктура и роли.

**Типовые связки.** sprint-planner → ведение задач (jira-*) → статус-отчёты → ретроспектива.

Навыков в категории: 14.

### `claude-skills/atlassian-admin`

Администрирование Atlassian — пользователи и группы Jira и Confluence, права, SSO, приложения, политики.

- **Ключевые навыки:** аудит прав; управление доступом; безопасность организации.
- **Задачи:** навести порядок в администрировании Atlassian.
- **Сочетается с:** `claude-skills/confluence-expert`, `claude-skills/jira-expert`

### `claude-skills/atlassian-templates`

Шаблоны и блупринты Jira и Confluence для повторного использования.

- **Ключевые навыки:** генерация шаблонов страниц и задач.
- **Задачи:** стандартизировать документы и задачи в организации.
- **Сочетается с:** `claude-skills/confluence-expert`, `claude-skills/atlassian-admin`

### `claude-skills/confluence-expert`

Построение и реструктуризация пространства Confluence.

- **Ключевые навыки:** иерархия страниц; права; шаблоны; макросы Jira; аудит контента.
- **Задачи:** навести порядок в базе знаний на Confluence.
- **Сочетается с:** `claude-skills/atlassian-templates`, `claude-skills/jira-expert`

### `claude-skills/internal-comms`

Внутренние объявления — реорганизация, новые инструменты, политика, смена руководства, сокращения, поглощение.

- **Ключевые навыки:** структура объявления; FAQ; план коммуникаций.
- **Задачи:** сообщить команде о важных изменениях.
- **Сочетается с:** `claude-skills/change-management`, `claude-skills/team-communications`

### `claude-skills/jira-expert`

Настройка Jira и запросы — JQL, процессы, поля, автоматизация, дашборды.

- **Ключевые навыки:** поиск и фильтры; workflow; автоматизация.
- **Задачи:** настроить Jira или найти нужные задачи.
- **Сочетается с:** `claude-skills/confluence-expert`, `ecc/jira-integration`

### `ecc/jira-integration`

Работа с задачами Jira через MCP или API.

- **Ключевые навыки:** чтение тикетов; анализ требований; смена статусов; комментарии.
- **Задачи:** взять задачу из Jira и обновить её по ходу работы.
- **Сочетается с:** `ecc/github-ops`, `ecc/project-flow-ops`

### `claude-skills/pm-skills`

Маршрутизатор навыков управления проектами — спринты, портфель, Jira, Confluence, коммуникации.

- **Ключевые навыки:** выбор навыка; цикл поставки.
- **Задачи:** понять, какой навык управления проектом нужен.
- **Сочетается с:** `claude-skills/senior-pm`, `claude-skills/scrum-master`

### `ecc/project-flow-ops`

Управление потоком работ между GitHub и Linear.

- **Ключевые навыки:** разбор issues и PR; связывание активной работы; разделение публичного и внутреннего.
- **Задачи:** держать задачи и код синхронизированными.
- **Сочетается с:** `ecc/github-ops`, `ecc/jira-integration`, `ecc/story-lifecycle`

### `claude-skills/scrum-master`

Аналитика спринтов и команды — прогноз скорости, здоровье спринта, ретро, burndown, блокеры.

- **Ключевые навыки:** velocity; ретроспективы.
- **Задачи:** улучшить работу Scrum-команды.
- **Сочетается с:** `pm-setup/sprint-planner`, `claude-skills/senior-pm`

### `claude-skills/senior-pm`

Управление проектами и портфелем с несколькими потоками работ.

- **Ключевые навыки:** планы; статус-отчёты; реестр рисков; загрузка; отчёты руководству.
- **Задачи:** вести сложную программу проектов.
- **Сочетается с:** `claude-skills/scrum-master`, `claude-skills/team-communications`

### `pm-setup/sprint-planner`

Планирование спринта и организация бэклога.

- **Ключевые навыки:** что брать в работу.
- **Задачи:** собрать план спринта.
- **Сочетается с:** `claude-skills/scrum-master`, `claude-skills/agile-product-owner`

### `ecc/story-lifecycle`

Файловый цикл «эпик → история → спринт» без внешнего трекера.

- **Ключевые навыки:** эпики; разбиение на истории; спринты; отслеживание статуса.
- **Задачи:** вести проект прямо в репозитории.
- **Сочетается с:** `ecc/project-flow-ops`, `ecc/blueprint`

### `claude-skills/team-communications`

Внутренние коммуникации — 3P-апдейты, статус-отчёты, рассылки, FAQ, отчёты об инцидентах.

- **Ключевые навыки:** шаблоны регулярных отчётов.
- **Задачи:** написать статус-апдейт.
- **Сочетается с:** `claude-skills/internal-comms`, `claude-skills/senior-pm`

### `pm-skills/workshop-facilitation`

Проведение воркшопов в многоходовом формате.

- **Ключевые навыки:** темп; варианты; отслеживание прогресса.
- **Задачи:** провести интерактивную командную сессию.
- **Сочетается с:** `pm-skills/positioning-workshop`, `pm-skills/user-story-mapping-workshop`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

---

<a id="cat-strategy"></a>
## Стратегия бизнеса и C-level

**Область применения.** Советники уровня CEO/CFO/CMO/CTO/COO и других руководителей, стратегия, рост, конкурентный анализ, организационное развитие.

**Решаемые задачи.** Стратегические решения и сценарии; совет директоров и инвесторы; оргдизайн; конкурентная разведка; бизнес-модели; кризисные решения.

**Типовые связки.** competitive-platform-analysis → benchmark-methodology → competitive-report-structure; council / C-level советники для решения → executive-материалы.

Навыков в категории: 65.

### `claude-skills/agent-protocol`

Протокол взаимодействия агентов-советников C-level между собой.

- **Ключевые навыки:** синтаксис вызова; защита от циклов; изоляция; формат ответов.
- **Задачи:** организовать совещание нескольких виртуальных руководителей.
- **Сочетается с:** `claude-skills/board-meeting`, `claude-skills/chief-of-staff`

### `claude-skills/andreessen`

Прямой «рыночный» вердикт по идее, бизнесу или карьерной ставке с сильнейшим контраргументом.

- **Ключевые навыки:** рынок прежде всего; контраргументы; ежедневный план на карточке 3×5.
- **Задачи:** трезво оценить идею до вложений.
- **Сочетается с:** `ecc/product-lens`, `claude-skills/challenge`

### `pm-skills/ansoff-matrix`

Варианты роста по матрице Ансоффа с оценкой рисков и последовательностью.

- **Ключевые навыки:** рынки и продукты; доказательная база.
- **Задачи:** решить, откуда брать следующий рост.
- **Сочетается с:** `pm-skills/organic-growth-advisor`, `pm-skills/porters-five-forces`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/arquiteto-de-empresa`

Описание и проектирование компании целиком в версионируемом markdown («компания как код»).

- **Ключевые навыки:** вики компании, читаемая агентами; структура и процессы в файлах.
- **Задачи:** задокументировать устройство компании для людей и агентов.
- **Сочетается с:** `claude-skills/company-os`, `claude-skills/culture-architect`

### `ecc/benchmark-methodology`

Оценка конкурентов по девяти взвешенным измерениям с рубриками 1–5 и картой напряжений.

- **Ключевые навыки:** позиционирование, голос, визуал, упаковка предложения, доказательства, цены; профили конкурентов.
- **Задачи:** сравнить и оценить конкурентов перед сборкой отчёта.
- **Сочетается с:** `ecc/competitive-platform-analysis`, `ecc/competitive-report-structure`, `ecc/market-research`

### `claude-skills/board-deck-builder`

Презентация для совета директоров, апдейт инвесторам или QBR с позиций всех руководителей.

- **Ключевые навыки:** структура нарратива; как подавать плохие новости.
- **Задачи:** подготовить материалы к совету директоров.
- **Сочетается с:** `claude-skills/board-prep`, `ecc/investor-materials`

### `claude-skills/board-meeting`

Структурированное совещание нескольких виртуальных руководителей в шесть этапов.

- **Ключевые навыки:** контекст; изолированные мнения C-level; дебаты; синтез; решение.
- **Задачи:** принять стратегическое решение, затрагивающее много функций.
- **Сочетается с:** `claude-skills/boardroom`, `claude-skills/chief-of-staff`, `claude-skills/decision-logger`

### `claude-skills/board-prep`

Подготовка к совету директоров, апдейту инвесторам или питчу, где цифры будут оспаривать.

- **Ключевые навыки:** знание цифр наизусть; предугадывание трудных вопросов.
- **Задачи:** подготовиться к жёстким вопросам по цифрам.
- **Сочетается с:** `claude-skills/board-deck-builder`, `claude-skills/cfo-advisor`

### `claude-skills/boardroom`

Совещание C-suite в шесть этапов по решению, затрагивающему несколько областей.

- **Ключевые навыки:** изменение цен; привлечение денег или сокращение; многофункциональный анализ.
- **Задачи:** принять решение с учётом всех руководящих позиций.
- **Сочетается с:** `claude-skills/board-meeting`, `claude-skills/brief`, `claude-skills/decide`

### `claude-skills/brief`

Одностраничный бриф стратегического вопроса — варианты, допущения, критерии успеха.

- **Ключевые навыки:** постановка вопроса до обсуждения.
- **Задачи:** сформулировать вопрос для совещания руководителей.
- **Сочетается с:** `claude-skills/boardroom`

### `claude-skills/c-level-agents`

Виртуальная команда руководителей — 13 агентов C-suite и 21 команда.

- **Ключевые навыки:** маршрутизация вопросов; многоролевые обсуждения.
- **Задачи:** получить совет «команды руководителей» по бизнесу.
- **Сочетается с:** `claude-skills/boardroom`, `claude-skills/c-level-skills`

### `claude-skills/c-level-skills`

Подбор советника C-level под вопрос — 14 ролей, советы директоров, культура, M&A.

- **Ключевые навыки:** навигация по советникам.
- **Задачи:** понять, к какому советнику обратиться.
- **Сочетается с:** `claude-skills/chief-of-staff`, `claude-skills/c-level-agents`

### `claude-skills/caio-review`

Критика плана, связанного с ИИ, с позиции директора по ИИ.

- **Ключевые навыки:** наличие набора оценок; API, дообучение или своя модель; класс по EU AI Act.
- **Задачи:** проверить ИИ-план на слабые места.
- **Сочетается с:** `claude-skills/chief-ai-officer-advisor`, `claude-skills/ai-act-readiness`

### `claude-skills/cco-review`

Критика плана по оттоку, удержанию, сегментам или найму в customer success.

- **Ключевые навыки:** позиция директора по клиентам.
- **Задачи:** проверить план удержания клиентов.
- **Сочетается с:** `claude-skills/chief-customer-officer-advisor`, `claude-skills/customer-success-manager`

### `claude-skills/cdo-review`

Критика плана, затрагивающего права на данные, архитектуру данных или их монетизацию.

- **Ключевые навыки:** позиция директора по данным.
- **Задачи:** проверить план работы с данными.
- **Сочетается с:** `claude-skills/chief-data-officer-advisor`

### `claude-skills/ceo-advisor`

Советник для CEO и основателя по управлению компанией.

- **Ключевые навыки:** проблемы с советом и инвесторами; привлекать или сокращать; стратегические ставки; оргструктура и культура.
- **Задачи:** принять трудное решение уровня CEO.
- **Сочетается с:** `claude-skills/board-meeting`, `claude-skills/cfo-advisor`, `claude-skills/challenge`

### `claude-skills/challenge`

Пре-мортем плана — допустим, через год он провалился; какие допущения и риски к этому привели.

- **Ключевые навыки:** поиск рискованных допущений; зависимости; риски исполнения.
- **Задачи:** проверить план до того, как в него вложиться.
- **Сочетается с:** `ecc/council`, `claude-skills/ceo-advisor`

### `claude-skills/change-management`

Проведение изменений — реорганизация, пивот, смена инструментов, руководства, закрытие продукта.

- **Ключевые навыки:** модель ADKAR; шаблоны коммуникаций; работа с сопротивлением.
- **Задачи:** провести изменения с минимальным сопротивлением.
- **Сочетается с:** `claude-skills/culture-architect`, `claude-skills/internal-comms`

### `claude-skills/chief-of-staff`

Маршрутизация вопросов основателя к нужному советнику C-level и созыв совещаний.

- **Ключевые навыки:** контекст компании; выбор советника; организация обсуждения.
- **Задачи:** понять, кто из «руководителей» должен ответить.
- **Сочетается с:** `claude-skills/c-level-skills`, `claude-skills/board-meeting`

### `claude-skills/company-os`

Выбор и настройка операционной системы компании — EOS, Scaling Up или OKR.

- **Ключевые навыки:** карта ответственности; скоркарды; ритм встреч; квартальные приоритеты.
- **Задачи:** выстроить управленческую систему компании.
- **Сочетается с:** `claude-skills/coo-advisor`, `claude-skills/strategic-alignment`

### `pm-skills/competitive-analysis-process`

Полный конкурентный анализ в шесть шагов — от ландшафта до стратегического направления.

- **Ключевые навыки:** оркестрация конкурентных навыков.
- **Задачи:** получить полную картину конкуренции.
- **Сочетается с:** `pm-skills/market-landscape-scan`, `pm-skills/competitive-research-snapshot`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-setup/competitive-analysis`

Конкурентный анализ по запросу «проанализируй конкурента» или «сравни нас с компанией».

- **Ключевые навыки:** структурированное сравнение.
- **Задачи:** быстро разобрать конкурента.
- **Сочетается с:** `claude-skills/competitive-teardown`, `pm-skills/competitive-research-snapshot`

### `pm-skills/competitive-intel-watch`

Регулярный мониторинг изменений у конкурентов относительно прошлого снимка.

- **Ключевые навыки:** только существенные сдвиги; доказательства.
- **Задачи:** отслеживать конкурентов по расписанию.
- **Сочетается с:** `pm-skills/pricing-packaging-tracker`, `claude-skills/competitive-intel`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/competitive-intel`

Конкурентная разведка — battlecards, разбор побед и поражений, позиционирование против альтернатив.

- **Ключевые навыки:** система отслеживания конкурентов; материалы для продаж.
- **Задачи:** выстроить постоянный мониторинг конкурентов.
- **Сочетается с:** `claude-skills/competitive-teardown`, `ecc/competitive-platform-analysis`

### `ecc/competitive-platform-analysis`

Определение и фильтрация набора конкурентов перед бенчмаркингом — кто конкурент, какого уровня, какие источники изучать.

- **Ключевые навыки:** категоризация конкурентов; скоринговый фильтр; выбор источников.
- **Задачи:** первый шаг конкурентного анализа.
- **Сочетается с:** `ecc/benchmark-methodology`, `ecc/competitive-report-structure`, `ecc/market-research`

### `ecc/competitive-report-structure`

Сборка оценённых профилей конкурентов в отчёт для принятия решений.

- **Ключевые навыки:** карта рынка; уровни конкурентов; матрица сравнения; анализ свободных ниш; стратегические рекомендации.
- **Задачи:** представить конкурентный анализ руководству или совету директоров.
- **Сочетается с:** `ecc/benchmark-methodology`, `ecc/competitive-platform-analysis`, `ecc/investor-materials`

### `pm-skills/competitive-research-snapshot`

Снимок конкурентного ландшафта с источниками, матрицей сравнения и выводами.

- **Ключевые навыки:** «и что из этого следует» для продукта.
- **Задачи:** обосновать продуктовое решение конкурентными данными.
- **Сочетается с:** `pm-skills/battle-card-builder`, `pm-skills/competitive-intel-watch`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `marketing/competitor-profiling`

Досье на конкурентов с датами — цены, заявления, действия.

- **Ключевые навыки:** проверка выводов о конкуренте; мониторинг изменений.
- **Задачи:** знать, что делают конкуренты.
- **Сочетается с:** `marketing/competitors`, `marketing/reverse-engineer-marketing`

### `claude-skills/context-engine`

Загрузка и обновление контекста компании для советников C-level.

- **Ключевые навыки:** проверка свежести контекста; защита данных перед отправкой во внешние сервисы.
- **Задачи:** обеспечить советникам актуальный контекст.
- **Сочетается с:** `claude-skills/cs-onboard`, `claude-skills/chief-of-staff`

### `ecc/council-multi-model`

Дополнительная внешняя критика решения совета другой моделью (Codex) с явного согласия.

- **Ключевые навыки:** попытка «сломать» итоговое решение; честная пометка источника критики.
- **Задачи:** перепроверить важное решение независимой моделью.
- **Сочетается с:** `ecc/council`

### `ecc/council`

«Совет» из четырёх голосов для неоднозначных решений и выбора «делать или нет».

- **Ключевые навыки:** структурированное несогласие; взвешивание компромиссов; итоговое решение.
- **Задачи:** выбрать из нескольких разумных вариантов.
- **Сочетается с:** `ecc/council-multi-model`, `ecc/recursive-decision-ledger`

### `claude-skills/cross-eval`

Независимая проверка важного меморандума несколькими моделями до обсуждения.

- **Ключевые навыки:** межмодельная критика.
- **Задачи:** перепроверить важное решение.
- **Сочетается с:** `ecc/council-multi-model`, `claude-skills/boardroom`

### `claude-skills/cs-onboard`

Первичная настройка советников C-level — интервью основателя о компании.

- **Ключевые навыки:** сбор контекста; обновление после раунда или пивота.
- **Задачи:** настроить виртуальную команду руководителей.
- **Сочетается с:** `claude-skills/context-engine`

### `claude-skills/culture-architect`

Ценности компании, перевод их в поведение, оценка культуры, ритуалы.

- **Ключевые навыки:** культура как операционное поведение, а не лозунги.
- **Задачи:** сформулировать и внедрить ценности.
- **Сочетается с:** `claude-skills/chro-advisor`, `claude-skills/change-management`

### `claude-skills/decide`

Фиксация одобренного решения совещания руководителей.

- **Ключевые навыки:** журнал решений.
- **Задачи:** записать решение, чтобы к нему вернуться.
- **Сочетается с:** `claude-skills/decision-logger`, `claude-skills/boardroom`

### `claude-skills/decision-logger`

Журнал решений после совещаний — обзор прошлых решений и просроченных действий.

- **Ключевые навыки:** хранение протоколов и одобренных решений.
- **Задачи:** отслеживать исполнение решений.
- **Сочетается с:** `claude-skills/decide`, `claude-skills/board-meeting`

### `claude-skills/execute`

Превращение одобренного решения в план на 90 дней с недельными вехами и ответственными.

- **Ключевые навыки:** план исполнения; вехи; владельцы.
- **Задачи:** перейти от решения к действиям.
- **Сочетается с:** `claude-skills/decide`, `claude-skills/post-mortem`

### `claude-skills/executive-mentor`

Наставник руководителя — стресс-тест плана, трудные решения, подготовка к сложному совету, честный разбор.

- **Ключевые навыки:** жёсткие вопросы; разбор ошибок.
- **Задачи:** получить честную обратную связь по важному решению.
- **Сочетается с:** `claude-skills/founder-coach`, `claude-skills/hard-call`

### `claude-skills/founder-coach`

Коучинг основателя, который стал узким местом, не делегирует или выгорает.

- **Ключевые навыки:** делегирование; аудит энергии и календаря; переход от исполнителя к CEO.
- **Задачи:** разгрузить основателя.
- **Сочетается с:** `claude-skills/executive-mentor`, `claude-skills/ceo-advisor`

### `claude-skills/founder-mode`

Маршрутизация стратегического вопроса основателя к нужному советнику C-suite.

- **Ключевые навыки:** выбор советника или совещания.
- **Задачи:** получить совет, когда непонятно, к кому идти.
- **Сочетается с:** `claude-skills/chief-of-staff`, `claude-skills/office-hours`

### `claude-skills/freeze`

«Заморозка» необратимого решения, принятого под давлением, на период остывания.

- **Ключевые навыки:** защита от поспешных решений.
- **Задачи:** не принимать необратимое решение сгоряча.
- **Сочетается с:** `claude-skills/hard-call`, `claude-skills/decide`

### `claude-skills/hard-call`

Решение, когда все варианты болезненны.

- **Ключевые навыки:** метод 10/10/10; минимизация сожалений.
- **Задачи:** выбрать между сокращениями и плохим раундом, закрыть любимый продукт.
- **Сочетается с:** `claude-skills/freeze`, `claude-skills/executive-mentor`

### `claude-skills/internal-narrative`

Единый нарратив компании для общих собраний, инвесторов, найма и кризисов.

- **Ключевые навыки:** согласование историй для разных аудиторий.
- **Задачи:** рассказывать о компании последовательно.
- **Сочетается с:** `claude-skills/board-deck-builder`, `claude-skills/internal-comms`

### `claude-skills/intl-expansion`

Выход на новую страну — выбор рынка, способ входа, локализация, регулирование, региональный GTM.

- **Ключевые навыки:** оценка рынков; модели входа.
- **Задачи:** спланировать международную экспансию.
- **Сочетается с:** `claude-skills/business-name-fit`, `ecc/market-research`

### `claude-skills/ma-playbook`

Покупка или продажа компании — due diligence, оценка, условия, интеграция.

- **Ключевые навыки:** сделки M&A; выход.
- **Задачи:** провести сделку слияния или поглощения.
- **Сочетается с:** `claude-skills/financial-analyst`, `claude-skills/general-counsel-advisor`

### `pm-skills/market-landscape-scan`

Карта рынка — сегменты, игроки, заменители, свободные ниши с источниками.

- **Ключевые навыки:** структура рынка.
- **Задачи:** оценить рынок перед входом.
- **Сочетается с:** `pm-skills/tam-sam-som-calculator`, `pm-skills/porters-five-forces`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `scientific/market-research-reports`

Рыночные отчёты с прослеживаемыми источниками и сценариями допущений.

- **Ключевые навыки:** границы рынка; TAM/SAM/SOM; конкурентный анализ
- **Задачи:** Подготовить исследовательский отчёт, отделяя наблюдения от прогнозных допущений.
- **Сочетается с:** `scientific/paper-lookup`, `ecc/market-research`

### `claude-skills/office-hours`

Совет основателю после шести вопросов в стиле YC.

- **Ключевые навыки:** диагностика ситуации; совет.
- **Задачи:** когда непонятно, что спрашивать.
- **Сочетается с:** `claude-skills/founder-mode`

### `claude-skills/onboard`

Интервью основателя для заполнения контекста компании виртуального C-suite.

- **Ключевые навыки:** файл company-context.md.
- **Задачи:** дать советникам контекст.
- **Сочетается с:** `claude-skills/cs-onboard`

### `claude-skills/org-health-diagnostic`

Проверка здоровья компании по 8 измерениям со светофором.

- **Ключевые навыки:** оценка функций; зоны риска.
- **Задачи:** найти слабые места компании перед советом.
- **Сочетается с:** `claude-skills/strategic-alignment`

### `pm-skills/organic-growth-advisor`

Выбор пути органического роста — новые сегменты, география, каналы, продукты.

- **Ключевые навыки:** где ограничение роста.
- **Задачи:** найти следующий источник роста.
- **Сочетается с:** `pm-skills/ansoff-matrix`, `pm-skills/acquisition-channel-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/pestel-analysis`

PESTEL-анализ — политические, экономические, социальные, технологические, экологические и правовые факторы.

- **Ключевые навыки:** внешние силы, влияющие на продукт.
- **Задачи:** учесть внешние риски в стратегии.
- **Сочетается с:** `pm-skills/pestel-delta-monitor`, `pm-skills/swot-analysis`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/pestel-delta-monitor`

Квартальный пересмотр PESTEL — что изменилось, какие допущения сломались.

- **Ключевые навыки:** мониторинг внешних факторов.
- **Задачи:** держать стратегию актуальной.
- **Сочетается с:** `pm-skills/pestel-analysis`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/porters-five-forces`

Анализ отрасли по пяти силам Портера с сигналами по каждой оценке.

- **Ключевые навыки:** структура отрасли; пул прибыли.
- **Задачи:** оценить привлекательность рынка.
- **Сочетается с:** `pm-skills/market-landscape-scan`, `pm-skills/swot-analysis`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/post-mortem`

Разбор решения через 90 дней или при срабатывании критериев остановки.

- **Ключевые навыки:** сверка с исходными допущениями; выводы.
- **Задачи:** проверить, оправдалось ли решение.
- **Сочетается с:** `claude-skills/decide`, `claude-skills/postmortem`

### `claude-skills/postmortem`

Безвинный разбор провала — запуск, квартал, неудачный найм.

- **Ключевые навыки:** 5 почему; реестр изменений.
- **Задачи:** извлечь уроки из неудачи.
- **Сочетается с:** `claude-skills/post-mortem`, `claude-skills/challenge`

### `pm-skills/pricing-packaging-tracker`

Отслеживание цен и упаковки конкурентов как временного ряда.

- **Ключевые навыки:** тарифы, ограничения, изменения цен.
- **Задачи:** мониторить цены конкурентов ежемесячно.
- **Сочетается с:** `pm-skills/competitive-intel-watch`, `marketing/pricing`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `ecc/recursive-decision-ledger`

Многократные прогоны рассуждений с журналом решений.

- **Ключевые навыки:** испытания; оценки; проверки согласованности; гейты продвижения.
- **Задачи:** принять сложное решение через серию проверяемых итераций.
- **Сочетается с:** `ecc/council`

### `marketing/reverse-engineer-marketing`

Как вырос другой бизнес и что можно скопировать.

- **Ключевые навыки:** журнал действий конкурента по датам.
- **Задачи:** учиться на росте конкурентов.
- **Сочетается с:** `marketing/competitor-profiling`

### `claude-skills/roast`

Разгром идеи панелью из пяти ролей и вердикт судьи GO, RESHAPE или KILL.

- **Ключевые навыки:** критик, защитник, аналитик, следователь, клиент.
- **Задачи:** проверить идею на прочность.
- **Сочетается с:** `claude-skills/challenge`, `ecc/council`

### `claude-skills/scenario-war-room`

Моделирование составных сценариев «что если X и Y одновременно» с каскадом последствий.

- **Ключевые навыки:** сценарный анализ по функциям.
- **Задачи:** подготовиться к кризисным сценариям.
- **Сочетается с:** `claude-skills/stress-test`, `claude-skills/hard-call`

### `claude-skills/strategic-alignment`

Согласование стратегии, когда команды тянут в разные стороны.

- **Ключевые навыки:** каскад стратегии; «осиротевшие» OKR; локальная оптимизация.
- **Задачи:** выстроить всех в одну линию.
- **Сочетается с:** `claude-skills/company-os`, `claude-skills/org-health-diagnostic`

### `claude-skills/stress-test`

Стресс-тест плана на непроверенных допущениях.

- **Ключевые навыки:** проверка «хоккейных клюшек» и долгих пилотов.
- **Задачи:** понять, выдержит ли план реальность.
- **Сочетается с:** `claude-skills/challenge`, `claude-skills/scenario-war-room`

### `pm-skills/swot-analysis`

SWOT компании по публичным источникам с перекрёстными выводами S-O и W-T.

- **Ключевые навыки:** доказательный SWOT.
- **Задачи:** стратегический обзор своей компании или конкурента.
- **Сочетается с:** `pm-skills/pestel-analysis`, `pm-skills/porters-five-forces`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/tam-sam-som-calculator`

Расчёт TAM, SAM и SOM с явными допущениями и оговорками.

- **Ключевые навыки:** методы оценки рынка.
- **Задачи:** оценить рынок для бизнес-кейса.
- **Сочетается с:** `claude-skills/market-research`, `pm-skills/market-landscape-scan`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

---

<a id="cat-finance"></a>
## Финансы, биллинг и инвестиции

**Область применения.** Финансовый анализ и модели, бюджет, бухгалтерия, налоги, биллинг и подписки, привлечение инвестиций.

**Решаемые задачи.** Финансовые модели и прогнозы; анализ отчётности; юнит-экономика; управление подписками и возвратами; материалы для инвесторов; трейдинг-риски.

**Типовые связки.** финансовая модель → анализ (financial-analyst) → investor-materials → investor-outreach; биллинг — customer-billing-ops / finance-billing-ops.

Навыков в категории: 21.

### `pm-skills/business-health-diagnostic`

Диагностика здоровья SaaS — рост, удержание, эффективность, капитал.

- **Ключевые навыки:** комплексная оценка; приоритет срочных исправлений.
- **Задачи:** подготовить бизнес-ревью.
- **Сочетается с:** `pm-skills/saas-revenue-growth-metrics`, `pm-skills/saas-economics-efficiency-metrics`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/business-investment-advisor`

Оценка капитальных затрат — оборудование, недвижимость, покупка бизнеса, найм, технологии.

- **Ключевые навыки:** ROI, IRR, NPV, срок окупаемости; build vs buy.
- **Задачи:** решить, окупится ли вложение.
- **Сочетается с:** `claude-skills/cfo-advisor`, `claude-skills/financial-analyst`

### `claude-skills/cfo-advisor`

Финансы стартапа — runway и burn, юнит-экономика, фандрайзинг и размытие.

- **Ключевые навыки:** LTV, CAC, окупаемость; прогноз денег; условия раунда.
- **Задачи:** понять, на сколько хватит денег и как привлечь ещё.
- **Сочетается с:** `claude-skills/financial-analyst`, `claude-skills/board-prep`, `ecc/investor-materials`

### `claude-skills/cfo-review`

Критика плана, требующего реальных расходов — волна найма, раунд, рекламный бюджет.

- **Ключевые навыки:** позиция финансового директора.
- **Задачи:** проверить, выдержит ли бюджет план.
- **Сочетается с:** `claude-skills/cfo-advisor`

### `claude-skills/commercial-forecaster`

Прогноз бронирований, ARR, воронки и NRR.

- **Ключевые навыки:** сценарии commit, best case и pipeline; цифра для совета.
- **Задачи:** построить прогноз выручки.
- **Сочетается с:** `claude-skills/cro-advisor`, `claude-skills/financial-analyst`

### `ecc/customer-billing-ops`

Операции с биллингом клиентов через Stripe и подобные сервисы.

- **Ключевые навыки:** подписки; возвраты; разбор оттока; восстановление доступа к порталу оплаты; анализ тарифов.
- **Задачи:** помочь клиенту с оплатой; проверить состояние подписки.
- **Сочетается с:** `ecc/finance-billing-ops`, `ecc/email-ops`

### `ecc/finance-billing-ops`

Анализ выручки, цен, возвратов и командного биллинга на основе фактических данных.

- **Ключевые навыки:** срез продаж; сравнение тарифов; поиск дублирующих списаний; проверка модели биллинга.
- **Задачи:** понять реальные цифры выручки и проблемы биллинга.
- **Сочетается с:** `ecc/customer-billing-ops`, `ecc/investor-materials`

### `pm-skills/finance-metrics-quickref`

Быстрый справочник SaaS-метрик — формулы и бенчмарки.

- **Ключевые навыки:** определения; формулы; ориентиры.
- **Задачи:** быстро вспомнить метрику во время анализа.
- **Сочетается с:** `claude-skills/saas-metrics-coach`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/finance-skills`

Выбор финансового навыка — коэффициенты, DCF, прогнозы, SaaS-метрики, закрытие месяца.

- **Ключевые навыки:** маршрутизация по финансовым навыкам.
- **Задачи:** понять, какой навык нужен для финансового вопроса.
- **Сочетается с:** `claude-skills/financial-analyst`, `claude-skills/saas-metrics-coach`

### `claude-skills/financial-analyst`

Анализ отчётности, оценка компании по DCF, анализ отклонений бюджета, скользящие прогнозы.

- **Ключевые навыки:** финансовые коэффициенты; DCF; прогнозирование.
- **Задачи:** понять финансовое состояние и стоимость компании.
- **Сочетается с:** `claude-skills/cfo-advisor`, `claude-skills/stock-analysis`

### `ecc/investor-materials`

Питч-деки, one-pager, инвестмеморандумы, заявки в акселераторы и финмодели.

- **Ключевые навыки:** структура питча; финансовая модель; материалы для фандрайзинга.
- **Задачи:** подготовить материалы для инвесторов.
- **Сочетается с:** `ecc/investor-outreach`, `ecc/market-research`, `ecc/frontend-slides`

### `ecc/investor-outreach`

Холодные письма, тёплые интро, фоллоу-апы и апдейты для инвесторов.

- **Ключевые навыки:** тексты для ангелов и фондов; регулярные апдейты.
- **Задачи:** провести коммуникацию в ходе привлечения инвестиций.
- **Сочетается с:** `ecc/investor-materials`, `ecc/brand-voice`

### `claude-skills/month-end-close`

Закрытие месяца или квартала — чек-лист, календарь, сверки, ускорение.

- **Ключевые навыки:** процесс закрытия; сверки счетов.
- **Задачи:** закрывать месяц быстрее и без ошибок.
- **Сочетается с:** `claude-skills/financial-analyst`

### `claude-skills/passive-deal-screener`

Проверка частной инвестиционной сделки для пассивного инвестора.

- **Ключевые навыки:** стресс-тест синдикаций, preferred equity, бридж-фондов, частного кредита.
- **Задачи:** решить, участвовать ли в сделке.
- **Сочетается с:** `claude-skills/business-investment-advisor`

### `claude-skills/research-finance`

Деньги программы НИОКР — бюджеты, накладные расходы, burn и runway по вехам, капитализация или расход.

- **Ключевые навыки:** многолетние бюджеты; учёт затрат на R&D.
- **Задачи:** спланировать финансы исследования.
- **Сочетается с:** `claude-skills/financial-analyst`, `claude-skills/grants`

### `pm-skills/saas-economics-efficiency-metrics`

Юнит-экономика и эффективность капитала SaaS.

- **Ключевые навыки:** CAC payback, burn multiple и др.
- **Задачи:** понять, может ли бизнес эффективно масштабироваться.
- **Сочетается с:** `pm-skills/saas-revenue-growth-metrics`, `claude-skills/saas-metrics-coach`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/saas-metrics-coach`

Разбор SaaS-метрик — ARR, MRR, отток, LTV, CAC, NRR.

- **Ключевые навыки:** расчёт и интерпретация; бенчмарки.
- **Задачи:** понять, как дела у SaaS-бизнеса.
- **Сочетается с:** `pm-skills/saas-economics-efficiency-metrics`, `claude-skills/cfo-advisor`

### `pm-skills/saas-revenue-growth-metrics`

Метрики выручки, удержания и роста SaaS.

- **Ключевые навыки:** моментум; отток; расширение; сигналы PMF.
- **Задачи:** диагностировать рост бизнеса.
- **Сочетается с:** `pm-skills/business-health-diagnostic`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/stock-analysis`

Анализ и оценка публичной компании (США, мир, NSE, BSE) на проверенных данных.

- **Ключевые навыки:** коэффициенты; скоринги; оценка стоимости.
- **Задачи:** проанализировать акцию.
- **Сочетается с:** `claude-skills/financial-analyst`

### `claude-skills/stripe-integration-expert`

Интеграция Stripe — подписки, триалы, проратация, checkout, оплата по использованию, вебхуки, портал, счета.

- **Ключевые навыки:** биллинг в Next.js и других стеках.
- **Задачи:** подключить оплату.
- **Сочетается с:** `ecc/customer-billing-ops`, `claude-skills/saas-scaffolder`

### `scientific/usfiscaldata`

Запросы к U.S. Treasury Fiscal Data REST API без API-ключа.

- **Ключевые навыки:** госдолг; аукционы; бюджет и курсы
- **Задачи:** Получить воспроизводимые финансовые ряды из официального источника.
- **Сочетается с:** `scientific/database-lookup`

---

<a id="cat-compliance"></a>
## Регуляторика, комплаенс и качество (QMS)

**Область применения.** ISO 13485/9001/27001, MDR/FDA, GDPR, HIPAA, SOC 2, CMMC, аудит, системы менеджмента качества, договоры.

**Решаемые задачи.** Подготовка к аудитам и сертификации; CAPA и несоответствия; оценка рисков; политика конфиденциальности данных; регистрация медизделий; шаблоны договоров.

**Типовые связки.** оценка готовности (*-readiness) → риск-менеджмент → документы QMS → внутренний аудит → CAPA.

Навыков в категории: 34.

### `claude-skills/access-lifecycle`

Ревизия доступов пользователей и сервисных учётных записей.

- **Ключевые навыки:** проверка отзыва доступа у уволившихся; поиск «осиротевших» сервисных аккаунтов; ответы аудиторам.
- **Задачи:** провести периодический пересмотр доступов.
- **Сочетается с:** `claude-skills/ciso-advisor`, `claude-skills/compliance-os`

### `claude-skills/agent-decision-receipts`

«Квитанции» о действиях автономного агента с побочными эффектами для последующего доказательства.

- **Ключевые навыки:** журнал деплоев, удалений, платежей, выдачи доступов; требования EU AI Act ст. 12.
- **Задачи:** обеспечить аудиторский след действий агента.
- **Сочетается с:** `claude-skills/ai-act-readiness`, `ecc/agent-security-hardening`

### `claude-skills/ai-act-readiness`

Готовность к EU AI Act — класс риска, обязанности, сроки.

- **Ключевые навыки:** классификация ИИ-системы; перечень обязанностей; дедлайны.
- **Задачи:** понять, применяется ли закон и что делать.
- **Сочетается с:** `claude-skills/aims-audit`, `claude-skills/agent-decision-receipts`

### `claude-skills/aims-audit`

Проверка готовности системы управления ИИ по ISO 42001.

- **Ключевые навыки:** требования стандарта; подготовка к аудиту этапа 1 или внутреннему.
- **Задачи:** подготовиться к сертификации ISO 42001.
- **Сочетается с:** `claude-skills/ai-act-readiness`, `claude-skills/compliance-os`

### `scientific/analytical-method-validation`

Планирование валидации, верификации и переноса аналитических методик.

- **Ключевые навыки:** ICH Q2/Q14/M10; точность; LOD/LOQ и robustness
- **Задачи:** Подготовить протокол и критерии пригодности методики для заявленной цели.
- **Сочетается с:** `scientific/statistical-analysis`, `scientific/uncertainty-and-units`

### `claude-skills/capa-officer`

CAPA в системе качества медизделий.

- **Ключевые навыки:** анализ первопричин (5 почему, Исикава); планы корректирующих действий; проверка эффективности; метрики CAPA.
- **Задачи:** провести и отследить корректирующие действия.
- **Сочетается с:** `claude-skills/quality-manager-qms-iso13485`, `ecc/quality-nonconformance`

### `claude-skills/cmmc-readiness`

Подготовка оборонного подрядчика к CMMC 2.0 уровня 2.

- **Ключевые навыки:** самооценка; оценка C3PAO; расчёт балла SPRS.
- **Задачи:** подготовиться к сертификации CMMC.
- **Сочетается с:** `claude-skills/compliance-os`

### `claude-skills/compliance-os`

Одновременная работа с несколькими стандартами комплаенса.

- **Ключевые навыки:** выбор применимых стандартов; пересечения контролей; пробный аудит; общий чек-лист доказательств.
- **Задачи:** вести SOC 2, ISO 27001 и другие стандарты одной системой.
- **Сочетается с:** `claude-skills/compliance-readiness`, `claude-skills/aims-audit`

### `claude-skills/compliance-readiness`

Проверка готовности перед добавлением стандарта или планированием годового календаря аудитов.

- **Ключевые навыки:** оценка пробелов; план аудитов.
- **Задачи:** спланировать комплаенс на год.
- **Сочетается с:** `claude-skills/compliance-os`

### `claude-skills/eu-ai-act-specialist`

Специалист по EU AI Act — класс риска, процедура оценки соответствия, техническая документация.

- **Ключевые навыки:** классификация; маршрут по ст. 43; приложение IV.
- **Задачи:** привести ИИ-систему в соответствие с регламентом.
- **Сочетается с:** `claude-skills/ai-act-readiness`, `claude-skills/iso42001-specialist`

### `claude-skills/fda-consultant-specialist`

Консультант по FDA для медизделий.

- **Ключевые навыки:** 510(k), De Novo или PMA; предикаты; QMSR (21 CFR 820); кибербезопасность устройств.
- **Задачи:** выбрать путь регистрации медизделия в США.
- **Сочетается с:** `claude-skills/regulatory-affairs-head`, `claude-skills/fda-qsr-audit-prep`

### `claude-skills/fda-qsr-audit-prep`

Подготовка к инспекции FDA, внутреннему аудиту QMSR или ответу на форму 483.

- **Ключевые навыки:** чек-листы; доказательства; ответы на замечания.
- **Задачи:** пройти инспекцию FDA.
- **Сочетается с:** `claude-skills/fda-consultant-specialist`, `claude-skills/qms-audit-expert`

### `claude-skills/gc-review`

Критика term sheet, договора с клиентом, передачи IP или регуляторных рисков перед подписанием.

- **Ключевые навыки:** позиция главного юриста.
- **Задачи:** проверить документ до подписи.
- **Сочетается с:** `claude-skills/general-counsel-advisor`

### `claude-skills/gdpr-audit-prep`

Подготовка к проверке по GDPR, аудиту после утечки или расследованию регулятора.

- **Ключевые навыки:** чек-лист доказательств; пробелы.
- **Задачи:** пройти проверку GDPR.
- **Сочетается с:** `claude-skills/gdpr-dsgvo-expert`

### `claude-skills/gdpr-dsgvo-expert`

Работа по GDPR — сканирование кода на риски приватности, DPIA, запросы субъектов данных.

- **Ключевые навыки:** оценка воздействия; сроки ответа по ст. 12(3).
- **Задачи:** обеспечить соответствие продукта GDPR.
- **Сочетается с:** `claude-skills/gdpr-audit-prep`, `ecc/healthcare-phi-compliance`

### `claude-skills/general-counsel-advisor`

Юридический советник — договоры и term sheet, стратегия IP, регуляторные риски.

- **Ключевые навыки:** MSA, SaaS, NDA, DPA, трудовые договоры; HIPAA, GDPR, FDA, финтех.
- **Задачи:** проверить договор или оценить правовой риск.
- **Сочетается с:** `claude-skills/gc-review`, `claude-skills/contract-and-proposal-writer`

### `claude-skills/information-security-manager-iso27001`

Построение и ведение СУИБ по ISO 27001 в HealthTech и MedTech.

- **Ключевые навыки:** оценка рисков; внедрение контролей; сертификация.
- **Задачи:** выстроить систему управления информационной безопасностью.
- **Сочетается с:** `claude-skills/isms-audit-expert`, `claude-skills/iso27001-audit-prep`

### `claude-skills/isms-audit-expert`

Аудит по ISO 27001 — внутренний или надзорный, доказательства по Приложению А, SoA, несоответствия.

- **Ключевые навыки:** проведение аудита; классификация замечаний.
- **Задачи:** провести или пройти аудит ISO 27001.
- **Сочетается с:** `claude-skills/information-security-manager-iso27001`, `claude-skills/iso27001-audit-prep`

### `scientific/iso-standards-readiness`

Подготовка свидетельств готовности по ISO 13485, 14971, 17025 и 15189.

- **Ключевые навыки:** контролируемые документы; traceability; CAPA
- **Задачи:** Организовать пакет доказательств, различая сертификацию, аккредитацию и регуляторные решения.
- **Сочетается с:** `claude-skills/quality-manager-qms-iso13485`

### `claude-skills/iso13485-audit-prep`

Подготовка к внутреннему аудиту ISO 13485 или закрытию DHF.

- **Ключевые навыки:** чек-листы; сбор доказательств.
- **Задачи:** пройти аудит системы качества медизделий.
- **Сочетается с:** `claude-skills/qms-audit-expert`, `claude-skills/quality-manager-qms-iso13485`

### `claude-skills/iso27001-audit-prep`

Подготовка к внутреннему, надзорному или первому аудиту ISO 27001.

- **Ключевые навыки:** чек-листы; доказательства.
- **Задачи:** пройти аудит ISO 27001.
- **Сочетается с:** `claude-skills/isms-audit-expert`

### `claude-skills/iso42001-specialist`

Система управления ИИ по ISO/IEC 42001.

- **Ключевые навыки:** анализ разрывов по разделам 4–10; реестр рисков ИИ; контроли Приложения А.
- **Задачи:** внедрить или проверить систему управления ИИ.
- **Сочетается с:** `claude-skills/aims-audit`, `claude-skills/eu-ai-act-specialist`

### `ecc/master-agreement-generator`

Черновики рамочных договоров с контрагентами из шаблона и JSON-спецификации.

- **Ключевые навыки:** подбор пунктов по роли; работа с приложением А.
- **Задачи:** быстро подготовить договор на ревью юристу.
- **Сочетается с:** `ecc/esign-field-placement`

### `claude-skills/mdr-745-specialist`

Работа по EU MDR 2017/745.

- **Ключевые навыки:** классификация по Приложению VIII; техфайл; клиническая оценка; PMS и PSUR.
- **Задачи:** вывести медизделие на рынок ЕС.
- **Сочетается с:** `claude-skills/regulatory-affairs-head`, `claude-skills/risk-management-specialist`

### `claude-skills/qms-audit-expert`

Внутренние аудиты ISO 13485 — программа, проведение, классификация замечаний, подготовка к внешнему.

- **Ключевые навыки:** план аудита; находки.
- **Задачи:** провести внутренний аудит СМК.
- **Сочетается с:** `claude-skills/iso13485-audit-prep`, `claude-skills/quality-manager-qms-iso13485`

### `claude-skills/quality-documentation-manager`

Управление документацией СМК — нумерация, версии, контроль изменений, электронные подписи 21 CFR Part 11.

- **Ключевые навыки:** валидация документов.
- **Задачи:** вести документацию системы качества.
- **Сочетается с:** `claude-skills/quality-manager-qms-iso13485`

### `claude-skills/quality-manager-qmr`

Обязанности представителя руководства по качеству по ISO 13485 п. 5.5.2.

- **Ключевые навыки:** анализ со стороны руководства; политика и цели качества; KPI; стоимость качества.
- **Задачи:** вести анализ СМК руководством.
- **Сочетается с:** `claude-skills/quality-manager-qms-iso13485`

### `claude-skills/quality-manager-qms-iso13485`

Построение и ведение СМК медизделий по ISO 13485.

- **Ключевые навыки:** проектирование; документация; CAPA; подготовка к аудиту.
- **Задачи:** пройти сертификацию ISO 13485.
- **Сочетается с:** `claude-skills/capa-officer`, `claude-skills/qms-audit-expert`

### `ecc/quality-nonconformance`

Контроль качества и управление несоответствиями в регулируемом производстве (FDA 21 CFR 820, IATF 16949, AS9100).

- **Ключевые навыки:** жизненный цикл NCR; 5 почему, Исикава; CAPA; статистический контроль.
- **Задачи:** разобрать несоответствие и провести корректирующие действия.
- **Сочетается с:** `ecc/production-scheduling`, `ecc/returns-reverse-logistics`

### `claude-skills/ra-qm-skills`

Маршрутизатор регуляторных и квалити-навыков — ISO 13485, MDR, FDA, ISO 14971, CAPA, ISO 27001, ISO 42001, EU AI Act, GDPR, SOC 2.

- **Ключевые навыки:** выбор навыка.
- **Задачи:** понять, какой регуляторный навык нужен.
- **Сочетается с:** `claude-skills/regulatory-affairs-head`

### `claude-skills/regulatory-affairs-head`

Стратегия доступа медизделий на рынки — FDA 510(k), De Novo, PMA, CE по MDR, встречи с регулятором.

- **Ключевые навыки:** регуляторная стратегия; ответы на замечания.
- **Задачи:** спланировать регистрацию медизделия.
- **Сочетается с:** `claude-skills/fda-consultant-specialist`, `claude-skills/mdr-745-specialist`

### `claude-skills/risk-management-specialist`

Управление рисками медизделий по ISO 14971.

- **Ключевые навыки:** анализ опасностей; FMEA; деревья отказов; меры контроля; польза–риск.
- **Задачи:** провести анализ рисков устройства.
- **Сочетается с:** `claude-skills/mdr-745-specialist`, `claude-skills/capa-officer`

### `claude-skills/soc2-audit-prep`

Подготовка к аудиту SOC 2 Type II или работа в период наблюдения.

- **Ключевые навыки:** доказательства; чек-листы.
- **Задачи:** пройти аудит SOC 2.
- **Сочетается с:** `claude-skills/soc2-compliance`

### `claude-skills/soc2-compliance`

Подготовка к SOC 2 — критерии доверия, матрица контролей, доказательства, анализ разрывов.

- **Ключевые навыки:** Trust Service Criteria; контроли.
- **Задачи:** выстроить соответствие SOC 2.
- **Сочетается с:** `claude-skills/soc2-audit-prep`, `claude-skills/compliance-os`

---

<a id="cat-operations"></a>
## Операции, логистика и закупки

**Область применения.** Цепочки поставок, логистика, закупки, производство, склад, таможня, энергоснабжение.

**Решаемые задачи.** Планирование спроса и запасов; управление перевозчиками; таможенное оформление; исключения в логистике; возвраты; планирование производства; закупки энергии.

**Типовые связки.** inventory-demand-planning → production-scheduling → carrier-relationship-management → logistics-exception-management → returns-reverse-logistics.

Навыков в категории: 13.

### `claude-skills/business-operations-skills`

Маршрутизатор внутренних операционных задач — процессы, поставщики, мощности, коммуникации, регламенты, закупки.

- **Ключевые навыки:** выбор подходящего BizOps-навыка.
- **Задачи:** понять, какой навык нужен для операционной задачи.
- **Сочетается с:** `claude-skills/capacity-planner`, `claude-skills/coo-advisor`

### `claude-skills/capacity-planner`

Расчёт численности операционной или поддерживающей команды.

- **Ключевые навыки:** модели очередей Erlang C; риск перегрузки; порядок найма.
- **Задачи:** понять, сколько людей нужно в поддержку или операции.
- **Сочетается с:** `claude-skills/coo-advisor`, `claude-skills/chro-advisor`

### `ecc/carrier-relationship-management`

Управление портфелем перевозчиков (FTL, LTL, интермодальные) от отбора до продления контрактов.

- **Ключевые навыки:** проверка перевозчиков; переговоры о ставках и топливных надбавках; тендеры и маршрутные гайды; скоринг перевозчиков.
- **Задачи:** провести тендер на перевозки; оценить и перераспределить объёмы между перевозчиками.
- **Сочетается с:** `ecc/logistics-exception-management`, `ecc/inventory-demand-planning`

### `claude-skills/coo-advisor`

Советник по операционному управлению.

- **Ключевые навыки:** дизайн процессов; исполнение OKR; ритм работы; узкие места; масштабирование.
- **Задачи:** выстроить операционную эффективность.
- **Сочетается с:** `claude-skills/company-os`, `claude-skills/capacity-planner`

### `ecc/customs-trade-compliance`

Таможенное и внешнеторговое соответствие в США, ЕС, Великобритании и Азии.

- **Ключевые навыки:** классификация по ТН ВЭД (HS/HTS); инвойсы и декларации; Инкотермс 2020; соглашения о свободной торговле; проверка санкционных списков.
- **Задачи:** классифицировать товар; подготовить документы для импорта и экспорта; ответить на запрос таможни.
- **Сочетается с:** `ecc/carrier-relationship-management`, `ecc/logistics-exception-management`

### `ecc/energy-procurement`

Закупка электроэнергии и газа для коммерческих и промышленных объектов.

- **Ключевые навыки:** оптимизация тарифов; снижение платы за мощность; тендеры поставщиков; хеджирование; ВИЭ.
- **Задачи:** выбрать тариф и поставщика; снизить затраты на энергию.
- **Сочетается с:** `ecc/inventory-demand-planning`

### `ecc/inventory-demand-planning`

Планирование спроса и запасов для сетевой розницы.

- **Ключевые навыки:** выбор метода прогноза; ABC/XYZ-анализ; страховой запас и точка заказа; промо и сезонность.
- **Задачи:** спрогнозировать спрос и оптимизировать запасы.
- **Сочетается с:** `ecc/production-scheduling`, `ecc/carrier-relationship-management`

### `ecc/logistics-exception-management`

Обработка исключений в грузоперевозках — задержки, повреждения, потери, недостачи, споры.

- **Ключевые навыки:** протоколы эскалации; особенности перевозчиков; претензии.
- **Задачи:** разрулить проблемную поставку.
- **Сочетается с:** `ecc/carrier-relationship-management`, `ecc/returns-reverse-logistics`

### `claude-skills/process-mapper`

Описание сквозного бизнес-процесса и поиск, где работа ждёт.

- **Ключевые навыки:** диаграмма процесса; узкие места; передачи.
- **Задачи:** оптимизировать процесс закупок, онбординга и др.
- **Сочетается с:** `claude-skills/knowledge-ops`, `claude-skills/coo-advisor`

### `claude-skills/procurement-optimizer`

Снижение расходов на ПО и поставщиков.

- **Ключевые навыки:** аудит SaaS-подписок; анализ категорий расходов; консолидация поставщиков.
- **Задачи:** сократить расходы компании.
- **Сочетается с:** `claude-skills/vendor-management`

### `ecc/production-scheduling`

Планирование производства — очередность заказов, балансировка линий, переналадки, узкие места.

- **Ключевые навыки:** дискретное и партионное производство; оптимизация переналадок.
- **Задачи:** составить производственный график и устранить узкое место.
- **Сочетается с:** `ecc/inventory-demand-planning`, `ecc/quality-nonconformance`

### `ecc/returns-reverse-logistics`

Возвраты и обратная логистика.

- **Ключевые навыки:** авторизация возвратов; приёмка и осмотр; решения о дальнейшей судьбе товара; возвраты денег; выявление мошенничества; гарантия.
- **Задачи:** выстроить процесс возвратов.
- **Сочетается с:** `ecc/logistics-exception-management`, `ecc/customer-billing-ops`

### `claude-skills/vendor-management`

Оценка и аудит поставщиков — скоркарды, SLA и компенсации, уровень риска третьих сторон.

- **Ключевые навыки:** ревью ключевых поставщиков.
- **Задачи:** управлять поставщиками.
- **Сочетается с:** `claude-skills/procurement-optimizer`

---

<a id="cat-career"></a>
## Карьера и HR

**Область применения.** Резюме, сопроводительные письма, поиск работы, собеседования, переговоры о зарплате, найм.

**Решаемые задачи.** Проверка резюме под ATS; адаптация резюме под вакансию; сопроводительные письма; анализ соответствия вакансии; подготовка к интервью; переговоры о компенсации.

**Типовые связки.** job-fit-analyzer → resume-customizer → ats-resume-checker → cover-letter-writer → подготовка к интервью → переговоры о зарплате.

Навыков в категории: 20.

### `career/academic-research-cv`

Академическое резюме для исследовательских и преподавательских позиций.

- **Ключевые навыки:** публикации, гранты, преподавание, служение по нормам дисциплины.
- **Задачи:** подготовить CV для научной карьеры.
- **Сочетается с:** `career/cover-letter-writer`, `academic/academic-paper`

### `pm-skills/altitude-horizon-framework`

Переход от PM к директору через мышление «высотой» и «горизонтом».

- **Ключевые навыки:** диагностика масштаба, горизонта и уровня лидерства.
- **Задачи:** понять, чего не хватает для роста до директора.
- **Сочетается с:** `pm-skills/director-readiness-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `career/ats-resume-checker`

Проверка и исправление резюме для систем ATS.

- **Ключевые навыки:** проблемы форматирования; пункты с метриками; ключевые слова вакансии; оценка готовности.
- **Задачи:** чтобы резюме проходило автоматический отбор.
- **Сочетается с:** `career/resume-customizer`, `career/job-fit-analyzer`

### `career/career-pivot-planner`

Пошаговый план смены карьеры.

- **Ключевые навыки:** переносимые навыки; перевод опыта в новую отрасль; история перехода; мосты.
- **Задачи:** сменить профессию или отрасль.
- **Сочетается с:** `career/linkedin-profile-booster`, `career/resume-customizer`

### `claude-skills/chro-advisor`

Стратегия по людям — планы найма, вилки зарплат, оргструктура, производительность, удержание.

- **Ключевые навыки:** кого нанимать; сколько платить; как выстроить структуру.
- **Задачи:** решить кадровые вопросы компании.
- **Сочетается с:** `claude-skills/culture-architect`, `claude-skills/capacity-planner`

### `career/compensation-negotiator`

Переговоры о полном пакете компенсации.

- **Ключевые навыки:** рыночные ставки; письмо с контрпредложением; разбор total comp; сравнение офферов.
- **Задачи:** получить лучшую зарплату и условия.
- **Сочетается с:** `career/mock-interview-coach`

### `career/cover-letter-writer`

Персонализированные сопроводительные письма.

- **Ключевые навыки:** связь опыта с требованиями; цепляющее начало; объяснение пробелов.
- **Задачи:** написать письмо под вакансию.
- **Сочетается с:** `career/resume-customizer`, `career/job-fit-analyzer`

### `pm-skills/director-readiness-advisor`

Переход от PM к директору — подготовка, собеседования, первые месяцы.

- **Ключевые навыки:** практические шаги при росте масштаба.
- **Задачи:** вырасти до директора продукта.
- **Сочетается с:** `pm-skills/altitude-horizon-framework`, `pm-skills/vp-cpo-readiness-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `career/executive-leadership-resume`

Резюме для позиций VP, директора и C-level.

- **Ключевые навыки:** лидерский бренд; истории трансформаций; метрики P&L.
- **Задачи:** подготовить резюме руководителя.
- **Сочетается с:** `career/linkedin-profile-booster`, `pm-skills/vp-cpo-readiness-advisor`

### `pm-skills/executive-onboarding-playbook`

План 30-60-90 дней для нового VP или CPO продукта.

- **Ключевые навыки:** диагностический вход; отказ от преждевременных изменений.
- **Задачи:** успешно начать на руководящей позиции.
- **Сочетается с:** `pm-skills/vp-cpo-readiness-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/interview-system-designer`

Проектирование процесса найма — этапы интервью, матрица компетенций, рубрики, банк вопросов.

- **Ключевые навыки:** калибровка интервьюеров; оценочные рубрики.
- **Задачи:** выстроить честный и эффективный найм.
- **Сочетается с:** `claude-skills/chro-advisor`

### `career/job-fit-analyzer`

Анализ вакансии на соответствие вам.

- **Ключевые навыки:** оценка совпадения; пробелы в навыках; красные флаги; стоит ли откликаться.
- **Задачи:** решить, подаваться ли на вакансию.
- **Сочетается с:** `career/resume-customizer`, `pm-skills/company-research`

### `career/linkedin-profile-booster`

Профиль LinkedIn для рекрутеров.

- **Ключевые навыки:** заголовок; раздел «О себе»; ключевые слова; полнота профиля.
- **Задачи:** чтобы рекрутеры находили вас.
- **Сочетается с:** `claude-skills/linkedin-profile`, `career/career-pivot-planner`

### `claude-skills/linkedin-profile`

Аудит и переписывание профиля LinkedIn.

- **Ключевые навыки:** заголовок; раздел «О себе»; опыт; Featured.
- **Задачи:** сделать профиль сильнее.
- **Сочетается с:** `career/linkedin-profile-booster`, `claude-skills/linkedin-strategy`

### `career/mock-interview-coach`

Тренировочные собеседования с ИИ-коучем.

- **Ключевые навыки:** истории по STAR; поведенческие ответы; «расскажите о себе»; подготовка рекомендателей.
- **Задачи:** подготовиться к собеседованию.
- **Сочетается с:** `pm-skills/product-sense-interview-answer`, `career/compensation-negotiator`

### `career/portfolio-case-study`

Кейсы для портфолио и креативные резюме, совместимые с ATS.

- **Ключевые навыки:** история проекта; результаты до и после.
- **Задачи:** показать работу так, чтобы звали на интервью.
- **Сочетается с:** `career/ats-resume-checker`

### `pm-skills/product-sense-interview-answer`

Структура устного ответа на продуктовом собеседовании.

- **Ключевые навыки:** допущения; сегментация; приоритизация болей; компромиссы MVP.
- **Задачи:** подготовиться к product sense интервью.
- **Сочетается с:** `career/mock-interview-coach`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `career/resume-customizer`

Адаптация резюме под вакансию.

- **Ключевые навыки:** порядок разделов; ключевые слова; версии резюме; оценка совпадения.
- **Задачи:** подогнать резюме под конкретную позицию.
- **Сочетается с:** `career/ats-resume-checker`, `career/cover-letter-writer`

### `career/software-engineer-resume`

Резюме разработчика, которое приводит к собеседованиям.

- **Ключевые навыки:** стек; пункты с метриками; проекты; профиль GitHub.
- **Задачи:** составить сильное резюме инженера.
- **Сочетается с:** `career/ats-resume-checker`, `career/portfolio-case-study`

### `pm-skills/vp-cpo-readiness-advisor`

Переход на позицию VP или CPO — подготовка, собеседования, первые месяцы.

- **Ключевые навыки:** рост исполнительного масштаба.
- **Задачи:** вырасти до руководителя продукта.
- **Сочетается с:** `pm-skills/executive-onboarding-playbook`, `pm-skills/director-readiness-advisor`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

---

<a id="cat-research"></a>
## Исследования и наука

**Область применения.** Глубокие исследования по веб-источникам, академические статьи, обзоры литературы, рецензирование, гранты, патенты, рыночные исследования.

**Решаемые задачи.** Исследование с цитатами; систематический обзор литературы; написание и рецензирование статей; поиск в PubMed и патентных базах; оценка источников.

**Типовые связки.** deep-research (сбор) → literature-review / scholar-evaluation (оценка) → academic-paper (написание) → academic-paper-reviewer (рецензия).

Навыков в категории: 57.

### `academic/academic-paper-reviewer`

Многостороннее рецензирование статьи панелью из пяти ролей.

- **Ключевые навыки:** соответствие журналу; рецензенты по методам и предмету; редакторское решение.
- **Задачи:** получить рецензию до подачи в журнал.
- **Сочетается с:** `academic/academic-paper`, `ecc/scientific-thinking-scholar-evaluation`
- **Лицензия:** CC-BY-NC-4.0 — только некоммерческое использование

### `academic/academic-paper`

Конвейер написания научной статьи из 12 агентов с 11 режимами.

- **Ключевые навыки:** план, структура, ревизия, аннотация, обзор литературы, конвертация формата, проверка цитат.
- **Задачи:** написать или доработать научную статью.
- **Сочетается с:** `academic/academic-paper-reviewer`, `academic/academic-pipeline`
- **Лицензия:** CC-BY-NC-4.0 — только некоммерческое использование

### `academic/academic-pipeline`

Оркестратор полного научного конвейера — исследование, написание, проверка, рецензия, доработки.

- **Ключевые навыки:** этапы с проверками добросовестности.
- **Задачи:** пройти путь от идеи до готовой статьи.
- **Сочетается с:** `academic/deep-research`, `academic/academic-paper`, `academic/academic-paper-reviewer`
- **Лицензия:** CC-BY-NC-4.0 — только некоммерческое использование

### `pm-skills/autonomous-investigation`

Протокол автономного исследования для всех навыков-расследований.

- **Ключевые навыки:** план поиска; метки «факт, вывод, допущение»; уровни уверенности.
- **Задачи:** доверить ИИ исследование без контроля на каждом шаге.
- **Сочетается с:** `pm-skills/company-intel`, `ecc/deep-research`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `scientific/bgpt-paper-search`

Поиск научных работ и извлечение свидетельств через BGPT.

- **Ключевые навыки:** поиск по теме/DOI; эксперименты; provenance
- **Задачи:** Найти детали результатов и ограничения за пределами аннотации.
- **Сочетается с:** `scientific/literature-review`

### `scientific/citation-management`

Поиск и проверка библиографических записей для научных текстов.

- **Ключевые навыки:** DOI/PMID; BibTeX; metadata validation
- **Задачи:** Собрать корректные ссылки без выдуманных реквизитов.
- **Сочетается с:** `scientific/paper-lookup`, `scientific/pyzotero`

### `pm-skills/company-intel`

Исследование компании, отрасли или группы конкурентов через семь аналитических линз.

- **Ключевые навыки:** веб-поиск; структурированная разведка для дальнейших решений.
- **Задачи:** собрать данные о компании или рынке.
- **Сочетается с:** `pm-skills/company-research`, `pm-skills/autonomous-investigation`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/company-research`

Бриф о компании — цитаты руководителей, продуктовая стратегия, оргконтекст.

- **Ключевые навыки:** подготовка к интервью, партнёрству, конкурентному анализу.
- **Задачи:** узнать компанию перед встречей или собеседованием.
- **Сочетается с:** `claude-skills/dossier`, `career/job-fit-analyzer`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `scientific/consciousness-council`

Структурированное сопоставление перспектив для сложных решений.

- **Ключевые навыки:** архетипы рассуждения; допущения; условный синтез
- **Задачи:** Сравнить альтернативы с разделением свидетельств и ценностей.
- **Сочетается с:** `scientific/what-if-oracle`, `scientific/scientific-critical-thinking`

### `marketing/customer-research`

Проведение и синтез исследований клиентов — цитаты, отзывы, обратная связь.

- **Ключевые навыки:** что на самом деле значат отзывы; какие выводы безопасны.
- **Задачи:** понять клиентов по реальным данным.
- **Сочетается с:** `pm-skills/voice-of-customer-miner`, `marketing/product-marketing`

### `academic/deep-research`

Команда из 13 агентов для строгого академического исследования любой темы.

- **Ключевые навыки:** 8 режимов — полное исследование, краткий бриф, разбор статьи и др.
- **Задачи:** провести глубокое исследование с академической строгостью.
- **Сочетается с:** `academic/academic-pipeline`, `ecc/deep-research`
- **Лицензия:** CC-BY-NC-4.0 — только некоммерческое использование

### `ecc/deep-research`

Исследовательские отчёты с цитатами по множеству веб-источников через MCP firecrawl и exa.

- **Ключевые навыки:** план подвопросов; поиск и глубокое чтение; синтез с цитатами и уровнем уверенности.
- **Задачи:** подготовить обоснованный обзор темы.
- **Сочетается с:** `ecc/exa-search`, `ecc/research-ops`, `ecc/market-research`

### `claude-skills/deepread`

Глубокое чтение книги, статьи, PDF или набора документов.

- **Ключевые навыки:** извлечение утверждений и доказательств; карта знаний; обучение по тексту.
- **Задачи:** по-настоящему понять сложный материал.
- **Сочетается с:** `claude-skills/research-summarizer`, `claude-skills/llm-wiki`

### `claude-skills/dossier`

Досье на компанию, человека или организацию для due diligence или подготовки к встрече.

- **Ключевые навыки:** проверка фактов; ключевые сведения; вопросы к встрече.
- **Задачи:** подготовиться к переговорам или проверить контрагента.
- **Сочетается с:** `ecc/osint-investigation`, `ecc/market-research`

### `ecc/exa-search`

Нейропоиск через Exa MCP по вебу, коду, компаниям и людям.

- **Ключевые навыки:** веб-поиск; поиск примеров кода; разведка по компаниям; поиск людей.
- **Задачи:** быстро найти актуальную информацию или примеры для исследования.
- **Сочетается с:** `ecc/deep-research`, `ecc/lead-intelligence`, `ecc/market-research`

### `scientific/exa-search`

Научный и технический веб-поиск через Exa с извлечением страниц.

- **Ключевые навыки:** academic filters; URL/PDF; пакетная выборка
- **Задачи:** Получить актуальные источники и тексты для исследования.
- **Сочетается с:** `scientific/paper-lookup`, `ecc/exa-search`

### `scientific/experimental-design`

Планирование эксперимента до сбора данных.

- **Ключевые навыки:** рандомизация; блокирование; factorial/DOE и репликация
- **Задачи:** Выбрать дизайн, снижающий смешение факторов и псевдорепликацию.
- **Сочетается с:** `scientific/statistical-power`, `scientific/statistical-analysis`

### `claude-skills/grants`

Поиск грантов NIH под исследование.

- **Ключевые навыки:** подбор институтов и секций; объявления о финансировании.
- **Задачи:** найти источник финансирования исследования.
- **Сочетается с:** `claude-skills/litreview`, `academic/academic-pipeline`

### `scientific/hypothesis-generation`

Формулирование научных гипотез и различающих предсказаний по имеющимся фактам.

- **Ключевые навыки:** конкурирующие объяснения; измерения; preregistration
- **Задачи:** Преобразовать наблюдения в проверяемый исследовательский план.
- **Сочетается с:** `scientific/experimental-design`, `scientific/scientific-critical-thinking`

### `pm-skills/intel-discipline-advisor`

Выбор дисциплин разведки, периодичности и навыка для конкурентного или рыночного вопроса.

- **Ключевые навыки:** триаж исследовательских вопросов.
- **Задачи:** понять, как исследовать вопрос.
- **Сочетается с:** `pm-skills/intelligence-collection-disciplines`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `pm-skills/intelligence-collection-disciplines`

Конкурентная разведка по методикам спецслужб — восемь дисциплин от OSINT до MASINT.

- **Ключевые навыки:** цепочки «сигнал–вывод»; слияние источников.
- **Задачи:** провести глубокую конкурентную разведку.
- **Сочетается с:** `pm-skills/intel-discipline-advisor`, `ecc/osint-investigation`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `claude-skills/interview-mapper`

Кодирование транскрипта интервью — клиентского, JTBD, экспертного, юзабилити, выходного.

- **Ключевые навыки:** выдержки с цитатами; темы; инсайты.
- **Задачи:** разобрать интервью на факты и выводы.
- **Сочетается с:** `claude-skills/product-research`, `pm-setup/user-research`

### `scientific/literature-review`

Систематические, scoping и нарративные обзоры литературы.

- **Ключевые навыки:** стратегия поиска; screening; синтез и цитаты
- **Задачи:** Подготовить воспроизводимый обзор с явными границами охвата.
- **Сочетается с:** `scientific/paper-lookup`, `scientific/citation-management`

### `claude-skills/litreview`

Обзор литературы — план поиска (PICO, SPIDER), поиск, отбор и синтез.

- **Ключевые навыки:** выбор фреймворка; стратегии поиска; отбор источников.
- **Задачи:** начать литературный обзор или проект на его основе.
- **Сочетается с:** `ecc/scientific-thinking-literature-review`, `academic/sr-screener`

### `claude-skills/market-research`

Оценка размера рынка TAM, SAM, SOM сверху вниз и снизу вверх, выборки опросов, скоринг сегментов.

- **Ключевые навыки:** расчёт рынка; размер выборки.
- **Задачи:** оценить рынок для бизнес-плана.
- **Сочетается с:** `pm-skills/tam-sam-som-calculator`, `ecc/market-research`

### `ecc/market-research`

Рыночные исследования, конкурентный анализ и due diligence с указанием источников.

- **Ключевые навыки:** анализ рынка и отрасли; сводки для решений.
- **Задачи:** оценить рынок, конкурентов или стартап перед инвестицией.
- **Сочетается с:** `ecc/deep-research`, `ecc/competitive-platform-analysis`, `ecc/investor-materials`

### `claude-skills/meta-research`

Исследование, когда ошибка дорога — стратегия, сравнение продуктов и рынков, проверка гипотезы.

- **Ключевые навыки:** многоисточниковая проверка; оценка достоверности.
- **Задачи:** получить надёжный ответ на важный вопрос.
- **Сочетается с:** `claude-skills/research`, `ecc/deep-research`

### `claude-skills/notebooklm`

Работа с Google NotebookLM — запросы, источники, аудио- и видеообзоры, отчёты, карточки, слайды.

- **Ключевые навыки:** управление блокнотами.
- **Задачи:** использовать NotebookLM для изучения материалов.
- **Сочетается с:** `claude-skills/deepread`

### `ecc/osint-investigation`

Методика OSINT-расследования по скудным зацепкам.

- **Ключевые навыки:** извлечение упущенных следов; связывание разрозненных данных; проверка версий по источникам.
- **Задачи:** собрать картину по человеку, компании или событию из открытых источников.
- **Сочетается с:** `ecc/exa-search`, `ecc/deep-research`

### `scientific/paper-lookup`

Поиск публикаций, препринтов и метаданных через научные API.

- **Ключевые навыки:** PubMed/OpenAlex/Crossref; OA; citation graph
- **Задачи:** Найти источники и получить воспроизводимые идентификаторы и тексты.
- **Сочетается с:** `scientific/citation-management`, `scientific/literature-review`

### `scientific/paperclip`

Поиск и чтение биомедицинских и регуляторных материалов через GXL Paperclip.

- **Ключевые навыки:** full-text grep; metadata SQL; line-pinned citations
- **Задачи:** Извлечь проверяемые свидетельства из публикаций и FDA/PMDA/EMA документов.
- **Сочетается с:** `scientific/literature-review`

### `scientific/paperzilla`

Работа с рекомендациями и проектными лентами Paperzilla через pz CLI.

- **Ключевые навыки:** projects; recommendations; JSON и Atom
- **Задачи:** Получить актуальную подборку работ и проверить карточки источников.
- **Сочетается с:** `scientific/paper-lookup`

### `scientific/parallel-web`

Поиск, извлечение страниц и глубокое исследование через Parallel CLI.

- **Ключевые навыки:** web search; extraction; structured enrichment
- **Задачи:** Собрать текущие веб-свидетельства и проверяемые материалы исследования.
- **Сочетается с:** `scientific/research-lookup`

### `claude-skills/patent`

Патентный поиск — уровень техники, свобода действий, патентный ландшафт, due diligence, споры.

- **Ключевые навыки:** выбор сценария; стратегия поиска; анализ патентов.
- **Задачи:** проверить, можно ли запатентовать или выпускать продукт.
- **Сочетается с:** `ecc/scientific-db-uspto-database`

### `scientific/peer-review`

Конструктивные черновики научных рецензий с привязкой к свидетельствам.

- **Ключевые навыки:** методы и статистика; reproducibility; источники
- **Задачи:** Подготовить структурированную оценку рукописи в разрешённом контексте.
- **Сочетается с:** `scientific/scientific-critical-thinking`, `scientific/scientific-writing`

### `claude-skills/product-research`

Планирование и синтез пользовательских исследований.

- **Ключевые навыки:** выбор метода; число участников; превращение заметок в инсайты.
- **Задачи:** провести исследование пользователей.
- **Сочетается с:** `claude-skills/interview-mapper`, `pm-setup/user-research`

### `claude-skills/pulse`

Что говорят о теме прямо сейчас — Reddit, Hacker News и другие сообщества.

- **Ключевые навыки:** тренды; настроения; жалобы; сравнения инструментов.
- **Задачи:** узнать реальное мнение сообщества.
- **Сочетается с:** `claude-skills/research`, `ecc/exa-search`

### `scientific/research-grants`

Подготовка и проверка исследовательских грантовых заявок.

- **Ключевые навыки:** aims; критерии конкурса; бюджет и resubmission
- **Задачи:** Собрать заявку под конкретный конкурс и проверить полноту требований.
- **Сочетается с:** `scientific/experimental-design`, `scientific/scientific-writing`

### `scientific/research-lookup`

Сбор актуальных научных свидетельств для рукописи или исследовательской записки.

- **Ключевые навыки:** Parallel Search/Extract; competing findings; provenance
- **Задачи:** Подготовить пакет источников под явно заданный исследовательский вопрос.
- **Сочетается с:** `scientific/literature-review`, `scientific/citation-management`

### `claude-skills/research-ops-skills`

Маршрутизатор корпоративных исследований — клинические, финансы R&D, размер рынка, пользователи.

- **Ключевые навыки:** выбор навыка.
- **Задачи:** понять, какой исследовательский навык нужен.
- **Сочетается с:** `claude-skills/clinical-research`, `claude-skills/market-research`

### `ecc/research-ops`

Исследование актуального состояния дел по свежим публичным данным.

- **Ключевые навыки:** сбор фактов; сравнения; обогащение; рекомендации.
- **Задачи:** получить свежие факты и обоснованную рекомендацию.
- **Сочетается с:** `ecc/deep-research`, `ecc/exa-search`

### `claude-skills/research-summarizer`

Сводка научной статьи, отчёта или нескольких источников с цитатами.

- **Ключевые навыки:** структурированный бриф; извлечение цитат.
- **Задачи:** быстро понять суть работы.
- **Сочетается с:** `claude-skills/deepread`, `claude-skills/litreview`

### `claude-skills/research`

Маршрутизатор исследовательских запросов к нужному специалисту.

- **Ключевые навыки:** классификация запроса.
- **Задачи:** исследовать тему, когда неясно, каким навыком.
- **Сочетается с:** `claude-skills/meta-research`, `claude-skills/pulse`

### `scientific/scholar-evaluation`

Развивающая оценка научных работ по прослеживаемым свидетельствам.

- **Ключевые навыки:** качественные рубрики; evidence checks; локальный QC
- **Задачи:** Проверить аргументацию работы без ранжирования людей и кадровых решений.
- **Сочетается с:** `scientific/peer-review`, `scientific/scientific-critical-thinking`

### `scientific/scientific-brainstorming`

Научный поиск идей с явными допущениями и проверкой альтернатив.

- **Ключевые навыки:** независимая генерация; критерии; decision log
- **Задачи:** Сформировать и приоритизировать кандидатные направления исследования.
- **Сочетается с:** `scientific/hypothesis-generation`, `scientific/experimental-design`

### `scientific/scientific-critical-thinking`

Критическая оценка научных утверждений и качества свидетельств.

- **Ключевые навыки:** bias/confounding; GRADE; интерпретация статистики
- **Задачи:** Найти слабые места аргументов и сформулировать ограничения выводов.
- **Сочетается с:** `scientific/peer-review`, `scientific/statistical-analysis`

### `ecc/scientific-db-pubmed-database`

Поиск биомедицинской литературы в PubMed через NCBI E-utilities.

- **Ключевые навыки:** запросы MeSH; поиск по PMID; выгрузка цитат; мониторинг публикаций.
- **Задачи:** найти научные статьи по медицине и биологии.
- **Сочетается с:** `ecc/scientific-thinking-literature-review`, `ecc/deep-research`

### `ecc/scientific-db-uspto-database`

Работа с патентами и товарными знаками USPTO.

- **Ключевые навыки:** PatentSearch; проверки TSDR; данные о передаче прав; журнал исследования.
- **Задачи:** проверить патенты и товарные знаки.
- **Сочетается с:** `ecc/market-research`

### `ecc/scientific-pkg-gget`

Быстрые запросы к геномным базам через gget.

- **Ключевые навыки:** поиск последовательностей; BLAST-поиск; анализ обогащения.
- **Задачи:** собрать биоинформатические данные.
- **Сочетается с:** `ecc/scientific-db-pubmed-database`

### `ecc/scientific-thinking-literature-review`

Систематический обзор литературы.

- **Ключевые навыки:** план поиска; отбор источников; синтез; оформление цитат.
- **Задачи:** подготовить обзор литературы по научной или технической теме.
- **Сочетается с:** `ecc/scientific-thinking-scholar-evaluation`, `ecc/scientific-db-pubmed-database`, `ecc/deep-research`

### `ecc/scientific-thinking-scholar-evaluation`

Структурированная оценка научных работ.

- **Ключевые навыки:** оценка методов; качество доказательств; поддержка цитатами; обратная связь по тексту.
- **Задачи:** отрецензировать статью, заявку или обзор.
- **Сочетается с:** `ecc/scientific-thinking-literature-review`

### `scientific/scientific-writing`

Подготовка научных текстов с проверяемыми фактами и источниками.

- **Ключевые навыки:** reporting guidelines; claim registry; consistency checks
- **Задачи:** Написать или проверить рукопись без выдуманных результатов и ссылок.
- **Сочетается с:** `scientific/citation-management`, `scientific/scientific-visualization`

### `academic/sr-screener`

Отбор исследований для систематических, обзорных и быстрых обзоров по протоколу.

- **Ключевые навыки:** правила включения из протокола или PROSPERO; скрининг.
- **Задачи:** провести отбор статей для систематического обзора.
- **Сочетается с:** `claude-skills/litreview`, `ecc/scientific-thinking-literature-review`
- **Лицензия:** CC-BY-NC-4.0 — только некоммерческое использование

### `claude-skills/syllabus`

Дополнительная литература к учебному курсу.

- **Ключевые навыки:** группировка тем; свежие работы по темам.
- **Задачи:** расширить программу курса.
- **Сочетается с:** `claude-skills/litreview`

### `scientific/venue-templates`

Оформление рукописей, постеров и заявок под требования конкретной площадки.

- **Ключевые навыки:** LaTeX-шаблоны; анонимность; page limits и PDF
- **Задачи:** Проверить актуальные правила и подготовить формат подачи.
- **Сочетается с:** `scientific/scientific-writing`, `scientific/latex-posters`

### `pm-skills/voice-of-customer-miner`

Анализ отзывов, магазинов приложений и форумов — неудовлетворённые потребности и слабости конкурентов.

- **Ключевые навыки:** цитаты как доказательства; триггеры переключения.
- **Задачи:** узнать, чего хотят клиенты, без интервью.
- **Сочетается с:** `marketing/customer-research`, `pm-skills/jobs-to-be-done`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

### `scientific/what-if-oracle`

Сценарный анализ исследовательских планов с явными допущениями. Лицензия навыка — CC BY-NC-SA 4.0.

- **Ключевые навыки:** reference/adverse/wild-card; последствия; decision triggers
- **Задачи:** Проверить устойчивость плана без выдачи сценариев за вероятностный прогноз.
- **Сочетается с:** `scientific/experimental-design`, `scientific/consciousness-council`
- **Лицензия:** CC-BY-NC-SA-4.0 — только некоммерческое использование

---

<a id="cat-productivity"></a>
## Личная продуктивность и коммуникации

**Область применения.** Почта, мессенджеры, календарь, заметки, личная база знаний, еженедельные обзоры, принятие решений.

**Решаемые задачи.** Разбор почты и черновики ответов; планирование недели; глубокая работа; подготовка к встречам; личная база знаний; уведомления.

**Типовые связки.** email-ops / messages-ops (входящие) → планирование (weekly-review) → deep-work → заметки и база знаний.

Навыков в категории: 23.

### `claude-skills/behuman`

Отвечать по-человечески — прямо и тепло, без списков и оговорок.

- **Ключевые навыки:** естественный разговорный стиль.
- **Задачи:** когда ответы звучат слишком роботизированно.
- **Сочетается с:** `claude-skills/content-humanizer`

### `claude-skills/capture`

Разбор хаотичного «выгруза мыслей» в структурированные задачи, идеи и планы.

- **Ключевые навыки:** категоризация; извлечение задач; приоритеты.
- **Задачи:** превратить поток мыслей в понятный план.
- **Сочетается с:** `claude-skills/weekly-review`, `claude-skills/deep-work`

### `claude-skills/caveman`

Сжатый режим ответов — без воды и вежливостей, примерно на 75% меньше токенов.

- **Ключевые навыки:** краткость при сохранении точности.
- **Задачи:** когда нужны короткие экономные ответы.
- **Сочетается с:** `ecc/token-budget-advisor`

### `claude-skills/collab-proof`

Ретроспектива сессии — что сделал Claude, а что вы.

- **Ключевые навыки:** доказательное разделение вклада.
- **Задачи:** оценить вклад ИИ в работу.
- **Сочетается с:** `claude-skills/agent-run-forensics`

### `claude-skills/deep-work`

Планирование дня глубокой работы — тайм-блоки, бюджет поверхностной работы, защита часов фокуса.

- **Ключевые навыки:** блокировка календаря; сокращение мелких задач; отслеживание фокуса.
- **Задачи:** организовать продуктивный день без отвлечений.
- **Сочетается с:** `claude-skills/weekly-review`, `claude-skills/capture`

### `ecc/email-ops`

Разбор почты, черновики, проверка отправки и безопасные follow-up.

- **Ключевые навыки:** сортировка входящих; черновики; верификация отправки.
- **Задачи:** навести порядок в почте; отправить и отследить письма.
- **Сочетается с:** `ecc/messages-ops`, `ecc/brand-voice`, `ecc/unified-notifications-ops`

### `ecc/esign-field-placement`

Детерминированная расстановка полей подписи, даты и текста в веб-конструкторе электронной подписи через браузер.

- **Ключевые навыки:** фиксированная страница подписи; координаты полей; автоматизация браузера.
- **Задачи:** подготовить документ к электронной подписи без ошибок в полях.
- **Сочетается с:** `ecc/master-agreement-generator`, `ecc/browser-qa`

### `claude-skills/google-workspace-cli`

Администрирование и автоматизация Google Workspace через gws CLI.

- **Ключевые навыки:** Gmail, Drive, Sheets, Calendar, Docs, Chat, Tasks; настройка авторизации.
- **Задачи:** автоматизировать работу с Google Workspace из терминала.
- **Сочетается с:** `ecc/google-workspace-ops`

### `ecc/google-workspace-ops`

Работа с Google Drive, Docs, Sheets и Slides как с единым рабочим пространством.

- **Ключевые навыки:** поиск и сводка документов; трекеры; презентации; общие документы.
- **Задачи:** найти, обобщить или обновить материалы в Google Workspace.
- **Сочетается с:** `ecc/knowledge-ops`, `ecc/email-ops`

### `ecc/growth-log`

Записи журнала роста, извлекающие переиспользуемые выводы из выполненной работы.

- **Ключевые навыки:** первопричина; переносимое правило; узнаваемый сигнал.
- **Задачи:** превратить опыт в уроки, а не в дневник событий.
- **Сочетается с:** `ecc/continuous-learning-v2`, `ecc/rules-distill`

### `claude-skills/handoff`

Сжатие текущего разговора в документ передачи для другого агента.

- **Ключевые навыки:** ссылки на PRD, планы, ADR и задачи.
- **Задачи:** передать работу без потери контекста.
- **Сочетается с:** `claude-skills/session-handoff`, `ecc/unified-memory`

### `claude-skills/inbox-setup`

Первичная настройка сортировки почты через интервью о приоритетах.

- **Ключевые навыки:** база знаний для разбора входящих.
- **Задачи:** настроить автоматический разбор почты.
- **Сочетается с:** `claude-skills/inbox-triage`

### `claude-skills/inbox-triage`

Разбор входящих писем по вашей базе приоритетов.

- **Ключевые навыки:** классификация писем; что ответить, что отложить.
- **Задачи:** быстро обработать почту.
- **Сочетается с:** `claude-skills/inbox-setup`, `ecc/email-ops`

### `claude-skills/meeting-analyzer`

Анализ транскриптов встреч — как вы звучите.

- **Ключевые навыки:** доля речи; перебивания; вопросы; стиль общения.
- **Задачи:** улучшить поведение на встречах.
- **Сочетается с:** `claude-skills/meetings`

### `claude-skills/meetings`

Стоит ли собирать встречу, сколько она стоит, повестка с таймбоксами и целью.

- **Ключевые навыки:** цена встречи; повестка; итоги.
- **Задачи:** проводить меньше и лучше встреч.
- **Сочетается с:** `claude-skills/meeting-analyzer`, `claude-skills/deep-work`

### `ecc/messages-ops`

Работа с сообщениями и личными переписками.

- **Ключевые навыки:** чтение SMS и личных сообщений; поиск одноразового кода; просмотр треда перед ответом.
- **Задачи:** найти сообщение или подготовить ответ.
- **Сочетается с:** `ecc/email-ops`, `ecc/unified-notifications-ops`

### `ecc/nutrient-document-processing`

Обработка документов через Nutrient DWS API.

- **Ключевые навыки:** конвертация, OCR, извлечение, редактирование, подпись и заполнение PDF, DOCX, XLSX, PPTX.
- **Задачи:** автоматизировать работу с документами.
- **Сочетается с:** `ecc/esign-field-placement`

### `claude-skills/reflect`

Шаг назад — проверка, на правильном ли пути работа.

- **Ключевые навыки:** сверка с целью; поиск отклонений.
- **Задачи:** когда работа ушла глубоко в детали.
- **Сочетается с:** `claude-skills/weekly-review`, `ecc/agent-self-evaluation`

### `claude-skills/session-handoff`

Документ передачи для новой сессии или другого агента — цель, состояние, решения, следующие шаги.

- **Ключевые навыки:** точное продолжение работы.
- **Задачи:** передать работу без потерь.
- **Сочетается с:** `claude-skills/handoff`, `ecc/ck`

### `claude-skills/swedish-mentor`

Наставник по шведскому языку — путь обучения, видео и подкасты по уровню CEFR.

- **Ключевые навыки:** SFI; Lätt Svenska; подбор материалов.
- **Задачи:** учить шведский системно.
- **Сочетается с:** `claude-skills/capture`

### `ecc/unified-notifications-ops`

Единый процесс уведомлений из GitHub, Linear, десктопа, хуков и мессенджеров.

- **Ключевые навыки:** сведение уведомлений; приоритизация; маршрутизация.
- **Задачи:** перестать тонуть в уведомлениях.
- **Сочетается с:** `ecc/email-ops`, `ecc/messages-ops`

### `ecc/visa-doc-translate`

Перевод изображений документов для визы на английский через OCR с двуязычным PDF.

- **Ключевые навыки:** справки о доходе, работе, выписки; HEIC, PNG, JPG.
- **Задачи:** подготовить перевод документов для визы.
- **Сочетается с:** `ecc/nutrient-document-processing`

### `claude-skills/weekly-review`

Еженедельный обзор — закрыть хвосты, проверить зависшие проекты, вернуть доверие к своей системе.

- **Ключевые навыки:** ревизия задач и обязательств.
- **Задачи:** проводить регулярный недельный обзор.
- **Сочетается с:** `claude-skills/capture`, `claude-skills/deep-work`

---

<a id="cat-media"></a>
## Видео, графика и мультимедиа

**Область применения.** Создание и монтаж видео, анимации, генерация изображений и медиа, презентации, 3D.

**Решаемые задачи.** Программные видео (Remotion, Manim); монтаж; генерация изображений и видео ИИ; слайды; демо-ролики интерфейсов.

**Типовые связки.** сценарий (content-engine) → генерация медиа (fal-ai-media) → видео (remotion-video-creation / manim-video) → монтаж (video-editing).

Навыков в категории: 27.

### `ecc/blender-motion-state-inspection`

Проверка персонажей, ригов, поз и анимации в Blender там, где скриншотов недостаточно.

- **Ключевые навыки:** ретаргетинг анимации; контакт с землёй; направление взгляда; соответствие модели и движения.
- **Задачи:** найти ошибки в 3D-анимации персонажа.
- **Сочетается с:** `ecc/video-editing`

### `claude-skills/demo-video`

Демо-видео, обзор продукта или GIF по скриншотам или описанию сцен.

- **Ключевые навыки:** оркестрация Playwright и монтажа; сценарий показа.
- **Задачи:** сделать видеопрезентацию фичи.
- **Сочетается с:** `ecc/ui-demo`, `ecc/video-editing`

### `ecc/fal-ai-media`

Генерация изображений, видео и аудио через fal.ai MCP.

- **Ключевые навыки:** текст в изображение; текст и изображение в видео (Seedance, Kling, Veo 3); синтез речи.
- **Задачи:** создать визуал, ролик или озвучку для проекта.
- **Сочетается с:** `ecc/video-editing`, `ecc/remotion-video-creation`, `ecc/content-engine`

### `ecc/frontend-slides`

Эффектные HTML-презентации с анимацией с нуля или из файлов PowerPoint.

- **Ключевые навыки:** вёрстка слайдов; анимации; конвертация PPT/PPTX в веб.
- **Задачи:** сделать презентацию для доклада или продукта.
- **Сочетается с:** `ecc/investor-materials`, `ecc/frontend-design-direction`

### `scientific/generate-image`

Генерация и редактирование изображений через OpenRouter Image API.

- **Ключевые навыки:** выбор модели; reference images; запросы и форматы
- **Задачи:** Подготовить иллюстрацию по заданию с проверкой результата.
- **Сочетается с:** `scientific/scientific-schematics`

### `marketing/image`

Создание, генерация, редактирование и оптимизация маркетинговых изображений.

- **Ключевые навыки:** выбор между генерацией, дизайном и фотосъёмкой; обложки блога и соцсетей.
- **Задачи:** сделать визуал для маркетинга.
- **Сочетается с:** `ecc/fal-ai-media`, `marketing/social`

### `scientific/infographics`

Создание инфографики по предоставленным данным через OpenRouter.

- **Ключевые навыки:** макеты; палитры; проверка читаемости
- **Задачи:** Подготовить визуальное объяснение процесса или сравнения.
- **Сочетается с:** `scientific/scientific-visualization`

### `scientific/latex-posters`

Научные постеры в LaTeX с beamerposter, tikzposter или baposter.

- **Ключевые навыки:** колонки; типографика; PDF preflight
- **Задачи:** Сверстать конференционный постер с проверкой итогового PDF.
- **Сочетается с:** `scientific/scientific-visualization`

### `ecc/manim-video`

Анимационные объяснения технических концепций на Manim.

- **Ключевые навыки:** графики; схемы систем; продуктовые демонстрации.
- **Задачи:** сделать обучающее видео об идее или системе.
- **Сочетается с:** `ecc/video-editing`, `ecc/remotion-video-creation`

### `scientific/matplotlib`

Настраиваемые статические научные графики в Matplotlib.

- **Ключевые навыки:** axes/artists; аннотации; экспорт PDF/SVG/PNG
- **Задачи:** Построить точный график и контролировать оформление каждого элемента.
- **Сочетается с:** `scientific/scientific-visualization`

### `claude-skills/md-slides`

Markdown в HTML-презентацию с навигацией с клавиатуры, заметками докладчика и печатью в PDF.

- **Ключевые навыки:** слайды из текста.
- **Задачи:** быстро сделать презентацию из заметок.
- **Сочетается с:** `claude-skills/markdown-html-orchestrator`, `ecc/frontend-slides`

### `scientific/pptx-posters`

Редактируемые научные постеры в PowerPoint без макросов.

- **Ключевые навыки:** физические размеры; печать; доступность и provenance
- **Задачи:** Собрать PPTX-постер из согласованных материалов и проверить пакет.
- **Сочетается с:** `scientific/scientific-visualization`

### `ecc/remotion-video-creation`

Видео на React через Remotion.

- **Ключевые навыки:** 3D; анимации; аудио; субтитры; графики; переходы.
- **Задачи:** собрать видео программно.
- **Сочетается с:** `ecc/video-editing`, `ecc/manim-video`, `ecc/ui-demo`

### `scientific/scientific-schematics`

Черновики научных схем с генерацией и итеративной проверкой качества.

- **Ключевые навыки:** архитектуры; flowcharts; биологические пути
- **Задачи:** Подготовить схему с проверкой подписей и научного содержания.
- **Сочетается с:** `scientific/markdown-mermaid-writing`

### `scientific/scientific-slides`

Презентации научных докладов в PowerPoint или LaTeX Beamer.

- **Ключевые навыки:** структура доклада; тайминг; визуальная проверка
- **Задачи:** Подготовить слайды для конференции, семинара или защиты.
- **Сочетается с:** `scientific/scientific-visualization`, `scientific/scientific-writing`

### `scientific/scientific-visualization`

Достоверные и доступные научные рисунки для публикации.

- **Ключевые навыки:** multi-panel; неопределённость; цвет и экспорт
- **Задачи:** Проверить графическое представление данных и подготовить журнальные файлы.
- **Сочетается с:** `scientific/matplotlib`, `scientific/seaborn`

### `scientific/seaborn`

Статистические графики Seaborn с явной агрегацией данных.

- **Ключевые навыки:** распределения; categorical plots; heatmaps
- **Задачи:** Исследовать отношения и сравнения с корректным отображением неопределённости.
- **Сочетается с:** `scientific/matplotlib`, `scientific/scientific-visualization`

### `ecc/taste-application`

Генерация нового видео по «стилевому паку» и монтаж в готовый ролик.

- **Ключевые навыки:** план кадров по ритму референса; генерация на fal; цветокоррекция; сборка.
- **Задачи:** сделать ролик в стиле референсов.
- **Сочетается с:** `ecc/taste-distillation`, `ecc/fal-ai-media`, `ecc/video-editing`

### `ecc/taste-distillation`

Измерение набора видео-референсов и упаковка их стиля в переиспользуемый пак.

- **Ключевые навыки:** цвет в 3D LUT; ритм монтажа; ключевые кадры; наложения.
- **Задачи:** формализовать стиль, чтобы повторять его.
- **Сочетается с:** `ecc/taste-application`, `ecc/taste`

### `ecc/taste`

Слой креативного направления для музыкальных клипов и коротких видео в эстетике angelcore, cloud-trance, hyperpop.

- **Ключевые навыки:** словарь жанровой эстетики; настроение; визуальные референсы.
- **Задачи:** задать стиль для короткого видео.
- **Сочетается с:** `ecc/taste-distillation`, `ecc/taste-application`, `ecc/tasteforge-video`

### `ecc/tasteforge-video`

Мультимодальная работа с изображениями, видео и 3D-ассетами по файлам — интервью о вкусе, стилевые паки, экспорт EDL/FCPXML.

- **Ключевые навыки:** поиск ассетов; валидация стилевых паков; редактируемые монтажные листы.
- **Задачи:** вести видеопроизводство по стилевым правилам.
- **Сочетается с:** `ecc/taste`, `ecc/taste-distillation`, `ecc/video-editing`

### `ecc/ui-demo`

Запись отполированных демо-видео интерфейса через Playwright.

- **Ключевые навыки:** сценарии демонстрации; запись экрана; туториалы.
- **Задачи:** сделать видео-обзор веб-приложения.
- **Сочетается с:** `ecc/video-editing`, `ecc/remotion-video-creation`

### `claude-skills/video-content-strategist`

Видеостратегия — сценарии, YouTube SEO, короткие форматы (Reels, TikTok, Shorts).

- **Ключевые навыки:** превращение длинного контента в видео.
- **Задачи:** выстроить видеоконтент.
- **Сочетается с:** `marketing/video`, `claude-skills/youtube-full`

### `ecc/video-editing`

Монтаж видео с помощью ИИ — от исходников до готового ролика.

- **Ключевые навыки:** FFmpeg; Remotion; структура ролика; дополнение материалом.
- **Задачи:** смонтировать видео из отснятого материала.
- **Сочетается с:** `ecc/remotion-video-creation`, `ecc/videodb`, `ecc/fal-ai-media`

### `ecc/videodb`

Загрузка, индексация, поиск, монтаж и мониторинг видео и аудио через VideoDB.

- **Ключевые навыки:** индексы речи и сцен; поиск по видео; работа с потоками RTSP.
- **Задачи:** найти нужный момент в видео или смонтировать нарезку.
- **Сочетается с:** `ecc/video-editing`

### `marketing/video`

Создание видео с ИИ или кодом.

- **Ключевые навыки:** выбор подхода — запись экрана, ИИ-аватар, генерация, шаблоны.
- **Задачи:** сделать маркетинговое видео.
- **Сочетается с:** `ecc/remotion-video-creation`, `claude-skills/video-content-strategist`

### `claude-skills/youtube-full`

Работа с YouTube — транскрипты, поиск видео, каналы, плейлисты, мониторинг новых видео.

- **Ключевые навыки:** получение данных по URL, ID или @handle.
- **Задачи:** получить расшифровку или данные канала.
- **Сочетается с:** `claude-skills/video-content-strategist`

---

<a id="cat-network"></a>
## Сети и homelab

**Область применения.** Сетевое оборудование (Cisco), BGP, автоматизация сетей, домашняя лаборатория — VLAN, VPN, DNS.

**Решаемые задачи.** Проверка и валидация конфигураций; диагностика BGP и интерфейсов; автоматизация по SSH; сегментация домашней сети; WireGuard VPN; Pi-hole.

**Типовые связки.** homelab-network-readiness → homelab-network-setup → homelab-vlan-segmentation → homelab-pihole-dns / homelab-wireguard-vpn.

Навыков в категории: 10.

### `ecc/cisco-ios-patterns`

Ревью конфигураций Cisco IOS и IOS-XE.

- **Ключевые навыки:** show-команды; иерархия конфигурации; wildcard-маски; размещение ACL; гигиена интерфейсов; проверка в окне изменений.
- **Задачи:** прочитать, написать или проверить конфиг Cisco; спланировать окно изменений.
- **Сочетается с:** `ecc/network-config-validation`, `ecc/netmiko-ssh-automation`, `ecc/network-interface-health`

### `ecc/homelab-network-readiness`

Чек-лист готовности домашней сети к VLAN, DNS-фильтрации и удалённому доступу.

- **Ключевые навыки:** проверка оборудования; план сегментации; риски.
- **Задачи:** спланировать или проверить домашнюю сеть перед изменениями.
- **Сочетается с:** `ecc/homelab-network-setup`, `ecc/homelab-vlan-segmentation`

### `ecc/homelab-network-setup`

Планирование домашней сети — шлюзы, коммутаторы, точки доступа, IP, DHCP, DNS, кабели.

- **Ключевые навыки:** адресный план; резервирование DHCP; типичные ошибки новичков.
- **Задачи:** построить или переделать домашнюю сеть.
- **Сочетается с:** `ecc/homelab-network-readiness`, `ecc/homelab-pihole-dns`

### `ecc/homelab-pihole-dns`

Pi-hole — установка, блок-листы, DNS-over-HTTPS, локальные записи, устранение проблем.

- **Ключевые навыки:** блокировка рекламы; интеграция с DHCP; диагностика DNS.
- **Задачи:** настроить фильтрацию DNS дома.
- **Сочетается с:** `ecc/homelab-network-setup`, `ecc/homelab-vlan-segmentation`

### `ecc/homelab-vlan-segmentation`

Разделение домашней сети на VLAN для IoT, гостей, доверенных устройств и серверов.

- **Ключевые навыки:** UniFi, pfSense, OPNsense, MikroTik; транки; правила файрвола.
- **Задачи:** изолировать умные устройства и гостей от основной сети.
- **Сочетается с:** `ecc/homelab-network-readiness`, `ecc/homelab-wireguard-vpn`

### `ecc/homelab-wireguard-vpn`

VPN-сервер WireGuard для доступа к домашней сети.

- **Ключевые навыки:** ключи и пиры; раздельное и полное туннелирование; клиенты на телефоне и ноутбуке.
- **Задачи:** получить безопасный удалённый доступ к дому.
- **Сочетается с:** `ecc/homelab-vlan-segmentation`, `ecc/homelab-network-setup`

### `ecc/netmiko-ssh-automation`

Безопасная автоматизация сетевого оборудования на Python и Netmiko.

- **Ключевые навыки:** сбор данных только на чтение; пакетный SSH; парсинг TextFSM; защищённые изменения конфигурации.
- **Задачи:** автоматизировать сбор данных или изменения на множестве устройств.
- **Сочетается с:** `ecc/cisco-ios-patterns`, `ecc/network-config-validation`

### `ecc/network-bgp-diagnostics`

Диагностика BGP без внесения изменений.

- **Ключевые навыки:** состояние соседей; обмен маршрутами; политики префиксов; AS-path.
- **Задачи:** найти причину проблемы с BGP-соседством или маршрутами.
- **Сочетается с:** `ecc/network-interface-health`, `ecc/cisco-ios-patterns`

### `ecc/network-config-validation`

Проверки конфигурации маршрутизаторов и коммутаторов перед применением.

- **Ключевые навыки:** опасные команды; дубли адресов; пересечения подсетей; риски управления.
- **Задачи:** проверить конфиг до выкатки.
- **Сочетается с:** `ecc/cisco-ios-patterns`, `ecc/netmiko-ssh-automation`

### `ecc/network-interface-health`

Диагностика интерфейсов — ошибки, потери, CRC, дуплекс, флаппинг.

- **Ключевые навыки:** анализ счётчиков и трендов на маршрутизаторах, коммутаторах и Linux.
- **Задачи:** выяснить, почему интерфейс работает плохо.
- **Сочетается с:** `ecc/network-bgp-diagnostics`

---

<a id="cat-web3"></a>
## Блокчейн, Web3 и трейдинг

**Область применения.** Смарт-контракты, DeFi, токены, платежи агентов, рынки предсказаний, торговые агенты.

**Решаемые задачи.** Аудит безопасности смарт-контрактов; работа с токенами и десятичностью; платежи ИИ-агентов; исследование рынков предсказаний; риски торговых агентов.

**Типовые связки.** defi-amm-security → evm-token-decimals → llm-trading-agent-security.

Навыков в категории: 8.

### `ecc/agent-payment-x402`

Подключение платежей по протоколу x402 к ИИ-агентам с бюджетами на задачу и некастодиальными кошельками.

- **Ключевые навыки:** бюджеты и лимиты расходов агента; кошельки в сетях Base, X Layer, Solana и EVM; расчёты через фасилитатор.
- **Задачи:** дать агенту возможность самостоятельно платить за API и сервисы под контролем лимитов.
- **Сочетается с:** `ecc/agent-security-hardening`, `ecc/llm-trading-agent-security`

### `ecc/defi-amm-security`

Чек-лист безопасности Solidity-контрактов AMM, пулов ликвидности и свопов.

- **Ключевые навыки:** reentrancy и порядок CEI; атаки донатом и инфляцией; манипуляции оракулами; проскальзывание; права админа.
- **Задачи:** аудит или разработка DeFi-контрактов.
- **Сочетается с:** `ecc/evm-token-decimals`, `ecc/security-review`

### `ecc/evm-token-decimals`

Защита от незаметных ошибок с десятичностью токенов в EVM-сетях.

- **Ключевые навыки:** запрос decimals во время выполнения; кэш с учётом сети; дрейф точности у мостовых токенов; безопасная нормализация.
- **Задачи:** исключить ошибки в суммах у ботов, кошельков и DeFi-приложений.
- **Сочетается с:** `ecc/defi-amm-security`, `ecc/nodejs-keccak256`

### `ecc/ito-baskets`

Чтение данных корзин и рынков предсказаний Itô.

- **Ключевые навыки:** каталог корзин; сравнение с исследованием или вотчлистом.
- **Задачи:** проанализировать корзину рынка предсказаний.
- **Сочетается с:** `ecc/prediction-market-oracle-research`, `ecc/prediction-market-risk-review`

### `ecc/llm-trading-agent-security`

Безопасность автономных торговых агентов с доступом к кошельку.

- **Ключевые навыки:** защита от prompt injection; лимиты трат; симуляция до отправки; circuit breaker; защита от MEV.
- **Задачи:** обезопасить агента, который совершает транзакции.
- **Сочетается с:** `ecc/agent-security-hardening`, `ecc/agent-payment-x402`

### `ecc/nodejs-keccak256`

Защита от ошибок хеширования Ethereum в JS/TS — sha3-256 в Node не равен Keccak-256.

- **Ключевые навыки:** правильные библиотеки хеширования; селекторы и подписи.
- **Задачи:** избежать скрытых ошибок в Ethereum-коде.
- **Сочетается с:** `ecc/evm-token-decimals`

### `ecc/prediction-market-oracle-research`

Исследование рынков предсказаний как источника данных и сигналов.

- **Ключевые навыки:** анализ на первоисточниках; использование в продуктах, агентах и дашбордах.
- **Задачи:** использовать рынки предсказаний для аналитики решений.
- **Сочетается с:** `ecc/prediction-market-risk-review`, `ecc/ito-baskets`

### `ecc/prediction-market-risk-review`

Ревью рисков процессов с рынками предсказаний, оракулами и торговыми агентами.

- **Ключевые навыки:** комплаенс; безопасность; качество данных; приватность; риски исполнения.
- **Задачи:** проверить процесс до запуска.
- **Сочетается с:** `ecc/prediction-market-oracle-research`, `ecc/llm-trading-agent-security`

---

<a id="cat-healthcare"></a>
## Медицина и здравоохранение

**Область применения.** Медицинские информационные системы, клиническая поддержка решений, защита медицинских данных, клинические исследования.

**Решаемые задачи.** Архитектура EMR; системы поддержки клинических решений; соответствие HIPAA и защита PHI; оценка медицинских ИИ-моделей.

**Типовые связки.** healthcare-emr-patterns → healthcare-cdss-patterns → healthcare-phi-compliance / hipaa-compliance → healthcare-eval-harness.

Навыков в категории: 21.

### `scientific/clinical-decision-support`

Подготовка исследовательских материалов оценки клинической поддержки решений.

- **Ключевые навыки:** когорты; survival; biomarker/model и governance
- **Задачи:** Описать и проверить агрегированную исследовательскую оценку без применения к лечению.
- **Сочетается с:** `scientific/scikit-survival`, `scientific/pyhealth`

### `scientific/clinical-reports`

Черновики клинических и исследовательских отчётов по проверенным фактам.

- **Ключевые навыки:** case/trial/safety; manifests; локальные проверки
- **Задачи:** Подготовить структуру отчёта из обезличенных или синтетических данных для экспертной проверки.
- **Сочетается с:** `scientific/scientific-writing`

### `claude-skills/clinical-research`

Дизайн проспективного клинического исследования.

- **Ключевые навыки:** первичные и вторичные конечные точки; размер выборки и мощность; оценка осуществимости.
- **Задачи:** спланировать клиническое исследование.
- **Сочетается с:** `claude-skills/litreview`, `academic/academic-pipeline`

### `scientific/dhdna-profiler`

Исследовательская рубрика DHDNA для анализа рассуждений в предоставленном тексте.

- **Ключевые навыки:** текстовые свидетельства; сравнение паттернов; ограничения оценки
- **Задачи:** Описать особенности текстового образца без психологической диагностики личности.
- **Сочетается с:** `scientific/scientific-critical-thinking`

### `scientific/folklore-variant-evidence`

Получение публичных свидетельств о генах и вариантах через Folklore MCP.

- **Ключевые навыки:** ClinGen; GRCh38 SNV/indel; происхождение источников
- **Задачи:** Собрать ограниченный исследовательский пакет доказательств по публичному варианту.
- **Сочетается с:** `scientific/genomic-coordinates`

### `ecc/healthcare-cdss-patterns`

Разработка систем поддержки клинических решений.

- **Ключевые навыки:** проверка лекарственных взаимодействий; валидация доз; клинические шкалы (NEWS2, qSOFA); классификация алертов.
- **Задачи:** построить модуль клинических подсказок для медицинской системы.
- **Сочетается с:** `ecc/healthcare-emr-patterns`, `ecc/healthcare-eval-harness`

### `ecc/healthcare-emr-patterns`

Разработка электронных медицинских карт (EMR/EHR).

- **Ключевые навыки:** клиническая безопасность; потоки приёма; генерация рецептов; разграничение доступа.
- **Задачи:** спроектировать медицинскую информационную систему.
- **Сочетается с:** `ecc/healthcare-cdss-patterns`, `ecc/healthcare-phi-compliance`

### `ecc/healthcare-eval-harness`

Оценка безопасности пациентов перед выпуском медицинского ПО.

- **Ключевые навыки:** тесты точности CDSS; утечки PHI; целостность клинических процессов.
- **Задачи:** проверить медицинское приложение перед деплоем.
- **Сочетается с:** `ecc/healthcare-cdss-patterns`, `ecc/eval-harness`

### `ecc/healthcare-phi-compliance`

Защита медицинских и персональных данных в приложениях.

- **Ключевые навыки:** классификация данных; доступ на уровне строк; неизменяемый журнал аудита; шифрование.
- **Задачи:** обеспечить соответствие требованиям по PHI и PII.
- **Сочетается с:** `ecc/hipaa-compliance`, `ecc/healthcare-emr-patterns`

### `ecc/hipaa-compliance`

Точка входа для задач по HIPAA — PHI, договоры BAA, утечки.

- **Ключевые навыки:** требования HIPAA; соглашения с подрядчиками; реагирование на утечки.
- **Задачи:** проверить продукт на соответствие HIPAA.
- **Сочетается с:** `ecc/healthcare-phi-compliance`, `ecc/security-review`

### `scientific/imaging-data-commons`

Поиск публичных онкологических изображений NCI Imaging Data Commons.

- **Ключевые навыки:** CT/MR/PET; DICOM; metadata SQL
- **Задачи:** Подобрать набор изображений с проверкой лицензий и происхождения.
- **Сочетается с:** `scientific/pydicom`

### `scientific/ncats-arax`

Ограниченные запросы биомедицинских связей через NCATS Translator ARAX.

- **Ключевые навыки:** Biolink/TRAPI; нормализация сущностей; one/two-hop
- **Задачи:** Получить связи и их источники без подмены причинными или клиническими выводами.
- **Сочетается с:** `scientific/primekg`

### `scientific/neurokit2`

Исследовательская обработка физиологических временных рядов в NeuroKit2.

- **Ключевые навыки:** очистка сигналов; события; вариабельность и сложность
- **Задачи:** Построить воспроизводимый анализ биосигналов с проверкой частоты, единиц и артефактов.
- **Сочетается с:** `scientific/statistical-analysis`, `scientific/uncertainty-and-units`

### `scientific/neuropixels-analysis`

Обработка внеклеточных Neuropixels-записей через SpikeInterface.

- **Ключевые навыки:** SpikeGLX/Open Ephys; Kilosort4; QC и курация
- **Задачи:** Подготовить spike sorting и проверить качество выделенных нейронных единиц.
- **Сочетается с:** `scientific/nwb-conversion`

### `scientific/nwb-conversion`

Конвертация нейрофизиологических данных в Neurodata Without Borders.

- **Ключевые навыки:** NeuroConv/PyNWB; TIFF и position CSV; временная синхронизация
- **Задачи:** Создать проверенный NWB-файл для описанного imaging/behavior процесса; поддержка произвольных форматов не заявлена.
- **Сочетается с:** `scientific/bids`

### `scientific/pkpd-modeling`

Исследовательское фармакокинетическое и фармакодинамическое моделирование.

- **Ключевые навыки:** NCA/popPK; exposure-response; биоэквивалентность
- **Задачи:** Оценить параметры концентрация-время и неопределённость модельных сценариев.
- **Сочетается с:** `scientific/pymc`, `scientific/statistical-analysis`

### `scientific/primekg`

Запросы к зафиксированной версии Precision Medicine Knowledge Graph.

- **Ключевые навыки:** типы узлов; прямые связи; пути и provenance
- **Задачи:** Получить воспроизводимые ассоциации генов, препаратов и заболеваний.
- **Сочетается с:** `scientific/ncats-arax`

### `scientific/pydicom`

Локальная обработка медицинских изображений и метаданных DICOM.

- **Ключевые навыки:** transfer syntax; pixels; частные элементы и обезличивание
- **Задачи:** Проверить или преобразовать DICOM-набор с учётом его структуры.
- **Сочетается с:** `scientific/imaging-data-commons`

### `scientific/pyhealth`

Исследовательские модели клинических данных с PyHealth.

- **Ключевые навыки:** EHR/сигналы; patient-level split; медицинские коды
- **Задачи:** Построить и проверить ML-конвейер с разделением на уровне пациентов.
- **Сочетается с:** `scientific/scikit-survival`, `scientific/shap`

### `scientific/relsa-severity-assessment`

Оценка тяжести состояний лабораторных животных по RELSA.

- **Ключевые навыки:** нормализация; welfare-показатели; интервалы ARIMA
- **Задачи:** Исследовать динамику тяжести и неопределённость прогнозов для экспертной оценки.
- **Сочетается с:** `scientific/statsmodels`

### `scientific/treatment-plans`

Оформление планов лечения по уже принятым и проверенным решениям клиницистов.

- **Ключевые навыки:** источники; цели и checkpoints; согласование документов
- **Задачи:** Проверить структуру и прослеживаемость документа без выбора лечения.
- **Сочетается с:** `scientific/clinical-reports`

---

<a id="cat-bioinformatics"></a>
## Биоинформатика, геномика и исследовательские изображения

**Область применения.** Последовательности, геномные интервалы, bulk и single-cell RNA-seq, микробиом, цитометрия, филогенетика и вычислительная патология.

**Решаемые задачи.** Контроль форматов и координат; подготовка counts; интеграция клеток; анализ путей; проверка сегментации и происхождения данных.

**Типовые связки.** bulk-rnaseq → pydeseq2 → pathway-enrichment; anndata → scanpy → scvi-tools; genomic-coordinates → pysam / polars-bio.

Навыков в категории: 47.

### `scientific/alphagenome`

Исследовательская оценка влияния геномных вариантов с помощью AlphaGenome и Atlas.

- **Ключевые навыки:** регуляторные варианты; AVI и SHAP; сравнение REF/ALT
- **Задачи:** Приоритизировать варианты GRCh38 и сформулировать проверяемые механистические гипотезы.
- **Сочетается с:** `scientific/genomic-coordinates`

### `scientific/anndata`

Хранение и преобразование аннотированных матриц одноклеточных данных AnnData.

- **Ключевые навыки:** h5ad и Zarr; метаданные клеток; совместимость scverse
- **Задачи:** Подготовить согласованную матрицу экспрессии для анализа.
- **Сочетается с:** `scientific/scanpy`, `scientific/scvi-tools`

### `scientific/arboreto`

Построение кандидатных генных регуляторных сетей из данных экспрессии.

- **Ключевые навыки:** GRNBoost2 и GENIE3; ранжирование связей; устойчивость сети
- **Задачи:** Найти предполагаемые связи транскрипционных факторов и генов-мишеней.
- **Сочетается с:** `scientific/scanpy`, `scientific/networkx`

### `scientific/bids`

Организация нейрофизиологических и биомедицинских данных по стандарту BIDS.

- **Ключевые навыки:** метаданные; DICOM-конвертация; валидация структуры
- **Задачи:** Подготовить воспроизводимый набор MRI, EEG, EMG или других поддерживаемых записей.
- **Сочетается с:** `scientific/nwb-conversion`, `scientific/pydicom`

### `scientific/biopython`

Обработка биологических последовательностей и запросы к NCBI через Biopython.

- **Ключевые навыки:** FASTA/GenBank/PDB; BLAST; Bio.Entrez
- **Задачи:** Автоматизировать пакетную обработку последовательностей и получение аннотаций.
- **Сочетается с:** `scientific/gget`, `scientific/bioservices`

### `scientific/bioservices`

Объединение биоинформатических сервисов через единый Python-интерфейс BioServices.

- **Ключевые навыки:** UniProt и KEGG; Reactome; сопоставление идентификаторов
- **Задачи:** Собрать аннотации белков и путей из нескольких баз.
- **Сочетается с:** `scientific/gget`, `scientific/pathway-enrichment`

### `scientific/bulk-rnaseq`

Подготовка bulk RNA-seq от FASTQ и результатов квантификации до генных счётчиков.

- **Ключевые навыки:** STAR/Salmon; nf-core/rnaseq; репликация и QC
- **Задачи:** Собрать проверенную матрицу counts для анализа дифференциальной экспрессии.
- **Сочетается с:** `scientific/nextflow`, `scientific/pydeseq2`

### `scientific/cellprofiler`

Воспроизводимый анализ микроскопических изображений в CellProfiler.

- **Ключевые навыки:** сегментация ядер; интенсивность флуоресценции; контроль качества
- **Задачи:** Построить пакетный конвейер подсчёта клеток и измерения объектов.
- **Сочетается с:** `scientific/scientific-visualization`

### `scientific/cellxgene-census`

Выборка публичных одноклеточных и пространственных данных CZ CELLxGENE Census.

- **Ключевые навыки:** версии Census; метаданные клеток; срезы экспрессии
- **Задачи:** Найти референсный атлас и получить ограниченную выборку данных.
- **Сочетается с:** `scientific/anndata`, `scientific/scanpy`

### `scientific/cobrapy`

Метаболическое моделирование с ограничениями с помощью COBRApy.

- **Ключевые навыки:** FBA/pFBA/FVA; нокауты; проверка SBML
- **Задачи:** Исследовать допустимые потоки и влияние среды или генетических изменений.
- **Сочетается с:** `scientific/13c-metabolic-flux`, `scientific/tellurium`

### `scientific/datalad`

Версионирование научных наборов данных и вычислительного происхождения в DataLad.

- **Ключевые навыки:** git-annex; run/rerun; удалённые хранилища
- **Задачи:** Получить реальные данные вместо указателей и обеспечить повторяемость обработки.
- **Сочетается с:** `scientific/lamindb`

### `scientific/deepspot-m`

Предсказание пространственной экспрессии по гистологическим изображениям с DeepSpot-M. Код и веса имеют некоммерческие ограничения.

- **Ключевые навыки:** H&E-тайлы; масштаб изображения; панели генов
- **Задачи:** Получить исследовательские прогнозы экспрессии и проверить границы их интерпретации.
- **Сочетается с:** `scientific/histolab`, `scientific/scanpy`
- **Лицензия:** PolyForm-Noncommercial-1.0.0 — только некоммерческое использование

### `scientific/deeptools`

Контроль качества и визуализация NGS-данных с deepTools.

- **Ключевые навыки:** BAM/bigWig; PCA и корреляции; профили TSS
- **Задачи:** Построить воспроизводимые профили и тепловые карты RNA-seq, ChIP-seq или ATAC-seq.
- **Сочетается с:** `scientific/pysam`, `scientific/scientific-visualization`

### `scientific/depmap`

Работа с версиями Cancer Dependency Map и зависимостями опухолевых моделей.

- **Ключевые навыки:** CRISPR Chronos; PRISM; идентификаторы моделей
- **Задачи:** Найти кандидатные зависимости и биомаркеры с учётом статистических ограничений.
- **Сочетается с:** `scientific/mageck`, `scientific/pathway-enrichment`

### `scientific/dnanexus-integration`

Разработка и запуск воспроизводимых геномных процессов в DNAnexus.

- **Ключевые навыки:** dx/dxpy; apps/applets; мониторинг и перенос данных
- **Задачи:** Подготовить облачный геномный конвейер и проверить выполнение.
- **Сочетается с:** `scientific/nextflow`

### `scientific/etetoolkit`

Редактирование, сравнение и визуализация готовых филогенетических деревьев в ETE 4.

- **Ключевые навыки:** Newick/Nexus; топологии; таксономия и SmartView
- **Задачи:** Аннотировать дерево и сравнить эволюционные структуры.
- **Сочетается с:** `scientific/phylogenetics`

### `scientific/flowio`

Низкоуровневое чтение и запись файлов проточной цитометрии FCS через FlowIO.

- **Ключевые навыки:** FCS 2.0/3.0/3.1; каналы; NumPy events
- **Задачи:** Проверить метаданные и извлечь события без выполнения gating.
- **Сочетается с:** `scientific/flowkit`

### `scientific/flowkit`

Анализ проточной цитометрии с компенсацией и gating в FlowKit.

- **Ключевые навыки:** spillover; logicle; FlowJo/GatingML
- **Задачи:** Воспроизвести выделение популяций и проверить доли клеток.
- **Сочетается с:** `scientific/flowio`

### `scientific/geniml`

Локальные модели геномных интервалов и планирование Geniml-процессов.

- **Ключевые навыки:** BED-контракты; Region2Vec/scEmbed; совместимость токенизаторов
- **Задачи:** Проверить входные интервалы и подготовить воспроизводимый запуск модели.
- **Сочетается с:** `scientific/gtars`, `scientific/genomic-coordinates`

### `scientific/genomic-coordinates`

Проверка и преобразование геномных координат между форматами и сборками.

- **Ключевые навыки:** BED/GTF/VCF; 0-based и 1-based; нормализация инделов
- **Задачи:** Найти ошибки границ, сборок и имён контигов до анализа.
- **Сочетается с:** `scientific/pysam`, `scientific/polars-bio`

### `scientific/genomic-intelligence`

Запросы к размещённым DNA-моделям Genomic Intelligence.

- **Ключевые навыки:** промоторы и сплайсинг; аннотация генов; прогноз экспрессии
- **Задачи:** Получить исследовательские предсказания по последовательности или области генома.
- **Сочетается с:** `scientific/alphagenome`

### `scientific/gget`

Быстрые геномные запросы через CLI и Python-пакет gget.

- **Ключевые навыки:** BLAST/BLAT; аннотации генов; PDB и обогащение
- **Задачи:** Найти сведения о генах и последовательностях с сохранением источников.
- **Сочетается с:** `scientific/biopython`, `scientific/bioservices`

### `scientific/gtars`

Локальная алгебра геномных интервалов и подготовка наборов BED.

- **Ключевые навыки:** пересечения и покрытие; консенсус; токенизация
- **Задачи:** Проверить интервалы и подготовить данные для моделей и поиска.
- **Сочетается с:** `scientific/genomic-coordinates`, `scientific/polars-bio`

### `scientific/histolab`

Извлечение и подготовка тайлов из полноразмерных гистологических изображений.

- **Ключевые навыки:** маски ткани; сеточные тайлы; нормализация H&E
- **Задачи:** Подготовить набор изображений для вычислительной патологии.
- **Сочетается с:** `scientific/pathml`, `scientific/deepspot-m`

### `scientific/lamindb`

Каталогизация биологических данных и моделей с происхождением в LaminDB.

- **Ключевые навыки:** артефакты и lineage; схемы; онтологии Bionty
- **Задачи:** Организовать проверяемое хранилище исследовательских данных.
- **Сочетается с:** `scientific/ontology-term-resolution`, `scientific/datalad`

### `scientific/latchbio-integration`

Разработка и эксплуатация биоинформатических процессов на Latch.

- **Ключевые навыки:** SDK и CLI; Registry; Nextflow/Snakemake
- **Задачи:** Развернуть конвейер, настроить ресурсы и отслеживать запуски.
- **Сочетается с:** `scientific/nextflow`

### `scientific/mageck`

Анализ пуловых CRISPR-скринингов с MAGeCK.

- **Ключевые навыки:** FASTQ и guide-counts; QC реплик; FDR и эффекты
- **Задачи:** Проверить библиотеку направляющих и ранжировать генные хиты.
- **Сочетается с:** `scientific/depmap`, `scientific/pathway-enrichment`

### `scientific/nextflow`

Создание, запуск и отладка Nextflow DSL2 и nf-core конвейеров.

- **Ключевые навыки:** process/channel; контейнеры; HPC и возобновление
- **Задачи:** Подготовить воспроизводимый pipeline и разобрать сбои выполнения.
- **Сочетается с:** `scientific/bulk-rnaseq`, `scientific/pacsomatic`

### `scientific/onekgpd`

Запросы по участникам и вариантам проекта 1000 Genomes.

- **Ключевые навыки:** GRCh38; носительство вариантов; частоты и аннотации
- **Задачи:** Получить публичные когортные сведения по заданным генам или областям.
- **Сочетается с:** `scientific/genomic-coordinates`

### `scientific/ontology-term-resolution`

Сопоставление научных названий с проверенными онтологическими идентификаторами.

- **Ключевые навыки:** OLS4; CURIE; Bioregistry и ZOOMA
- **Задачи:** Аннотировать ткани, типы клеток, заболевания и методы контролируемыми терминами.
- **Сочетается с:** `scientific/lamindb`

### `scientific/pacsomatic`

Подготовка nf-core/pacsomatic для парных tumor-normal PacBio HiFi данных.

- **Ключевые навыки:** samplesheet; Nextflow; планировщики кластеров
- **Задачи:** Собрать проверенные файлы запуска и диагностировать старт процесса.
- **Сочетается с:** `scientific/nextflow`, `scientific/pysam`

### `scientific/pathml`

Локальные исследовательские процессы вычислительной патологии с PathML.

- **Ключевые навыки:** WSI и тайлы; QC; h5path и пространственные графы
- **Задачи:** Подготовить и проанализировать изображения с ограниченным модельным выводом.
- **Сочетается с:** `scientific/histolab`, `scientific/deepspot-m`

### `scientific/pathogen-variant-surveillance`

Описательный геномный надзор за патогенами через публичные GenSpectrum LAPIS данные.

- **Ключевые навыки:** линии Pango; доли последовательностей; задержки отчётности
- **Задачи:** Оценить изменения в поданных последовательностях без подмены распространённости инфекций.
- **Сочетается с:** `scientific/genomic-coordinates`

### `scientific/pathway-enrichment`

Обогащение биологических путей и генных наборов с явным фоном сравнения.

- **Ключевые навыки:** ORA/GSEA; GO/KEGG/Reactome; FDR
- **Задачи:** Интерпретировать списки генов и ранги с проверкой идентификаторов.
- **Сочетается с:** `scientific/pydeseq2`, `scientific/scanpy`

### `scientific/phylogenetics`

Построение филогенетических деревьев из гомологичных последовательностей.

- **Ключевые навыки:** MAFFT; IQ-TREE; поддержка ветвей
- **Задачи:** Подготовить выравнивание и оценить устойчивость филогенетических выводов.
- **Сочетается с:** `scientific/biopython`, `scientific/etetoolkit`

### `scientific/polars-bio`

Геномные интервальные операции и биоформаты в Polars DataFrame.

- **Ключевые навыки:** overlap/nearest/coverage; BED/VCF/BAM; ленивый ввод
- **Задачи:** Выполнить координатно корректные объединения и анализ покрытия.
- **Сочетается с:** `scientific/polars`, `scientific/genomic-coordinates`

### `scientific/primer-design`

Проектирование и проверка PCR и RT-qPCR праймеров с Primer3.

- **Ключевые навыки:** термодинамика; off-target; координаты и isoforms
- **Задачи:** Подготовить кандидатные праймеры и провести ограниченную in-silico проверку.
- **Сочетается с:** `scientific/biopython`, `scientific/genomic-coordinates`

### `scientific/pydeseq2`

Дифференциальная экспрессия bulk RNA-seq с PyDESeq2.

- **Ключевые навыки:** дизайн и контрасты; Wald-тесты; LFC shrinkage и FDR
- **Задачи:** Получить проверенные результаты по биологическим репликам.
- **Сочетается с:** `scientific/bulk-rnaseq`, `scientific/pathway-enrichment`

### `scientific/pysam`

Чтение, индексирование и преобразование геномных форматов через Python/HTSlib.

- **Ключевые навыки:** SAM/BAM/CRAM; VCF/BCF; pileup и tabix
- **Задачи:** Извлечь покрытие или варианты и проверить соответствие референсу.
- **Сочетается с:** `scientific/genomic-coordinates`, `scientific/polars-bio`

### `scientific/qiime2-amplicon`

Обработка парных 16S-ампликонов в QIIME 2 с сохранением происхождения.

- **Ключевые навыки:** FASTQ-манифесты; ASV; праймеры и таксономия
- **Задачи:** Получить проверенные ампликонные таблицы и оценить удержание чтений.
- **Сочетается с:** `scientific/scikit-bio`, `scientific/waypoint-bio`

### `scientific/relion`

Подготовка и проверка single-particle cryo-EM процессов RELION.

- **Ключевые навыки:** STAR; half sets; маски и FSC
- **Задачи:** Проверить согласованность частиц и численное качество refinement.
- **Сочетается с:** `scientific/scientific-visualization`

### `scientific/scanpy`

Исследовательский анализ single-cell RNA-seq в Scanpy.

- **Ключевые навыки:** QC и нормализация; PCA/UMAP; кластеры и маркеры
- **Задачи:** Подготовить одноклеточный анализ с явным происхождением counts.
- **Сочетается с:** `scientific/anndata`, `scientific/scvi-tools`

### `scientific/scikit-bio`

Биологические последовательности и разнообразие с scikit-bio.

- **Ключевые навыки:** выравнивания; UniFrac; PCoA и PERMANOVA
- **Задачи:** Оценить разнообразие микробиома и структуру биологических выборок.
- **Сочетается с:** `scientific/qiime2-amplicon`, `scientific/phylogenetics`

### `scientific/scvelo`

Анализ RNA velocity по spliced/unspliced счётчикам с scVelo.

- **Ключевые навыки:** кинетические модели; velocity-граф; latent time
- **Задачи:** Проверить направленные гипотезы траекторий без причинных утверждений.
- **Сочетается с:** `scientific/scanpy`, `scientific/anndata`

### `scientific/scvi-tools`

Вероятностные модели одноклеточных и мультимодальных данных в scvi-tools.

- **Ключевые навыки:** scVI/scANVI; totalVI/MultiVI; неопределённость
- **Задачи:** Интегрировать партии, аннотировать клетки и оценить модельные различия.
- **Сочетается с:** `scientific/scanpy`, `scientific/anndata`

### `scientific/tiledbvcf`

Хранение и запросы когортных вариантов с TileDB-VCF.

- **Ключевые навыки:** VCF/BCF ingestion; регионы и образцы; потоковая выборка
- **Задачи:** Организовать расширяемую когорту и получить ограниченные срезы вариантов.
- **Сочетается с:** `scientific/pysam`

### `scientific/waypoint-bio`

Модели микробиома Outpost Bio Waypoint и их воспроизводимая оценка.

- **Ключевые навыки:** эмбеддинги; дообучение; Atlas и Compass
- **Задачи:** Преобразовать таблицы таксонов и проверить модель на задачах микробиома.
- **Сочетается с:** `scientific/qiime2-amplicon`, `scientific/scikit-bio`

---

<a id="cat-chemistry"></a>
## Химия, молекулярное моделирование и белки

**Область применения.** Хемоинформатика, молекулярные признаки, масс-спектрометрия, дизайн белков, docking, динамика и метаболическое моделирование.

**Решаемые задачи.** Подготовка молекул; проверка структур; поиск кандидатных поз; анализ спектров; воспроизводимые расчёты и ограничение интерпретаций.

**Типовые связки.** datamol / rdkit → molfeat → deepchem; diffdock → molecular-dynamics; cobrapy + 13c-metabolic-flux для разных типов потокового анализа.

Навыков в категории: 18.

### `scientific/13c-metabolic-flux`

Оценка метаболических потоков по стационарным углерод-13 изотопным измерениям.

- **Ключевые навыки:** атомные карты; mfapy; многократная оптимизация
- **Задачи:** Проверить, какие потоки ограничены наблюдаемыми изотопными данными.
- **Сочетается с:** `scientific/cobrapy`, `scientific/uncertainty-and-units`

### `scientific/datamol`

Типовые хемоинформатические процессы через упрощённый интерфейс RDKit.

- **Ключевые навыки:** SMILES; дескрипторы; конформеры и кластеризация
- **Задачи:** Подготовить и стандартизировать набор малых молекул.
- **Сочетается с:** `scientific/rdkit`, `scientific/medchem`

### `scientific/deepchem`

Модели молекулярных свойств и бенчмарки MoleculeNet с DeepChem.

- **Ключевые навыки:** фичеризация; scaffold-разбиения; графовые модели
- **Задачи:** Построить проверяемый прогноз ADMET или других химических свойств.
- **Сочетается с:** `scientific/molfeat`, `scientific/pytdc`

### `scientific/diffdock`

Предсказание поз связывания белка и малой молекулы с DiffDock.

- **Ключевые навыки:** PDB/SMILES; пакетный docking; проверка уверенности
- **Задачи:** Получить кандидатные позы без подмены оценки аффинности.
- **Сочетается с:** `scientific/rdkit`, `scientific/molecular-dynamics`

### `scientific/esm`

Белковые модели ESM3, ESMC и ESMFold2 через Biohub esm SDK.

- **Ключевые навыки:** генерация последовательностей; эмбеддинги; фолдинг
- **Задачи:** Подготовить локальный или размещённый вывод с учётом версии модели.
- **Сочетается с:** `scientific/tamarind`

### `scientific/glycoengineering`

Исследование гликозилирования белков с опорой на проверяемые аннотации.

- **Ключевые навыки:** N-гликосайты; S/T-области; гликановое экранирование
- **Задачи:** Подготовить гипотезы инженерии гликопротеинов и проверку сайтов.
- **Сочетается с:** `scientific/biopython`

### `scientific/matchms`

Сравнение масс-спектров и поиск малых молекул по спектральным библиотекам.

- **Ключевые навыки:** очистка метаданных; similarity; сопоставление пиков
- **Задачи:** Подготовить воспроизводимый спектральный поиск и оценить совпадения.
- **Сочетается с:** `scientific/pyopenms`

### `scientific/medchem`

Медицинско-химическая фильтрация кандидатных соединений.

- **Ключевые навыки:** Lipinski/Veber; PAINS и alerts; сложность молекул
- **Задачи:** Отобрать соединения для дальнейшего исследования с явными критериями.
- **Сочетается с:** `scientific/datamol`, `scientific/rdkit`

### `scientific/molecular-dynamics`

Молекулярная динамика и анализ траекторий с OpenMM и MDAnalysis.

- **Ключевые навыки:** силовые поля; минимизация; RMSD/RMSF
- **Задачи:** Подготовить симуляцию и оценить структурную динамику системы.
- **Сочетается с:** `scientific/rdkit`, `scientific/rowan`

### `scientific/molfeat`

Молекулярные признаки для QSAR/QSPR и химического машинного обучения.

- **Ключевые навыки:** ECFP/MACCS; дескрипторы; pretrained embeddings
- **Задачи:** Построить воспроизводимые признаки с корректным соответствием меткам.
- **Сочетается с:** `scientific/rdkit`, `scientific/deepchem`

### `scientific/nmrglue`

Обработка одномерных ЯМР-сигналов с nmrglue.

- **Ключевые навыки:** FID; Фурье-преобразование; фазировка и интегрирование
- **Задачи:** Получить откалиброванный спектр и проверяемые области интеграции.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/pyopenms`

Обработка протеомных и метаболомных масс-спектрометрических данных с pyOpenMS.

- **Ключевые навыки:** детекция признаков; идентификация; количественный анализ
- **Задачи:** Собрать LC-MS/MS-конвейер с проверкой форматов и результатов.
- **Сочетается с:** `scientific/matchms`

### `scientific/pytdc`

Наборы данных и бенчмарки Therapeutics Data Commons через PyTDC.

- **Ключевые навыки:** реестр задач; разбиения; метрики и molecular oracles
- **Задачи:** Сравнить модели на терапевтических задачах без утечки выборок.
- **Сочетается с:** `scientific/deepchem`, `scientific/scikit-learn`

### `scientific/rdkit`

Точное управление молекулярными структурами и реакциями в RDKit.

- **Ключевые навыки:** SMILES/SDF; fingerprints; подструктуры и 3D
- **Задачи:** Реализовать специализированный хемоинформатический процесс.
- **Сочетается с:** `scientific/datamol`, `scientific/medchem`

### `scientific/rowan`

Облачное молекулярное моделирование через Rowan Python API.

- **Ключевые навыки:** pKa; конформеры; docking и cofolding
- **Задачи:** Подготовить пакетный расчёт химических свойств и структур.
- **Сочетается с:** `scientific/rdkit`, `scientific/molecular-dynamics`

### `scientific/tamarind`

Облачный запуск моделей структурной биологии через Tamarind Bio API или MCP.

- **Ключевые навыки:** фолдинг; дизайн белков; docking и динамика
- **Задачи:** Собрать пакетные задания без локальных GPU и проверить результаты.
- **Сочетается с:** `scientific/esm`, `scientific/diffdock`

### `scientific/tellurium`

Кинетические модели биохимических реакций в Tellurium и libRoadRunner.

- **Ключевые навыки:** SBML/Antimony; единицы; SED-ML/COMBINE
- **Задачи:** Смоделировать динамику концентраций и воспроизвести вычислительный эксперимент.
- **Сочетается с:** `scientific/cobrapy`, `scientific/uncertainty-and-units`

### `scientific/torchdrug`

Молекулярные графы и модели поиска лекарств в TorchDrug.

- **Ключевые навыки:** свойства молекул; генерация; белковые представления
- **Задачи:** Подготовить и отладить исследовательский графовый ML-процесс.
- **Сочетается с:** `scientific/torch-geometric`, `scientific/pytdc`

---

<a id="cat-scientific-computing"></a>
## Физика, материалы и научные вычисления

**Область применения.** Символьная математика, квантовые схемы и динамика, гидродинамика, химические реакторы, батареи, фазовые равновесия и астрономия.

**Решаемые задачи.** Выбор модели и solver; проверка единиц; численная сходимость; анализ чувствительности; воспроизводимая симуляция.

**Типовые связки.** uncertainty-and-units → предметный solver → statistical-analysis → scientific-visualization; qiskit / cirq / pennylane выбираются по целевой платформе.

Навыков в категории: 17.

### `scientific/astropy`

Астрономические вычисления и форматы данных в Astropy.

- **Ключевые навыки:** единицы и координаты; FITS; время и WCS
- **Задачи:** Обработать астрономические наблюдения с согласованными физическими величинами.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/cantera`

Моделирование химических реакторов и воспламенения в Cantera.

- **Ключевые навыки:** механизмы реакций; балансы; численная сходимость
- **Задачи:** Оценить задержку воспламенения при заданных физических допущениях.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/cirq`

Квантовые схемы и шумовые модели в Google Cirq.

- **Ключевые навыки:** Google Quantum AI; симуляция; характеризация
- **Задачи:** Подготовить и проверить квантовый эксперимент для целевой платформы.
- **Сочетается с:** `scientific/qiskit`, `scientific/pennylane`

### `scientific/fluidsim`

Планирование и анализ вычислительных гидродинамических симуляций FluidSim.

- **Ключевые навыки:** выбор solver; FFT/MPI; рестарты и диагностика
- **Задачи:** Подготовить ограниченную симуляцию и проверить численную достоверность.
- **Сочетается с:** `scientific/openpiv`, `scientific/get-available-resources`

### `scientific/marine-carbonate-chemistry`

Карбонатная химия морской воды с PyCO2SYS.

- **Ключевые навыки:** щелочность и DIC; pH/pCO2; насыщение минералов
- **Задачи:** Рассчитать параметры карбонатной системы с переносом неопределённости.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/matlab`

Численные вычисления и исследовательские процессы в MATLAB и Octave.

- **Ключевые навыки:** матрицы; визуализация; численные методы
- **Задачи:** Написать или проверить научный код для совместимого MATLAB/Octave окружения.
- **Сочетается с:** `scientific/sympy`

### `scientific/openpiv`

Измерение полей скорости по парам изображений методом PIV.

- **Ключевые навыки:** корреляция окон; фильтрация векторов; завихренность
- **Задачи:** Получить проверенное поле течения из экспериментальных изображений.
- **Сочетается с:** `scientific/fluidsim`, `scientific/uncertainty-and-units`

### `scientific/pennylane`

Дифференцируемые квантовые схемы и гибридные модели в PennyLane.

- **Ключевые навыки:** VQE/QAOA; PyTorch/JAX; симуляторы
- **Задачи:** Проверить вариационный квантовый алгоритм до переноса на оборудование.
- **Сочетается с:** `scientific/qiskit`, `scientific/cirq`

### `scientific/pybamm`

Электрохимические симуляции литий-ионных батарей в PyBaMM.

- **Ключевые навыки:** SPM/DFN; циклы заряда; сеточная сходимость
- **Задачи:** Сравнить расчётные кривые напряжения с измерениями.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/pycalphad`

Расчёт фазовых равновесий CALPHAD с pycalphad.

- **Ключевые навыки:** TDB; фазовые доли; температурные серии
- **Задачи:** Оценить устойчивость фаз сплава с явными составами и условиями.
- **Сочетается с:** `scientific/pymatgen`

### `scientific/pymatgen`

Обработка структур и расчётных свойств материалов в pymatgen.

- **Ключевые навыки:** симметрия; фазовые диаграммы; Materials Project
- **Задачи:** Проверить структуру и подготовить воспроизводимый материаловедческий анализ.
- **Сочетается с:** `scientific/pycalphad`

### `scientific/pymoo`

Одно- и многокритериальная оптимизация с pymoo.

- **Ключевые навыки:** NSGA-II/III; ограничения; Парето-фронт
- **Задачи:** Настроить задачу и проверить качество приближённых решений.
- **Сочетается с:** `scientific/statistical-analysis`

### `scientific/qiskit`

Квантовые схемы и выполнение на IBM Quantum с Qiskit.

- **Ключевые навыки:** транспиляция; Sampler/Estimator; шум и mitigation
- **Задачи:** Подготовить схему, проверить симуляцию и настроить целевое выполнение.
- **Сочетается с:** `scientific/cirq`, `scientific/pennylane`

### `scientific/qutip`

Моделирование открытых и закрытых квантовых систем в QuTiP 5.

- **Ключевые навыки:** траектории; стационарные состояния; спектры
- **Задачи:** Проверить физические размерности и сходимость квантовой динамики.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/simpy`

Дискретно-событийное моделирование процессов и очередей в SimPy.

- **Ключевые навыки:** ресурсы; прерывания; независимые репликации
- **Задачи:** Построить воспроизводимую симуляцию и оценить её выходные показатели.
- **Сочетается с:** `scientific/statistical-analysis`

### `scientific/sympy`

Точная символьная математика в SymPy.

- **Ключевые навыки:** алгебра; анализ; уравнения и LaTeX
- **Задачи:** Получить символьное решение с явными предположениями.
- **Сочетается с:** `scientific/uncertainty-and-units`

### `scientific/uncertainty-and-units`

Контроль физических единиц и перенос неопределённости измерений.

- **Ключевые навыки:** pint/uncertainties; GUM; Монте-Карло
- **Задачи:** Проверить размерности, бюджет неопределённости и физическую правдоподобность результата.
- **Сочетается с:** `scientific/statistical-analysis`

---

<a id="cat-lab-automation"></a>
## Лабораторная автоматизация и оборудование

**Область применения.** ELN и реестры образцов, роботизированное дозирование, облачные лаборатории, параметрические лабораторные детали и изготовление.

**Решаемые задачи.** Интеграция метаданных; подготовка протоколов и симуляция; проектирование деталей; проверка входов, стоимости и разрешённого действия перед запуском или заказом.

**Типовые связки.** lab-hardware-cad → fictiv; experimental-design → protocolsio-integration → opentrons-integration / pylabrobot; benchling-integration → lamindb.

Навыков в категории: 10.

### `scientific/adaptyv`

Планирование белковых экспериментов через Adaptyv Foundry API и SDK.

- **Ключевые навыки:** ассеи; оценка стоимости; задания и результаты
- **Задачи:** Подготовить последовательности и контролировать лабораторный заказ в рамках разрешённого действия.
- **Сочетается с:** `scientific/esm`

### `scientific/benchling-integration`

Автоматизация лабораторных данных через Benchling SDK и REST API.

- **Ключевые навыки:** Registry; Inventory; ELN и Workflows
- **Задачи:** Связать записи и образцы в проверяемом лабораторном процессе.
- **Сочетается с:** `scientific/lamindb`

### `scientific/fictiv`

Работа с платформой изготовления деталей Fictiv в браузере.

- **Ключевые навыки:** CAD-загрузка; DFM; материалы и допуски
- **Задачи:** Подготовить конфигурацию изготовления, смету или проверку статуса заказа.
- **Сочетается с:** `scientific/lab-hardware-cad`

### `scientific/ginkgo-cloud-lab`

Подготовка и заказ поддерживаемых экспериментов Ginkgo Cloud Lab.

- **Ключевые навыки:** экспрессия белков; SPR; оценка входов и цены
- **Задачи:** Выбрать протокол и подготовить проверяемый план лабораторной услуги.
- **Сочетается с:** `scientific/adaptyv`

### `scientific/lab-hardware-cad`

Параметрическое проектирование лабораторных деталей с build123d.

- **Ключевые навыки:** держатели и адаптеры; STEP/STL/DXF; сопряжения
- **Задачи:** Подготовить геометрию для печати, CNC или лазерной обработки.
- **Сочетается с:** `scientific/fictiv`

### `scientific/labarchive-integration`

Интеграция с официальными API LabArchives ELN и Inventory.

- **Ключевые навыки:** региональные endpoint; подписанные запросы; UID
- **Задачи:** Подготовить авторизованный обмен лабораторными записями.
- **Сочетается с:** `scientific/benchling-integration`

### `scientific/omero-integration`

Управление исследовательскими изображениями и метаданными через OMERO.

- **Ключевые навыки:** поиск изображений; ROI; импорт и экспорт
- **Задачи:** Подготовить ограниченную выборку изображений или проверенный план записи.
- **Сочетается с:** `scientific/histolab`

### `scientific/opentrons-integration`

Подготовка протоколов Opentrons Python Protocol API v2 для Flex и OT-2.

- **Ключевые навыки:** labware и deck; пипетки; симуляция
- **Задачи:** Написать, проверить или мигрировать протокол дозирования.
- **Сочетается с:** `scientific/pylabrobot`

### `scientific/protocolsio-integration`

Чтение и проверка конкретных версий протоколов protocols.io.

- **Ключевые навыки:** REST/MCP; экспорт; планы изменений
- **Задачи:** Получить прослеживаемую копию протокола без неявного выполнения изменений.
- **Сочетается с:** `scientific/experimental-design`

### `scientific/pylabrobot`

Подготовка и проверка автоматизации лабораторного оборудования с PyLabRobot.

- **Ключевые навыки:** ресурсы; жидкостные планы; офлайн-симуляция
- **Задачи:** Составить протокол для поддерживаемых устройств с операторской проверкой перед физическим запуском.
- **Сочетается с:** `scientific/opentrons-integration`
