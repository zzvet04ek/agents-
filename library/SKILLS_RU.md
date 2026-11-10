# Навыки библиотеки — описание по категориям

Генерируется `library/tools/library.py index` из `library/ru/`. Правьте описания в `library/ru/skills/*.yaml`, не здесь.

Описано навыков: **314** из 856. Без описания: 542 (см. конец файла).

Для каждого навыка: суть, ключевые навыки, решаемые задачи и с чем сочетать. Идентификатор `коллекция/имя` можно назвать Claude напрямую: «возьми навык marketing/copywriting».

## Содержание

| Категория | Навыков |
|---|---|
| [Backend-разработка, языки и фреймворки](#cat-dev-backend) | 28 |
| [Frontend, UI и дизайн интерфейсов](#cat-dev-frontend) | 17 |
| [Мобильная и десктопная разработка](#cat-dev-mobile) | 12 |
| [Тестирование и контроль качества кода](#cat-testing) | 32 |
| [Безопасность](#cat-security) | 11 |
| [DevOps, инфраструктура, деплой и мониторинг](#cat-devops) | 13 |
| [Базы данных, данные и аналитика](#cat-data) | 11 |
| [AI, LLM и агентные системы](#cat-ai-agents) | 40 |
| [Архитектура, планирование и процесс разработки](#cat-eng-process) | 27 |
| [Настройка Claude Code и экосистемы ECC](#cat-claude-setup) | 27 |
| [Документация и управление знаниями](#cat-docs) | 7 |
| [Контент, тексты и бренд](#cat-content) | 8 |
| [Маркетинг, SEO и рост](#cat-marketing) | 2 |
| [Продажи, клиенты и поддержка](#cat-sales) | 2 |
| [Продакт-менеджмент](#cat-product) | 2 |
| [Управление проектами и командами](#cat-project) | 3 |
| [Стратегия бизнеса и C-level](#cat-strategy) | 6 |
| [Финансы, биллинг и инвестиции](#cat-finance) | 4 |
| [Регуляторика, комплаенс и качество (QMS)](#cat-compliance) | 2 |
| [Операции, логистика и закупки](#cat-operations) | 7 |
| [Исследования и наука](#cat-research) | 10 |
| [Личная продуктивность и коммуникации](#cat-productivity) | 8 |
| [Видео, графика и мультимедиа](#cat-media) | 12 |
| [Сети и homelab](#cat-network) | 10 |
| [Блокчейн, Web3 и трейдинг](#cat-web3) | 8 |
| [Медицина и здравоохранение](#cat-healthcare) | 5 |

---

<a id="cat-dev-backend"></a>
## Backend-разработка, языки и фреймворки

**Область применения.** Серверная логика, API и бизнес-код на Python, Node.js/TypeScript, Go, Rust, Java/Kotlin, C#, C++, PHP, Ruby, Perl и их фреймворках (Django, FastAPI, Spring Boot, Quarkus, Laravel, Rails, NestJS, Ktor).

**Решаемые задачи.** Написание идиоматичного кода по стандартам языка; проектирование REST/GraphQL API; работа с ORM; фоновые задачи; обработка ошибок; ревью кода и рефакторинг.

**Типовые связки.** *-patterns (как писать) → *-tdd / *-testing (тесты сначала) → *-security (защита) → *-verification (финальная проверка перед релизом); api-design + contract-first для согласования интерфейсов.

Навыков в категории: 28.

### `ecc/api-connector-builder`

Добавление нового API-коннектора или провайдера строго по образцу уже существующих интеграций проекта.

- **Ключевые навыки:** анализ существующего паттерна интеграций; повторение структуры без второй архитектуры.
- **Задачи:** подключить ещё один внешний сервис так же, как подключены остальные.
- **Сочетается с:** `ecc/api-design`, `ecc/error-handling`, `ecc/contract-first`

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

Навыков в категории: 17.

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

### `ecc/design-system`

Создание дизайн-системы из существующего кода или аудит визуальной согласованности.

- **Ключевые навыки:** извлечение токенов (цвета, типографика, отступы, тени); CSS-переменные; документация дизайн-системы.
- **Задачи:** навести порядок в стилях; задокументировать визуальный язык.
- **Сочетается с:** `ecc/frontend-design-direction`, `ecc/accessibility`, `ecc/make-interfaces-feel-better`

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

Навыков в категории: 12.

### `ecc/android-clean-architecture`

Clean Architecture для Android и Kotlin Multiplatform — модули, правила зависимостей, UseCase, репозитории, слой данных.

- **Ключевые навыки:** модульная структура; направление зависимостей; UseCase и Repository; организация слоя данных.
- **Задачи:** спроектировать или навести порядок в архитектуре Android/KMP-проекта.
- **Сочетается с:** `ecc/kotlin-patterns`, `ecc/compose-multiplatform-patterns`, `ecc/kotlin-coroutines-flows`

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

Навыков в категории: 32.

### `ecc/ai-regression-testing`

Регрессионное тестирование при ИИ-разработке — тесты API в песочнице без БД и ловушки для «слепых зон» модели.

- **Ключевые навыки:** sandbox-тесты API; автоматические проверки на баги; защита от ситуации, когда одна модель пишет и ревьюит код.
- **Задачи:** покрыть регрессиями код, написанный ИИ; проверить изменения, которые ревьюила та же модель.
- **Сочетается с:** `ecc/tdd-workflow`, `ecc/verification-loop`, `ecc/ai-first-engineering`

### `ecc/browser-qa`

Автоматическая проверка UI после деплоя через браузер — ошибки консоли, Web Vitals, формы, визуальная регрессия, доступность.

- **Ключевые навыки:** smoke-проверки; тесты форм и авторизации; скриншоты на трёх брейкпоинтах; аудит axe-core; вердикт SHIP/DO-NOT-SHIP.
- **Задачи:** проверить фичу на стейдже; оценить фронтенд-PR перед релизом.
- **Сочетается с:** `ecc/e2e-testing`, `ecc/canary-watch`, `ecc/accessibility`

### `ecc/click-path-audit`

Трассировка каждой кнопки интерфейса через всю цепочку изменений состояния.

- **Ключевые навыки:** поиск функций, которые по отдельности работают, но гасят друг друга; проверка итогового состояния UI.
- **Задачи:** найти баги, когда пользователи жалуются на кнопки, а отладка ничего не нашла; проверка после рефакторинга состояния.
- **Сочетается с:** `ecc/browser-qa`, `ecc/e2e-testing`, `ecc/react-testing`

### `ecc/codehealth-mcp`

Оценка структурного здоровья кода в реальном времени через CodeScene MCP.

- **Ключевые навыки:** ревью до правок; дельта оценки после изменений; гейты для коммитов и PR.
- **Задачи:** проверить, не ухудшил ли ИИ файл; рефакторинг с контролем качества.
- **Сочетается с:** `ecc/plankton-code-quality`, `ecc/coding-standards`

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

### `ecc/fsharp-testing`

Тестирование на F#.

- **Ключевые навыки:** xUnit, FsUnit, Unquote; property-based тесты на FsCheck; интеграционные тесты.
- **Задачи:** писать тесты F#-проекта.
- **Сочетается с:** `ecc/dotnet-patterns`, `ecc/csharp-testing`

### `ecc/gateguard`

Хук, который блокирует первую попытку правки или команды, пока агент не приведёт конкретные факты о коде.

- **Ключевые навыки:** принуждение к исследованию перед правкой; проверка импортов и потоков данных.
- **Задачи:** снизить число «слепых» правок агента.
- **Сочетается с:** `ecc/delivery-gate`, `ecc/search-first`, `ecc/hookify-rules`

### `ecc/golang-testing`

Тестирование на Go по TDD.

- **Ключевые навыки:** табличные тесты; подтесты; бенчмарки; фаззинг; покрытие.
- **Задачи:** писать тесты Go-проекта.
- **Сочетается с:** `ecc/golang-patterns`, `ecc/tdd-workflow`

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

### `ecc/module-regression`

Контроль межмодульных регрессий через реестр REGRESSION.md.

- **Ключевые навыки:** потребители каждого модуля; команды приёмки; прогон после изменений.
- **Задачи:** не сломать соседние модули в большом репозитории.
- **Сочетается с:** `ecc/module-governance`, `ecc/change-impact`

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

Навыков в категории: 11.

### `ecc/agent-security-hardening`

Защита агентных систем, которые обрабатывают недоверенный контент, вызывают инструменты, пишут файлы и работают с секретами.

- **Ключевые навыки:** защита от prompt injection; изоляция инструментов; обращение с учётными данными; мультиарендная изоляция; безопасная память агента.
- **Задачи:** ревью безопасности агентного рантайма, шлюза инструментов или сервиса памяти.
- **Сочетается с:** `ecc/safety-guard`, `ecc/mcp-dependency-review`, `ecc/security-review`

### `ecc/django-security`

Безопасность Django — аутентификация, авторизация, CSRF, SQL-инъекции, XSS, безопасный деплой.

- **Ключевые навыки:** настройки безопасности; права доступа; защита от инъекций.
- **Задачи:** ревью безопасности Django-проекта.
- **Сочетается с:** `ecc/django-patterns`, `ecc/security-review`, `ecc/django-verification`

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

### `ecc/safety-guard`

Защита от разрушительных операций агента.

- **Ключевые навыки:** перехват опасных команд (rm -rf, push --force, DROP TABLE); заморозка путей; режимы защиты.
- **Задачи:** работать с агентом на важных системах без риска потерь.
- **Сочетается с:** `ecc/hookify-rules`, `ecc/agent-security-hardening`

### `ecc/security-bounty-hunter`

Поиск эксплуатируемых уязвимостей уровня баг-баунти в репозиториях.

- **Ключевые навыки:** удалённо достижимые уязвимости; отсев шума; подготовка отчёта.
- **Задачи:** найти реальные уязвимости для отчёта.
- **Сочетается с:** `ecc/security-review`, `ecc/security-scan`

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

### `ecc/springboot-security`

Spring Security.

- **Ключевые навыки:** аутентификация и авторизация; валидация; CSRF; секреты; заголовки; rate limiting.
- **Задачи:** защитить Spring Boot-сервис.
- **Сочетается с:** `ecc/springboot-patterns`, `ecc/security-review`

---

<a id="cat-devops"></a>
## DevOps, инфраструктура, деплой и мониторинг

**Область применения.** CI/CD, Docker, Kubernetes, облака (AWS, GCP, Azure), Terraform, наблюдаемость, инциденты, производительность в проде.

**Решаемые задачи.** Настройка пайплайнов и деплоя; контейнеризация; дашборды и алерты; мониторинг после релиза; разбор инцидентов; оптимизация затрат на облако.

**Типовые связки.** docker-patterns → deployment-patterns / kubernetes-patterns → canary-watch после релиза → dashboard-builder для мониторинга → incident-разбор при сбоях.

Навыков в категории: 13.

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

### `ecc/docker-patterns`

Docker и Docker Compose — локальная разработка, безопасность контейнеров, сети, тома, многосервисные стеки.

- **Ключевые навыки:** Dockerfile; compose; харднинг; сети и тома.
- **Задачи:** создать или отревьюить Docker-конфигурацию.
- **Сочетается с:** `ecc/deployment-patterns`, `ecc/kubernetes-patterns`, `ecc/security-scan`

### `ecc/flox-environments`

Воспроизводимые кроссплатформенные окружения разработки на Flox (на базе Nix).

- **Ключевые навыки:** декларативные окружения; тулчейны проекта; одинаковая среда на macOS и Linux.
- **Задачи:** настроить окружение проекта, которое одинаково работает у всех.
- **Сочетается с:** `ecc/docker-patterns`

### `ecc/github-ops`

Операции с репозиториями GitHub через gh CLI.

- **Ключевые навыки:** разбор issues; управление PR; CI/CD; релизы; мониторинг безопасности.
- **Задачи:** автоматизировать рутину по GitHub-репозиторию.
- **Сочетается с:** `ecc/git-workflow`, `ecc/issue-review`, `ecc/deployment-patterns`

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

### `ecc/production-audit`

Аудит готовности к продакшену по локальным данным без отправки кода наружу.

- **Ключевые навыки:** «что сломается в проде»; проверка перед запуском и после мержа.
- **Задачи:** оценить, готово ли приложение к реальным пользователям.
- **Сочетается с:** `ecc/security-review`, `ecc/deployment-patterns`, `ecc/canary-watch`

### `ecc/terminal-ops`

Исполнение задач в репозитории с доказательствами — запуск команд, проверки, отладка CI, точечные исправления.

- **Ключевые навыки:** точные команды; фиксация результатов; узкие правки.
- **Задачи:** проверить репозиторий или разобрать падение CI.
- **Сочетается с:** `ecc/github-ops`, `ecc/verification-loop`

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

Навыков в категории: 11.

### `ecc/clickhouse-io`

ClickHouse для высоконагруженной аналитики — схемы, оптимизация запросов, инженерия данных.

- **Ключевые навыки:** движки таблиц; партиционирование; оптимизация медленных аналитических запросов.
- **Задачи:** спроектировать схему или ускорить аналитический запрос в ClickHouse.
- **Сочетается с:** `ecc/data-throughput-accelerator`, `ecc/dashboard-builder`

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

### `ecc/database-migrations`

Безопасные обратимые миграции БД без простоя.

- **Ключевые навыки:** expand-contract; конкурентные индексы; пакетные бэкфиллы; инструменты PostgreSQL, Prisma и др.
- **Задачи:** провести миграцию на продакшене без остановки сервиса.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/change-impact`, `ecc/prisma-patterns`

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

### `ecc/redis-patterns`

Redis в продакшене.

- **Ключевые навыки:** структуры данных; стратегии кэширования; распределённые блокировки; rate limiting; pub/sub.
- **Задачи:** добавить кэш, очереди или блокировки на Redis.
- **Сочетается с:** `ecc/postgres-patterns`, `ecc/django-celery`

---

<a id="cat-ai-agents"></a>
## AI, LLM и агентные системы

**Область применения.** Проектирование ИИ-агентов, мультиагентных систем, автономных циклов, RAG, промптов; оценка и стоимость LLM; ML-пайплайны.

**Решаемые задачи.** Построение агента и набора инструментов; оркестрация нескольких агентов; оценка качества (eval); снижение стоимости токенов; память агента; отладка сбоев агента.

**Типовые связки.** agent-harness-construction (инструменты агента) → autonomous-agent-harness / continuous-agent-loop (цикл) → eval-harness / agent-eval (оценка) → cost-aware-llm-pipeline (стоимость) → agent-security-hardening (защита).

Навыков в категории: 40.

### `ecc/agent-architecture-audit`

Полная диагностика ИИ-агентов и LLM-приложений по 12 слоям стека с ранжированием проблем по критичности.

- **Ключевые навыки:** поиск регрессий обёрток; загрязнение памяти агента; нарушения дисциплины инструментов; скрытые циклы самоисправления; искажения при выводе.
- **Задачи:** найти слой, в котором ломается агент; аудит агента перед выпуском; список исправлений в коде.
- **Сочетается с:** `ecc/agent-introspection-debugging`, `ecc/eval-harness`, `ecc/agent-security-hardening`

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

### `ecc/agent-introspection-debugging`

Структурированная самодиагностика сбоев ИИ-агента — фиксация, диагноз, ограниченное восстановление и отчёт.

- **Ключевые навыки:** сбор контекста сбоя; гипотезы о причине; безопасный повторный запуск; отчёт с выводами.
- **Задачи:** разобрать неудачный запуск агента воспроизводимо, а не простым повтором.
- **Сочетается с:** `ecc/agent-architecture-audit`, `ecc/continuous-agent-loop`

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

### `ecc/bengali-nlp`

Обработка текста на бенгальском языке для ИИ-приложений.

- **Ключевые навыки:** нормализация Unicode; определение письменности; токенизация; лигатуры.
- **Задачи:** подготовить бенгальские тексты для NLP и LLM.
- **Сочетается с:** `ecc/regex-vs-llm-structured-text`

### `ecc/claude-devfleet`

Оркестрация параллельных кодовых агентов через Claude DevFleet в изолированных worktree.

- **Ключевые навыки:** планирование проекта; запуск агентов; мониторинг прогресса; структурированные отчёты.
- **Задачи:** распараллелить разработку между несколькими агентами.
- **Сочетается с:** `ecc/dmux-workflows`, `ecc/team-agent-orchestration`, `ecc/blueprint`

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

### `ecc/gan-style-harness`

Обвязка «генератор–оценщик» по мотивам GAN для автономного создания качественных приложений.

- **Ключевые навыки:** агент-генератор и агент-критик; итерации до прохождения оценки.
- **Задачи:** собрать фичу, где важна высокая планка качества, без постоянного участия человека.
- **Сочетается с:** `ecc/eval-harness`, `ecc/santa-method`, `ecc/continuous-agent-loop`

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

### `ecc/loop-design-check`

Проектирование или ревью целевого цикла агента на типичные сбои.

- **Ключевые навыки:** зацикливание; «обман» проверяющего; доведение неверного ответа до конца; машинно-проверяемые критерии остановки.
- **Задачи:** убедиться, что агентный цикл сходится к правильному результату.
- **Сочетается с:** `ecc/continuous-agent-loop`, `ecc/eval-harness`

### `ecc/mcp-server-patterns`

Создание MCP-серверов на Node/TypeScript SDK.

- **Ключевые навыки:** инструменты, ресурсы, промпты; валидация Zod; stdio и Streamable HTTP.
- **Задачи:** написать свой MCP-сервер для подключения сервиса к агенту.
- **Сочетается с:** `ecc/agent-harness-construction`, `ecc/mcp-dependency-review`

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

### `ecc/prompt-optimizer`

Анализ черновика промпта и выдача улучшенной версии.

- **Ключевые навыки:** определение намерения; поиск недостающего контекста; подбор команд, навыков и агентов ECC.
- **Задачи:** превратить сырой запрос в сильный промпт.
- **Сочетается с:** `ecc/ecc-recipes`, `ecc/search-first`

### `ecc/pytorch-patterns`

Глубокое обучение на PyTorch.

- **Ключевые навыки:** пайплайны обучения; архитектуры моделей; загрузка данных; воспроизводимость.
- **Задачи:** построить и обучить нейросеть.
- **Сочетается с:** `ecc/mle-workflow`, `ecc/ml-adoption-playbook`

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

### `ecc/unified-memory`

Общая память и передача контекста между Claude, Codex, Cursor и другими агентами через ECC Memory Vault.

- **Ключевые навыки:** долговечный проверяемый контекст; передача задач между агентами.
- **Задачи:** продолжить работу другим агентом без потери контекста.
- **Сочетается с:** `ecc/ck`, `ecc/knowledge-ops`

---

<a id="cat-eng-process"></a>
## Архитектура, планирование и процесс разработки

**Область применения.** Архитектурные решения, декомпозиция задач, планы на несколько PR, git-процессы, оценка влияния изменений, работа с унаследованным кодом.

**Решаемые задачи.** План реализации фичи; ADR и фиксация решений; анализ влияния изменений; онбординг в чужой код; стандарты кода; сообщения коммитов; ретроспективы.

**Типовые связки.** codebase-onboarding → blueprint / plan-* (план) → architecture-decision-records → реализация → change-impact → conventional-commit-review → git-workflow.

Навыков в категории: 27.

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

### `ecc/dev-team`

Имитация командной сессии с ролями PM, архитектор, разработчик и QA над одной задачей.

- **Ключевые навыки:** взгляд с разных ролей; обсуждение компромиссов.
- **Задачи:** спроектировать фичу; отревьюить решение с нескольких сторон.
- **Сочетается с:** `ecc/council`, `ecc/blueprint`, `ecc/product-lens`

### `ecc/git-workflow`

Git-процессы — ветвление, соглашения коммитов, чистая история, merge и rebase, конфликты.

- **Ключевые навыки:** стратегии веток; приведение коммитов в порядок; разрешение конфликтов.
- **Задачи:** настроить командный git-процесс; навести порядок в истории перед мержем.
- **Сочетается с:** `ecc/conventional-commit-review`, `ecc/github-ops`

### `ecc/hexagonal-architecture`

Архитектура «порты и адаптеры» с чёткими границами домена.

- **Ключевые навыки:** инверсия зависимостей; оркестрация use case; тестируемость.
- **Задачи:** спроектировать или переработать систему с изолированным доменом.
- **Сочетается с:** `ecc/android-clean-architecture`, `ecc/architecture-decision-records`

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

---

<a id="cat-claude-setup"></a>
## Настройка Claude Code и экосистемы ECC

**Область применения.** Конфигурация Claude Code и других агентных оболочек — навыки, хуки, память, контекст, стоимость, установка ECC.

**Решаемые задачи.** Установка и настройка ECC; чистка конфигурации; контроль контекста и токенов; память между сессиями; создание и проверка навыков; хуки контроля качества.

**Типовые связки.** configure-ecc → agent-sort (что оставить) → context-budget / token-budget-advisor → config-gc (чистка) → skill-stocktake (ревизия навыков).

Навыков в категории: 27.

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

### `ecc/ck`

Постоянная память проекта для Claude Code (Context Keeper) через команды /ck и хук начала сессии.

- **Ключевые навыки:** сохранение состояния и следующих шагов; возобновление работы; краткий бриф проекта при старте.
- **Задачи:** продолжить проект в новой сессии без повторных объяснений.
- **Сочетается с:** `ecc/unified-memory`, `ecc/strategic-compact`

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

### `ecc/rules-distill`

Извлечение сквозных принципов из навыков и превращение их в правила.

- **Ключевые навыки:** поиск повторяющихся принципов; создание и правка файлов правил.
- **Задачи:** обобщить опыт из навыков в единые правила.
- **Сочетается с:** `ecc/continuous-learning-v2`, `ecc/skill-stocktake`

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

---

<a id="cat-docs"></a>
## Документация и управление знаниями

**Область применения.** Техническая документация, README, база знаний, живые документы, справочники по библиотекам, локализация.

**Решаемые задачи.** Написание и актуализация документации; аудит документов; база знаний команды; поиск актуальной документации фреймворков; синхронизация переводов.

**Типовые связки.** documentation-lookup (актуальные доки) → написание → docs-governance / living-docs-governance (аудит) → knowledge-ops (база знаний).

Навыков в категории: 7.

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

### `ecc/i18n-sync`

Перевод и синхронизация JSON-файлов локализации приложения.

- **Ключевые навыки:** учёт использования ключей; терминология проекта; валидация.
- **Задачи:** добавить язык или новые ключи и обновить переводы.
- **Сочетается с:** `ecc/visa-doc-translate`

### `ecc/knowledge-ops`

Управление базой знаний на нескольких уровнях хранения — файлы, MCP-память, векторные БД, git.

- **Ключевые навыки:** загрузка и синхронизация знаний; поиск; дедупликация.
- **Задачи:** собрать и поддерживать личную или командную базу знаний.
- **Сочетается с:** `ecc/unified-memory`, `ecc/google-workspace-ops`

### `ecc/living-docs-governance`

Защита документации долгоживущего проекта от устаревания.

- **Ключевые навыки:** роли документов (конституция, карта, статус, история); связка с инструкциями агента.
- **Задачи:** поддерживать документацию актуальной на протяжении жизни проекта.
- **Сочетается с:** `ecc/docs-governance`, `ecc/architecture-decision-records`

---

<a id="cat-content"></a>
## Контент, тексты и бренд

**Область применения.** Статьи, посты, рассылки, голос бренда, публикации в соцсетях, редактура.

**Решаемые задачи.** Длинные тексты в заданном стиле; контент-планы; адаптация под платформы; профиль голоса бренда; кросспостинг; редактура и вычитка.

**Типовые связки.** brand-discovery → brand-voice → article-writing / content-engine → crosspost / social-publisher.

Навыков в категории: 8.

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

### `ecc/content-engine`

Системы контента под каждую платформу — X, LinkedIn, TikTok, YouTube, рассылки.

- **Ключевые навыки:** посты и треды; сценарии; контент-календари; переупаковка одного материала под разные платформы.
- **Задачи:** построить регулярный контент-поток; адаптировать материал под площадки.
- **Сочетается с:** `ecc/crosspost`, `ecc/brand-voice`, `ecc/social-publisher`

### `ecc/crosspost`

Распространение контента по X, LinkedIn, Threads и Bluesky с адаптацией под каждую площадку.

- **Ключевые навыки:** адаптация формата; запрет одинаковых постов на разных площадках.
- **Задачи:** опубликовать материал сразу на нескольких платформах.
- **Сочетается с:** `ecc/content-engine`, `ecc/social-publisher`, `ecc/x-api`

### `ecc/social-publisher`

Планирование и публикация постов в 13 соцсетях через SocialClaw.

- **Ключевые навыки:** X, LinkedIn, Instagram, Facebook и другие; расписание публикаций.
- **Задачи:** автоматизировать публикации в соцсетях.
- **Сочетается с:** `ecc/content-engine`, `ecc/crosspost`

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

Навыков в категории: 2.

### `ecc/marketing-campaign`

Планирование и запуск маркетинговой кампании от начала до конца.

- **Ключевые навыки:** исследование аудитории; позиционирование; угол кампании; тексты лендинга; email-цепочки; посты.
- **Задачи:** провести кампанию под запуск или акцию.
- **Сочетается с:** `ecc/content-engine`, `ecc/brand-voice`, `ecc/seo`

### `ecc/seo`

Аудит, план и внедрение SEO.

- **Ключевые навыки:** техническое SEO; on-page; структурированные данные; Core Web Vitals; контент-стратегия.
- **Задачи:** улучшить видимость сайта в поиске.
- **Сочетается с:** `ecc/article-writing`, `ecc/benchmark`, `ecc/marketing-campaign`

---

<a id="cat-sales"></a>
## Продажи, клиенты и поддержка

**Область применения.** Продажи B2B, лидогенерация, работа с клиентами, customer success, биллинг клиентов, партнёрства.

**Решаемые задачи.** Поиск и квалификация лидов; холодные письма; подготовка к сделкам; удержание клиентов и снижение оттока; клиентская поддержка.

**Типовые связки.** lead-intelligence / поиск лидов → cold-email → sales-материалы → customer-success / churn-prevention.

Навыков в категории: 2.

### `ecc/lead-intelligence`

ИИ-конвейер разведки и аутрича по лидам вместо Apollo, Clay и ZoomInfo.

- **Ключевые навыки:** скоринг сигналов; поиск тёплых путей; обогащение данных; персонализированные сообщения.
- **Задачи:** найти и приоритизировать потенциальных клиентов или партнёров.
- **Сочетается с:** `ecc/exa-search`, `ecc/connections-optimizer`, `ecc/email-ops`

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

Навыков в категории: 2.

### `ecc/product-capability`

Перевод PRD, запросов roadmap и обсуждений в инженерный план возможности.

- **Ключевые навыки:** ограничения и инварианты; интерфейсы; нерешённые вопросы.
- **Задачи:** превратить продуктовую идею в план для разработки.
- **Сочетается с:** `ecc/product-lens`, `ecc/blueprint`, `ecc/intent-driven-development`

### `ecc/product-lens`

Проверка «зачем» до разработки через четыре продуктовые диагностики в стиле YC.

- **Ключевые навыки:** продуктовый бриф PRODUCT-BRIEF.md; рекомендация делать или нет.
- **Задачи:** решить, стоит ли вообще строить фичу или продукт.
- **Сочетается с:** `ecc/product-capability`, `ecc/market-research`, `ecc/council`

---

<a id="cat-project"></a>
## Управление проектами и командами

**Область применения.** Планирование и ведение проектов, Agile/Scrum, Jira/Confluence, ресурсы и риски, управление командами разработки.

**Решаемые задачи.** Планирование спринтов; статус-отчёты; управление рисками; ретроспективы; работа с Jira и Confluence; оргструктура и роли.

**Типовые связки.** sprint-planner → ведение задач (jira-*) → статус-отчёты → ретроспектива.

Навыков в категории: 3.

### `ecc/jira-integration`

Работа с задачами Jira через MCP или API.

- **Ключевые навыки:** чтение тикетов; анализ требований; смена статусов; комментарии.
- **Задачи:** взять задачу из Jira и обновить её по ходу работы.
- **Сочетается с:** `ecc/github-ops`, `ecc/project-flow-ops`

### `ecc/project-flow-ops`

Управление потоком работ между GitHub и Linear.

- **Ключевые навыки:** разбор issues и PR; связывание активной работы; разделение публичного и внутреннего.
- **Задачи:** держать задачи и код синхронизированными.
- **Сочетается с:** `ecc/github-ops`, `ecc/jira-integration`, `ecc/story-lifecycle`

### `ecc/story-lifecycle`

Файловый цикл «эпик → история → спринт» без внешнего трекера.

- **Ключевые навыки:** эпики; разбиение на истории; спринты; отслеживание статуса.
- **Задачи:** вести проект прямо в репозитории.
- **Сочетается с:** `ecc/project-flow-ops`, `ecc/blueprint`

---

<a id="cat-strategy"></a>
## Стратегия бизнеса и C-level

**Область применения.** Советники уровня CEO/CFO/CMO/CTO/COO и других руководителей, стратегия, рост, конкурентный анализ, организационное развитие.

**Решаемые задачи.** Стратегические решения и сценарии; совет директоров и инвесторы; оргдизайн; конкурентная разведка; бизнес-модели; кризисные решения.

**Типовые связки.** competitive-platform-analysis → benchmark-methodology → competitive-report-structure; council / C-level советники для решения → executive-материалы.

Навыков в категории: 6.

### `ecc/benchmark-methodology`

Оценка конкурентов по девяти взвешенным измерениям с рубриками 1–5 и картой напряжений.

- **Ключевые навыки:** позиционирование, голос, визуал, упаковка предложения, доказательства, цены; профили конкурентов.
- **Задачи:** сравнить и оценить конкурентов перед сборкой отчёта.
- **Сочетается с:** `ecc/competitive-platform-analysis`, `ecc/competitive-report-structure`, `ecc/market-research`

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

### `ecc/recursive-decision-ledger`

Многократные прогоны рассуждений с журналом решений.

- **Ключевые навыки:** испытания; оценки; проверки согласованности; гейты продвижения.
- **Задачи:** принять сложное решение через серию проверяемых итераций.
- **Сочетается с:** `ecc/council`

---

<a id="cat-finance"></a>
## Финансы, биллинг и инвестиции

**Область применения.** Финансовый анализ и модели, бюджет, бухгалтерия, налоги, биллинг и подписки, привлечение инвестиций.

**Решаемые задачи.** Финансовые модели и прогнозы; анализ отчётности; юнит-экономика; управление подписками и возвратами; материалы для инвесторов; трейдинг-риски.

**Типовые связки.** финансовая модель → анализ (financial-analyst) → investor-materials → investor-outreach; биллинг — customer-billing-ops / finance-billing-ops.

Навыков в категории: 4.

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

---

<a id="cat-compliance"></a>
## Регуляторика, комплаенс и качество (QMS)

**Область применения.** ISO 13485/9001/27001, MDR/FDA, GDPR, HIPAA, SOC 2, CMMC, аудит, системы менеджмента качества, договоры.

**Решаемые задачи.** Подготовка к аудитам и сертификации; CAPA и несоответствия; оценка рисков; политика конфиденциальности данных; регистрация медизделий; шаблоны договоров.

**Типовые связки.** оценка готовности (*-readiness) → риск-менеджмент → документы QMS → внутренний аудит → CAPA.

Навыков в категории: 2.

### `ecc/master-agreement-generator`

Черновики рамочных договоров с контрагентами из шаблона и JSON-спецификации.

- **Ключевые навыки:** подбор пунктов по роли; работа с приложением А.
- **Задачи:** быстро подготовить договор на ревью юристу.
- **Сочетается с:** `ecc/esign-field-placement`

### `ecc/quality-nonconformance`

Контроль качества и управление несоответствиями в регулируемом производстве (FDA 21 CFR 820, IATF 16949, AS9100).

- **Ключевые навыки:** жизненный цикл NCR; 5 почему, Исикава; CAPA; статистический контроль.
- **Задачи:** разобрать несоответствие и провести корректирующие действия.
- **Сочетается с:** `ecc/production-scheduling`, `ecc/returns-reverse-logistics`

---

<a id="cat-operations"></a>
## Операции, логистика и закупки

**Область применения.** Цепочки поставок, логистика, закупки, производство, склад, таможня, энергоснабжение.

**Решаемые задачи.** Планирование спроса и запасов; управление перевозчиками; таможенное оформление; исключения в логистике; возвраты; планирование производства; закупки энергии.

**Типовые связки.** inventory-demand-planning → production-scheduling → carrier-relationship-management → logistics-exception-management → returns-reverse-logistics.

Навыков в категории: 7.

### `ecc/carrier-relationship-management`

Управление портфелем перевозчиков (FTL, LTL, интермодальные) от отбора до продления контрактов.

- **Ключевые навыки:** проверка перевозчиков; переговоры о ставках и топливных надбавках; тендеры и маршрутные гайды; скоринг перевозчиков.
- **Задачи:** провести тендер на перевозки; оценить и перераспределить объёмы между перевозчиками.
- **Сочетается с:** `ecc/logistics-exception-management`, `ecc/inventory-demand-planning`

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

---

<a id="cat-research"></a>
## Исследования и наука

**Область применения.** Глубокие исследования по веб-источникам, академические статьи, обзоры литературы, рецензирование, гранты, патенты, рыночные исследования.

**Решаемые задачи.** Исследование с цитатами; систематический обзор литературы; написание и рецензирование статей; поиск в PubMed и патентных базах; оценка источников.

**Типовые связки.** deep-research (сбор) → literature-review / scholar-evaluation (оценка) → academic-paper (написание) → academic-paper-reviewer (рецензия).

Навыков в категории: 10.

### `ecc/deep-research`

Исследовательские отчёты с цитатами по множеству веб-источников через MCP firecrawl и exa.

- **Ключевые навыки:** план подвопросов; поиск и глубокое чтение; синтез с цитатами и уровнем уверенности.
- **Задачи:** подготовить обоснованный обзор темы.
- **Сочетается с:** `ecc/exa-search`, `ecc/research-ops`, `ecc/market-research`

### `ecc/exa-search`

Нейропоиск через Exa MCP по вебу, коду, компаниям и людям.

- **Ключевые навыки:** веб-поиск; поиск примеров кода; разведка по компаниям; поиск людей.
- **Задачи:** быстро найти актуальную информацию или примеры для исследования.
- **Сочетается с:** `ecc/deep-research`, `ecc/lead-intelligence`, `ecc/market-research`

### `ecc/market-research`

Рыночные исследования, конкурентный анализ и due diligence с указанием источников.

- **Ключевые навыки:** анализ рынка и отрасли; сводки для решений.
- **Задачи:** оценить рынок, конкурентов или стартап перед инвестицией.
- **Сочетается с:** `ecc/deep-research`, `ecc/competitive-platform-analysis`, `ecc/investor-materials`

### `ecc/osint-investigation`

Методика OSINT-расследования по скудным зацепкам.

- **Ключевые навыки:** извлечение упущенных следов; связывание разрозненных данных; проверка версий по источникам.
- **Задачи:** собрать картину по человеку, компании или событию из открытых источников.
- **Сочетается с:** `ecc/exa-search`, `ecc/deep-research`

### `ecc/research-ops`

Исследование актуального состояния дел по свежим публичным данным.

- **Ключевые навыки:** сбор фактов; сравнения; обогащение; рекомендации.
- **Задачи:** получить свежие факты и обоснованную рекомендацию.
- **Сочетается с:** `ecc/deep-research`, `ecc/exa-search`

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

---

<a id="cat-productivity"></a>
## Личная продуктивность и коммуникации

**Область применения.** Почта, мессенджеры, календарь, заметки, личная база знаний, еженедельные обзоры, принятие решений.

**Решаемые задачи.** Разбор почты и черновики ответов; планирование недели; глубокая работа; подготовка к встречам; личная база знаний; уведомления.

**Типовые связки.** email-ops / messages-ops (входящие) → планирование (weekly-review) → deep-work → заметки и база знаний.

Навыков в категории: 8.

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

---

<a id="cat-media"></a>
## Видео, графика и мультимедиа

**Область применения.** Создание и монтаж видео, анимации, генерация изображений и медиа, презентации, 3D.

**Решаемые задачи.** Программные видео (Remotion, Manim); монтаж; генерация изображений и видео ИИ; слайды; демо-ролики интерфейсов.

**Типовые связки.** сценарий (content-engine) → генерация медиа (fal-ai-media) → видео (remotion-video-creation / manim-video) → монтаж (video-editing).

Навыков в категории: 12.

### `ecc/blender-motion-state-inspection`

Проверка персонажей, ригов, поз и анимации в Blender там, где скриншотов недостаточно.

- **Ключевые навыки:** ретаргетинг анимации; контакт с землёй; направление взгляда; соответствие модели и движения.
- **Задачи:** найти ошибки в 3D-анимации персонажа.
- **Сочетается с:** `ecc/video-editing`

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

### `ecc/manim-video`

Анимационные объяснения технических концепций на Manim.

- **Ключевые навыки:** графики; схемы систем; продуктовые демонстрации.
- **Задачи:** сделать обучающее видео об идее или системе.
- **Сочетается с:** `ecc/video-editing`, `ecc/remotion-video-creation`

### `ecc/remotion-video-creation`

Видео на React через Remotion.

- **Ключевые навыки:** 3D; анимации; аудио; субтитры; графики; переходы.
- **Задачи:** собрать видео программно.
- **Сочетается с:** `ecc/video-editing`, `ecc/manim-video`, `ecc/ui-demo`

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

Навыков в категории: 5.

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

---

## Пока без русского описания

- `academic/academic-paper` — 12-agent academic paper writing pipeline.
- `academic/academic-paper-reviewer` — Multi-perspective academic paper review with dynamic reviewer personas.
- `academic/academic-pipeline` — Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise ->…
- `academic/deep-research` — Universal deep research agent team.
- `academic/sr-screener` — Protocol-driven study screening for systematic, scoping and rapid reviews.
- `career/academic-research-cv` — Build an academic CV for research and faculty roles — format publications, grants, teaching, and service sections by discipline convention
- `career/ats-resume-checker` — Check and fix resume ATS compatibility — scan for formatting issues, rewrite weak bullets with metrics, match keywords to job descriptions,…
- `career/career-pivot-planner` — Plan your career pivot step by step — map transferable skills, translate experience to a new industry, write transition narratives, and ide…
- `career/compensation-negotiator` — Negotiate your full compensation package — research market rates, draft counter-offer emails, break down total comp, and compare multiple o…
- `career/cover-letter-writer` — Generate personalized cover letters — connect resume experience to job requirements with industry-appropriate tone, hook openings, and gap-…
- `career/executive-leadership-resume` — Write an executive resume for VP, Director, and C-suite roles — leadership branding, transformation narratives, P&L metrics, and board-read…
- `career/job-fit-analyzer` — Analyze any job posting to see if you're a fit — match score, skill gap breakdown, red flag detection, and whether it's worth applying
- `career/linkedin-profile-booster` — Boost your LinkedIn profile for recruiter visibility — rewrite headlines, craft About sections, place searchable keywords, and audit profil…
- `career/mock-interview-coach` — Practice mock interviews with AI coaching — build STAR stories, rehearse behavioral answers, craft "tell me about yourself" scripts, and pr…
- `career/portfolio-case-study` — Write portfolio case studies that win interviews — structure project narratives with before/after results, and build ATS-safe creative resu…
- `career/resume-customizer` — Customize your resume for any job posting — reorder sections, integrate keywords, manage multiple versions, and score your match before app…
- `career/software-engineer-resume` — Build a software engineer resume that gets interviews — format tech stacks, write metrics-driven bullets, showcase projects, and optimize y…
- `claude-skills/a11y-audit` — Use for any accessibility audit or a11y fix (WCAG 2.2 A/AA, color contrast, compliance report, CI check) in React, Next.js, Vue, Angular, S…
- `claude-skills/ab-test-setup` — Use before planning or launching any A/B, split or multivariate test, or when asked if a result is significant.
- `claude-skills/access-lifecycle` — Use when preparing or running a user access review, checking that leavers lost their access, finding orphaned or ownerless service accounts…
- `claude-skills/ad-creative` — Use for any ad copy request (RSA headlines, Meta, LinkedIn or TikTok ads, bulk variations), before writing.
- `claude-skills/adversarial-reviewer` — Tough, critical review of a diff or PR before merge, through hostile reviewer personas that catch shared blind spots.
- `claude-skills/aeo` — Use when content should be cited by ChatGPT, Perplexity, Claude or Gemini (answer engine optimization), before rewriting it.
- `claude-skills/agent-decision-receipts` — Use when an autonomous agent takes a side-effecting action (deploy, delete, pay, grant access) that may need proving later, or for EU AI Ac…
- `claude-skills/agent-designer` — Design multi-agent systems (supervisor, swarm, pipeline) and tool schemas; find bottlenecks in run logs.
- `claude-skills/agent-harness` — Use when an agent should drive a goal in one of this repo's domains to a verified close, before starting the work.
- `claude-skills/agent-launcher-orchestrator` — Use when someone wants to build, launch, grade or schedule a Claude Managed Agent in their own Anthropic account ('build me an agent', 'run…
- `claude-skills/agent-memory` — Use when an agent keeps relearning the same correction, CLAUDE.md has grown unreadable, or you need to trace where a remembered rule came f…
- `claude-skills/agent-protocol` — Use when C-suite advisor agents need to call each other or run a multi-role meeting.
- `claude-skills/agent-regression-evals` — Use before shipping any agent, prompt, model or tool change, or when a pass-rate drop needs a verdict.
- `claude-skills/agent-run-forensics` — Use when asked why an agent did something, what a past session or run changed, whether tests really passed, or to verify a session summary.
- `claude-skills/agent-workflow-designer` — Use when architecting a multi-step LLM or agent pipeline, choosing single vs multi-agent, or fixing context bloat and broken handoffs.
- `claude-skills/agenthub` — Run several agents on one task in parallel and keep the best result: faster code, copy variants, research angles.
- `claude-skills/agile-product-owner` — Use for backlog work: writing user stories and acceptance criteria, splitting epics, estimating or prioritizing for a sprint.
- `claude-skills/ai-act-readiness` — EU AI Act readiness: risk tier, duties, deadlines.
- `claude-skills/ai-decision-authority` — Use before letting AI or an agent act on a marketing or GTM task without human review, or when writing an AI review policy.
- `claude-skills/ai-security` — Use when assessing an AI/ML system or LLM agent for prompt injection, jailbreaks, model inversion, data poisoning or tool abuse.
- `claude-skills/aims-audit` — ISO 42001 AI readiness check.
- `claude-skills/analytics-tracking` — Use for any GA4, Google Tag Manager, event-tracking or conversion-tracking setup, audit or broken-event debug, before touching tags.
- `claude-skills/andreessen` — Blunt market-first verdict on an idea, venture or career bet, leading with the strongest counterargument, or a 3x5-card daily plan.
- `claude-skills/api-design-reviewer` — Use for any PR or spec that adds or changes REST endpoints, before approving it.
- `claude-skills/api-test-suite-builder` — Use when asked to write API, integration or contract tests for REST endpoints.
- `claude-skills/app-store-optimization` — Use for any App Store or Google Play listing, keyword, ranking or review question, before writing metadata.
- `claude-skills/apple-hig-expert` — Use when designing or reviewing iOS, macOS, watchOS or visionOS UI against Apple's Human Interface Guidelines, including Liquid Glass, cont…
- `claude-skills/ar-loop` — Use for /ar-loop, or to run an autoresearch experiment on a schedule (10 min to monthly) with CronCreate.
- `claude-skills/ar-resume` — Use for /ar-resume, or to continue a paused autoresearch experiment from its branch and results history.
- `claude-skills/ar-run` — Use for /ar-run, or to run one manual autoresearch iteration: edit, evaluate, keep or discard.
- `claude-skills/ar-status` — Show autoresearch results and progress.
- `claude-skills/arquiteto-de-empresa` — Use when a founder wants to document or design a whole company as version-controlled markdown (company as code, a company wiki agents can r…
- `claude-skills/atlassian-admin` — Use for Atlassian org administration: Jira or Confluence users and groups, permissions, SSO, marketplace apps or security policy.
- `claude-skills/atlassian-templates` — Use when creating or changing Jira or Confluence templates, blueprints or page layouts for reuse across the org.
- `claude-skills/autoresearch-agent` — Make a file measurably better by trial: faster code, smaller bundle, higher pass rate or prompt score.
- `claude-skills/aws-solution-architect` — Use when designing or costing an AWS architecture (serverless, Lambda, API Gateway, DynamoDB, ECS, Aurora, CloudFormation, migration to AWS…
- `claude-skills/azure-cloud-architect` — Use when designing or costing an Azure architecture (AKS, App Service, Functions, Cosmos DB, Bicep or ARM, Azure DevOps, migration to Azure…
- `claude-skills/behuman` — Reply like a real person, direct and warm, without lists or hedging.
- `claude-skills/board` — Use to post or read messages on the AgentHub coordination board between competing agents.
- `claude-skills/board-deck-builder` — Use when building a board deck, investor update or QBR from all C-suite perspectives.
- `claude-skills/board-meeting` — Use for /c-level-agents:boardroom or a strategic question that needs a structured multi-executive deliberation.
- `claude-skills/board-prep` — Use before a board meeting, investor update or fundraising pitch where the numbers will be challenged.
- `claude-skills/boardroom` — Use for /c-level-agents:boardroom, or a decision spanning several executive domains (a pricing change, raise vs cut).
- `claude-skills/book-to-skill` — Use when turning a book, docs folder or spec collection (PDF, EPUB, DOCX, HTML, Markdown) into an agent skill, before summarizing it by han…
- `claude-skills/boost-asio-pro` — Use for any C++ networking code with Boost.Asio or standalone Asio (TCP/UDP, SSL, timers, strands, io_context, co_spawn, awaitable, complet…
- `claude-skills/brand-guidelines` — Use when writing or enforcing brand guidelines (colors, typography, logo rules, imagery, tone of voice), or checking an asset against them.
- `claude-skills/brief` — Use for /c-level-agents:brief, or to frame a strategic question (options, assumptions, success criteria) as a one-page brief before deliber…
- `claude-skills/browser-automation` — Automate a browser: scrape websites, fill forms, pull structured data from web pages.
- `claude-skills/browserstack` — Use when running Playwright tests on BrowserStack or across a browser matrix ('browserstack', 'cross-browser', 'test on safari or firefox',…
- `claude-skills/business-growth-skills` — Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations and contract-and-proposal-writ…
- `claude-skills/business-investment-advisor` — Use when deciding whether a capital expense is worth it (equipment, property, an acquisition, hiring, technology), or for ROI, IRR, NPV, pa…
- `claude-skills/business-name-fit` — Use when naming a company, brand or product, or checking whether a name works abroad, before committing to one.
- `claude-skills/business-operations-skills` — Route internal operations requests to the right BizOps skill: process, vendors, capacity, internal comms, SOPs, procurement.
- `claude-skills/c-level-agents` — Use when the founder wants a virtual executive team or a /c-level-agents command.
- `claude-skills/c-level-skills` — Find which C-level advisor fits a question: 14 C-suite roles, board meetings, culture, M&A.
- `claude-skills/caio-review` — Use for /c-level-agents:caio-review, or to challenge a plan involving AI (no eval set, API vs fine-tune vs self-host, EU AI Act class).
- `claude-skills/campaign-analytics` — Analyze campaign performance on the user's numbers: ROAS, CPA, ROI, multi-touch attribution and funnel drop-off.
- `claude-skills/capa-officer` — Use for CAPA work in a medical device QMS: root cause analysis (5-Why, fishbone), corrective action plans, effectiveness checks or CAPA met…
- `claude-skills/capacity-planner` — Size an ops or support team and plan headcount: Erlang C queue models, utilization risk, hiring order.
- `claude-skills/capture` — Use whenever the user unloads a messy brain dump of ideas, tasks and plans ('capture this', 'brain dump', a long unstructured paste) and wa…
- `claude-skills/caveman` — Terse mode: drop filler, articles and pleasantries, keep technical accuracy, about 75% fewer tokens, and stay in it.
- `claude-skills/cco-review` — Challenge a churn, retention, segment or CS hiring plan.
- `claude-skills/cdo-review` — Use for /c-level-agents:cdo-review, or to challenge a plan touching training-data rights, data architecture or data monetization.
- `claude-skills/ceo-advisor` — Advice for a CEO or founder on running the company: board and investor trouble, raise or cut, strategy bets, org and culture.
- `claude-skills/cfo-advisor` — Startup finance: runway and burn, unit economics (LTV, CAC, payback), fundraising and dilution.
- `claude-skills/cfo-review` — Challenge a plan that spends real money: hiring wave, raise, channel budget.
- `claude-skills/challenge` — Pre-mortem a plan: assume it failed in 12 months and work back to the assumptions, dependencies and execution risks.
- `claude-skills/change-management` — Use when rolling out a reorg, pivot, tool switch, leadership change or product kill.
- `claude-skills/changelog-generator` — Write release notes and CHANGELOG.md from commits and pick the next semver version.
- `claude-skills/channel-economics` — Use for a direct vs partner channel review: fully loaded cost to serve, channel ROI and the best channel mix under constraints.
- `claude-skills/chaos-engineering` — Use before running a chaos experiment, gameday or fault injection, or after one to write it up.
- `claude-skills/chief-ai-officer-advisor` — Use for AI strategy decisions: API vs fine-tune vs build, EU AI Act or US state risk classification, when self-hosting pays off, or AI hiri…
- `claude-skills/chief-customer-officer-advisor` — Use for retention strategy, customer segmentation or CS team sizing decisions (GRR vs NRR, churn causes, pooled vs named CSMs).
- `claude-skills/chief-data-officer-advisor` — Use for data strategy decisions: training models on customer data, warehouse vs lakehouse vs mesh, valuing data for a raise or M&A, or data…
- `claude-skills/chief-of-staff` — Use when a founder question needs routing to the right C-suite advisor, or a cross-functional decision needs a board meeting convened.
- `claude-skills/chro-advisor` — People strategy: hiring plans, comp bands, org structure, performance, retention.
- `claude-skills/churn-prevention` — Use when designing a cancel flow, save offers, exit surveys or dunning emails, or cutting failed-payment churn.
- `claude-skills/ci-cd-pipeline-builder` — Generate a CI/CD workflow for a repo from its detected stack: lint, test, build, deploy.
- `claude-skills/ciso-advisor` — Use for security leadership decisions: a security program, budget justification in dollars, SOC 2 vs ISO 27001 vs HIPAA roadmap, or board s…
- `claude-skills/ciso-review` — Challenge a plan touching customer data, compliance or prod access.
- `claude-skills/claude-coach` — Use when the user wants to get better at using Claude ('coach me', 'teach me Claude tricks', 'make me a power user').
- `claude-skills/clinical-research` — Use when designing a prospective clinical study: choosing primary and secondary endpoints, estimating sample size and power, or scoring fea…
- `claude-skills/cloud-security` — Use when checking AWS, Azure or GCP for security misconfigurations: IAM privilege escalation, public buckets, open security groups, IaC gap…
- `claude-skills/cmmc-readiness` — Use when a defense contractor or subcontractor is preparing for a CMMC 2.0 Level 2 self-assessment or C3PAO assessment, calculating or chec…
- `claude-skills/cmo-advisor` — Marketing leadership: positioning, product-led vs sales-led vs community-led growth, budget split across channels, marketing team design.
- `claude-skills/cmo-review` — Use for /c-level-agents:cmo-review, or to challenge positioning, ICP, messaging or channel mix before a launch.
- `claude-skills/code-reviewer` — Use for any code review: a pull request, a diff, a commit, or a pasted function, handler or file in TypeScript, JavaScript, Python, Go, Swi…
- `claude-skills/code-to-prd` — Use when asked to write a PRD or product spec from an existing codebase (reverse-engineer requirements, document pages, fields, routes and…
- `claude-skills/code-tour` — Use when asked for a CodeTour .tour file or a step-by-step code walkthrough (onboarding, architecture, PR review, how X works).
- `claude-skills/codebase-onboarding` — Explain an unfamiliar repo: architecture brief and onboarding docs.
- `claude-skills/coding-agent-rollout` — Roll out Claude Code to a team: shared or managed settings, MCP and plugin approval, layered CLAUDE.md, adoption.
- `claude-skills/cold-email` — Use for any cold outreach or SDR email or follow-up sequence to prospects who did not opt in, before drafting.
- `claude-skills/collab-proof` — Use for /collab-proof or a session retrospective on what Claude contributed versus what the user drove.
- `claude-skills/commercial-forecaster` — Use when building a bookings, ARR, pipeline or NRR forecast, or a commit, best-case and pipeline board number.
- `claude-skills/commercial-policy` — Use when writing or revising discount rules: discount matrix, approver thresholds, exception flows and the deal framework sales works under.
- `claude-skills/commercial-skills` — Use when a commercial request needs routing (pricing, deal review, discounts, partners, channels, policy, RFPs, forecasts): 'review this de…
- `claude-skills/commit-craft` — Turn a mix of changes into clean, reviewable commits with good messages, blocking staged secrets and .env files.
- `claude-skills/company-os` — Use when choosing or setting up how the company runs: EOS, Scaling Up or OKRs, accountability chart, scorecard, meeting rhythm, quarterly r…
- `claude-skills/competitive-intel` — Use for competitor analysis, battlecards, win/loss review or positioning against alternatives.
- `claude-skills/competitive-teardown` — Deep competitor teardown: pricing, reviews, hiring, SEO, UX, scored across 12 dimensions with SWOT and positioning maps.
- `claude-skills/competitor-alternatives` — Use when creating an 'X vs Y', '[product] alternative' or comparison page, before drafting.
- `claude-skills/compliance-os` — Use when running several compliance frameworks at once: which apply, where controls overlap, a mock audit or one evidence checklist.
- `claude-skills/compliance-readiness` — Use for /compliance-os:compliance-readiness, or before adding a framework or planning the annual audit calendar.
- `claude-skills/confluence-expert` — Use when building or restructuring a Confluence space: page hierarchy, permissions, templates, Jira macros or a content audit.
- `claude-skills/content-creator` — Use when someone asks for 'content creator' by name.
- `claude-skills/content-humanizer` — Make a draft sound less like AI: fix generic, robotic text with rhythm, specifics, personality and brand voice.
- `claude-skills/content-production` — Write a blog post, article or guide end to end: research, outline, draft, SEO pass and quality gates.
- `claude-skills/content-strategy` — Use when deciding what content to create (topics, clusters, a blog or content plan), before listing ideas.
- `claude-skills/context-engine` — Use when starting a C-suite advisor session, when company context is missing or older than 90 days, or before company data goes to an exter…
- `claude-skills/contract-and-proposal-writer` — Use when drafting a freelance contract, proposal, SOW, NDA or MSA for US, EU, UK or DACH jurisdictions.
- `claude-skills/coo-advisor` — Use for operations leadership: process design, OKR execution, operating cadence, bottlenecks or scaling playbooks.
- `claude-skills/copy-editing` — Edit, proofread and tighten existing marketing copy in focused passes: clarity, voice, proofreading, specificity, readability and AI tells.
- `claude-skills/copywriting` — Use for any headline, tagline, CTA, landing, pricing or about-page copy request, before drafting.
- `claude-skills/coverage` — Find what is not tested: map untested pages and flows and coverage gaps.
- `claude-skills/cpo-advisor` — Product leadership: PMF measurement, product vision, portfolio investment, product org design, board product reporting.
- `claude-skills/cpo-review` — Challenge a roadmap, PMF claim or feature kill.
- `claude-skills/cro-advisor` — Use for B2B revenue leadership: forecasting, quotas, sales model, NRR and churn, pricing or sales capacity.
- `claude-skills/cro-review` — Challenge a forecast, win-rate drop or sales hires.
- `claude-skills/cross-eval` — Use for /c-level-agents:cross-eval, or when a high-stakes memo needs independent review by several models before the boardroom.
- `claude-skills/cs-onboard` — Use when setting up the C-suite advisors for the first time, or when company context is missing or stale after a raise or pivot.
- `claude-skills/cto-advisor` — CTO decisions: tech debt, architecture direction, scaling the engineering team, technology evaluation, DORA metrics.
- `claude-skills/cto-review` — Challenge an architecture bet, 10x scaling plan or rebuild vs buy.
- `claude-skills/culture-architect` — Use when defining company values, turning them into behaviors, assessing culture health or designing rituals.
- `claude-skills/customer-success-manager` — Use when reviewing customer accounts for health, churn risk or expansion.
- `claude-skills/data-quality-auditor` — Use before analysis or model training on any dataset, or when asked to profile data or hunt missing values and outliers.
- `claude-skills/database-designer` — Design a database schema: tables, relationships, indexes, normalization, SQL vs NoSQL, migration plans.
- `claude-skills/database-schema-designer` — Use when asked for an ERD, table relationships, normalization or a schema migration plan.
- `claude-skills/deal-desk` — Use before closing a deal that needs a discount beyond AE authority, has a redlined MSA or unclear per-deal economics.
- `claude-skills/decide` — Use for /c-level-agents:decide, or right after the founder approves a boardroom memo, to log it as a durable decision.
- `claude-skills/decision-logger` — Use when logging a decision after a board meeting, reviewing past decisions or checking overdue actions.
- `claude-skills/deep-learning-book` — Use when studying or applying Goodfellow, Bengio and Courville's Deep Learning, or asking if its advice still holds.
- `claude-skills/deep-work` — Use when someone wants to plan a deep work day, time-block their calendar or task list, budget or cut shallow work, protect focus hours, tr…
- `claude-skills/deepread` — Use when the user asks to deeply read a book, article, PDF, or document set; extract claims and evidence; build a knowledge map; or learn t…
- `claude-skills/demo-video` — Use when asked for a demo video, product walkthrough, feature showcase or GIF from screenshots or scene descriptions.
- `claude-skills/dependency-auditor` — Audit project dependencies for CVEs and licenses and plan safe upgrades.
- `claude-skills/design-qa` — Use when a UI screen, page or component is about to be called done, handed off or shipped, or when generated UI looks generic or half-finis…
- `claude-skills/design-system` — Use when setting up brand settings before the first markdown-to-HTML conversion, or changing them.
- `claude-skills/docker-development` — Use for any Dockerfile or docker-compose file to write, optimize or review, before editing it.
- `claude-skills/dossier` — Use for diligence or meeting prep on a specific company, person or organization ('prep me for a meeting with X', 'due diligence on Y').
- `claude-skills/email-sequence` — Use for any drip, nurture, onboarding, welcome or re-engagement email sequence to opted-in users, before writing emails.
- `claude-skills/email-template-builder` — Use when adding or reworking transactional email (React Email templates, Resend, Postmark, SendGrid or SES, preview, i18n, dark mode, deliv…
- `claude-skills/embedded-iot-mentor` — Use for any embedded or IoT hardware project (ESP32, STM32, Arduino, Pico, firmware, PCB, MQTT, Home Assistant, sensor dashboards), before…
- `claude-skills/engineering-advanced-skills` — Pick the right advanced engineering skill: agents, RAG, MCP, CI/CD, databases, observability, release.
- `claude-skills/engineering-skills` — Find which engineering skill fits a task: architecture, frontend, backend, QA, DevOps, security, AI/ML, data, cloud.
- `claude-skills/env-secrets-manager` — Use when auditing .env files, planning credential rotation, chasing a missing env var in production or hardening a repo against leaked secr…
- `claude-skills/epic-design` — Use for any landing page, hero section or scroll-driven web design that should feel cinematic (parallax, scrollytelling, overlapping sectio…
- `claude-skills/eu-ai-act-specialist` — Use for EU AI Act (Regulation 2024/1689) compliance work: classifying an AI system's risk tier, planning the Art.
- `claude-skills/eval` — Rank finished AgentHub agents by metric or judge.
- `claude-skills/execute` — Use for /c-level-agents:execute, or to turn an approved decision into a 90-day plan with weekly milestones and owners.
- `claude-skills/executive-mentor` — Use when a founder or executive needs a plan stress-tested, a dreaded decision made, a hard board meeting prepared or an honest post-mortem.
- `claude-skills/experiment-designer` — Plan A/B tests and product experiments: hypotheses, sample size, priority, reading results.
- `claude-skills/extract` — Turn a fix or pattern that keeps coming up into a reusable skill with SKILL.md, reference docs and examples.
- `claude-skills/fable-goal` — Use when the user wants a /goal prompt rather than the build itself ('/fable-goal', 'turn this into a goal prompt', 'write the prompt that…
- `claude-skills/fda-consultant-specialist` — Use for FDA medical device questions: 510(k) vs De Novo vs PMA, predicates and substantial equivalence, QMSR (21 CFR 820), HIPAA or device…
- `claude-skills/fda-qsr-audit-prep` — Use for /compliance-os:fda-qsr-audit-prep, or before an FDA inspection, QMSR internal audit or Form 483 response.
- `claude-skills/feature-flags-architect` — Use before adding, rolling out or retiring a feature flag or kill switch, or when flag debt piles up.
- `claude-skills/finance-skills` — Pick the right finance skill: ratios, DCF, forecasts (financial-analyst), ARR, churn, CAC, LTV (saas-metrics-coach), month-end-close.
- `claude-skills/financial-analyst` — Analyze financial statements, value a company with a DCF, explain budget variance, build rolling forecasts.
- `claude-skills/fix` — Diagnose and fix a failing or flaky Playwright test.
- `claude-skills/focused-fix` — Use when a whole feature or module is broken and needs fixing end to end ('make X work', 'the Y module is broken').
- `claude-skills/form-cro` — Use when a lead, contact, demo or checkout form is underperforming or being designed, before changing fields.
- `claude-skills/founder-coach` — Use when a founder is the bottleneck, can't delegate, is burning out or is moving from IC to CEO.
- `claude-skills/founder-mode` — Use for /c-level-agents:founder-mode, or any founder strategy question that hasn't been routed yet.
- `claude-skills/free-tool-strategy` — Use when considering a free calculator, grader, checker or generator as a marketing asset, before building it.
- `claude-skills/freeze` — Use for /c-level-agents:freeze, or to put a cooling-off lock on an irreversible decision made under pressure.
- `claude-skills/full-page-screenshot` — Use when asked for a full-page or long screenshot of a web page.
- `claude-skills/gc-review` — Use for /c-level-agents:gc-review, or to challenge a term sheet, customer MSA, IP assignment or regulatory exposure before signing.
- `claude-skills/gcp-cloud-architect` — Design, deploy and cut the cost of Google Cloud setups: Cloud Run, GKE, Functions, Cloud SQL, BigQuery, moving to GCP.
- `claude-skills/gdpr-audit-prep` — Use for /compliance-os:gdpr-audit-prep, or before a GDPR review, post-breach audit or DPA investigation.
- `claude-skills/gdpr-dsgvo-expert` — Use for GDPR or DSGVO work: scanning a codebase for privacy risks, writing a DPIA or tracking data subject requests against the Art.
- `claude-skills/general-counsel-advisor` — Legal review of contracts and term sheets (MSA, SaaS, NDA, DPA, employment), IP strategy and regulatory exposure (HIPAA, GDPR, FDA, fintech…
- `claude-skills/generate` — Use when asked to write Playwright or e2e tests for a page, component or feature ('write tests', 'add tests for', 'e2e test').
- `claude-skills/git-worktree-manager` — Use when running several branches or agents in parallel on one repo.
- `claude-skills/google-workspace-cli` — Use for Google Workspace admin or automation from the gws CLI (Gmail, Drive, Sheets, Calendar, Docs, Chat, Tasks).
- `claude-skills/grade-iterate` — Use when a launched managed agent needs grading against a rubric and improving ('grade my agent', 'is it good enough').
- `claude-skills/grants` — Use for any NIH funding question ('find grants for my research', 'which NIH institute').
- `claude-skills/grill-me` — Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree.
- `claude-skills/grill-with-docs` — Use when a plan should be stress-tested against the project's own docs (CONTEXT.md glossary, docs/adr decisions), or the user says 'grill w…
- `claude-skills/handoff` — Compact the current conversation into a handoff document for another agent to pick up, referencing existing artifacts (PRDs, plans, ADRs, i…
- `claude-skills/hard-call` — Use for a decision where every option hurts (layoff vs down round, killing a loved product).
- `claude-skills/helm-chart-builder` — Use for any Helm chart to create, review or harden (values.yaml, templates, subcharts, RBAC, pod security), before editing it.
- `claude-skills/hivemind` — Use when delegating grunt work to free opencode workers instead of spending Claude tokens: one worker or a scout, coder and tester swarm in…
- `claude-skills/hub-init` — Use for /hub-init, or to start an AgentHub competition: task, agent count and evaluation criteria.
- `claude-skills/hub-run` — Use for /hub-run, or to run a whole AgentHub competition end to end: init, baseline, spawn, eval and merge.
- `claude-skills/hub-status` — Use for /hub-status, or to check AgentHub agent progress, branches and DAG state.
- `claude-skills/human-gate` — Use before shipping anything that needs human sign-off (a plan, spec, report, page, migration or irreversible action).
- `claude-skills/i18n-localization` — Use when adding UI text, adding or shipping a language, reviewing translation files, or building i18n into an app.
- `claude-skills/inbox-setup` — Use when setting up email triage for the first time, before inbox-triage, or when priorities change.
- `claude-skills/inbox-triage` — Use when the user wants their inbox processed ('triage my inbox', 'check my email').
- `claude-skills/incident-commander` — Use when declaring or running a production incident or outage, or writing its post-incident review.
- `claude-skills/incident-response` — Handle a suspected security breach: triage, SEV1-SEV4 severity, escalation and forensic evidence, per NIST SP 800-61.
- `claude-skills/information-security-manager-iso27001` — Use when designing or running an ISO 27001 ISMS in HealthTech or MedTech: risk assessment, control implementation, certification or securit…
- `claude-skills/internal-comms` — Use when announcing a reorg, tool rollout, policy change, leadership change, layoff or acquisition internally.
- `claude-skills/internal-narrative` — Use when preparing an all-hands, investor update, recruiting pitch or crisis message, or when stories told to different audiences drift apa…
- `claude-skills/interview` — Use when someone has an agent idea to scope before launch ('help me scope an agent').
- `claude-skills/interview-mapper` — Use when coding or making sense of one interview transcript (customer, JTBD, expert, usability, exit).
- `claude-skills/interview-system-designer` — Use when designing a hiring loop, competency matrix, scoring rubric or question bank, or checking interviewer calibration.
- `claude-skills/intl-expansion` — Use when expanding to a new country: market selection, entry mode, localization, regulation and regional go-to-market.
- `claude-skills/isms-audit-expert` — Use for ISO 27001 audit work: internal or surveillance audits, Annex A control evidence, Statement of Applicability, nonconformities, Stage…
- `claude-skills/iso13485-audit-prep` — Use for /compliance-os:iso13485-audit-prep, or before an ISO 13485 internal audit or DHF closure.
- `claude-skills/iso27001-audit-prep` — Use for /compliance-os:iso27001-audit-prep, or before an ISO 27001 internal, surveillance or stage 1 audit.
- `claude-skills/iso42001-specialist` — Use for ISO/IEC 42001 AI management system work: gap analysis against Clauses 4-10, the AI risk register and Annex A controls, or the inter…
- `claude-skills/jira-expert` — Jira setup and queries: JQL, workflows, custom fields, automation, dashboards.
- `claude-skills/karpathy-coder` — Check a diff for overbuilt code: hidden assumptions, needless abstraction, non-surgical changes, unverified goals (Karpathy's four principl…
- `claude-skills/knowledge-ops` — Use when writing, checking or cleaning up SOPs and runbooks.
- `claude-skills/kubernetes-operator` — Use when building a Kubernetes operator or CRD (controller-runtime, kubebuilder, operator-sdk, KOPF), before writing the controller.
- `claude-skills/landing` — Use when asked for a premium single-file HTML landing page with 3D CSS, GSAP scroll effects and parallax.
- `claude-skills/landing-page-generator` — Use when asked for a landing, marketing or campaign page as a Next.js TSX component with Tailwind.
- `claude-skills/launch-strategy` — Plan a product or feature launch: readiness score and a phased plan by channel.
- `claude-skills/linkedin-analytics` — Use when someone asks why their LinkedIn reach dropped, which posts worked, whether a pattern is real or how to test one.
- `claude-skills/linkedin-content` — Write, edit or review a LinkedIn post: story, how-to, carousel, video script or poll.
- `claude-skills/linkedin-engagement` — Use for LinkedIn comments, connection notes, DMs or outreach plans, or checking outreach volume is safe.
- `claude-skills/linkedin-profile` — Use when auditing or rewriting a LinkedIn profile (headline, About, experience, Featured).
- `claude-skills/linkedin-skills` — Use for any organic LinkedIn growth request (strategy, profile, posts, cadence, outreach, analytics).
- `claude-skills/linkedin-strategy` — Build a LinkedIn plan rather than a post: content pillars, positioning, a sustainable cadence, whether to start a newsletter.
- `claude-skills/litreview` — Use when starting a literature review or a literature-based project.
- `claude-skills/llm-cost-optimizer` — Use whenever an LLM feature is being built or its costs come up (model choice, prompt caching, token limits, per-feature spend).
- `claude-skills/llm-wiki` — Use when building or maintaining an Obsidian second brain that an LLM keeps up to date, or when ingesting a paper, article or book into it.
- `claude-skills/local-seo-manager` — Use for any local business's Google Business Profile, Maps ranking, service-area pages, citations or review replies, before writing.
- `claude-skills/loop-library` — Discover, find, compare, audit, repair, adapt, and design repeatable AI-agent loops with explicit triggers, actions, verification, stopping…
- `claude-skills/ma-playbook` — Buy a company or sell yours: diligence, valuation, terms, integration.
- `claude-skills/markdown-html-orchestrator` — Use when the user wants a markdown file turned into a single-file interactive HTML page (document, code review or slide deck).
- `claude-skills/market-research` — Use for market sizing (TAM, SAM, SOM both top-down and bottom-up), survey sample sizes or segment scoring.
- `claude-skills/marketing-context` — Use at the start of any marketing project, or when ICP, positioning or brand voice are missing, before other marketing skills.
- `claude-skills/marketing-demand-acquisition` — Use when planning demand generation, paid acquisition across Google, LinkedIn and Meta, or a marketing budget, before allocating spend.
- `claude-skills/marketing-ideas` — Use when asked for marketing or growth ideas for a SaaS or software product.
- `claude-skills/marketing-ops` — Use when a marketing request spans several skills (a campaign across content, SEO, CRO and channels) or it is unclear which skill fits.
- `claude-skills/marketing-psychology` — Apply persuasion and behavioral science ethically to a page, offer or campaign, from 70+ mental models.
- `claude-skills/marketing-skills` — Use when looking for which of the 44 marketing skills fits a task.
- `claude-skills/marketing-strategy-pmm` — Use for product positioning, ICP, competitive battlecards or a go-to-market plan, before drafting.
- `claude-skills/mcp-oauth-triage` — Use when an MCP connector that used to authenticate now fails (tool calls 401 after a good token exchange, breaks after refresh, returns an…
- `claude-skills/mcp-server-builder` — Use when exposing an API as an MCP server or scaffolding a new MCP server in Python or TypeScript, before hand-writing tool wrappers.
- `claude-skills/md-document` — Use when converting long-form markdown (spec, RFC, report, plan) into a single-file HTML page with sticky TOC, search and code-copy.
- `claude-skills/md-review` — Use when converting a markdown code review with diff blocks and severity callouts into a two-column HTML review.
- `claude-skills/md-slides` — Turn a markdown file into a single-file HTML slide deck with keyboard navigation, presenter notes and print-to-PDF.
- `claude-skills/mdr-745-specialist` — Use for EU MDR 2017/745 work: device classification under Annex VIII, technical file gaps (Annex II/III), clinical evaluation, PMS and PSUR…
- `claude-skills/meeting-analyzer` — Use when the user shares meeting transcripts (.vtt, .srt, .txt, Otter, Granola, Zoom) or asks how they come across in meetings.
- `claude-skills/meetings` — Use when someone wants to decide whether a meeting is worth calling, price a meeting in dollars, build a timeboxed agenda with desired outc…
- `claude-skills/memory-engineering` — Use before adding memory to an agent or when a memory store keeps growing (long context vs RAG vs graph vs agentic memory, what to expire).
- `claude-skills/memory-review` — Review what the agent has learned in auto-memory: what to promote to permanent rules, stale entries to prune, duplicates to merge.
- `claude-skills/memory-status` — Health check of agent auto-memory: line counts, topic files, capacity, stale entries and what to prune.
- `claude-skills/merge` — Use to land the winning AgentHub branch, archive the others and clean up worktrees.
- `claude-skills/meta-research` — Use when a wrong answer is expensive: strategy research, comparing several products or markets, validating a hypothesis with outside data.
- `claude-skills/migrate` — Use when moving tests from Cypress or Selenium to Playwright ('migrate tests', 'convert tests', 'replace selenium').
- `claude-skills/migration-architect` — Plan a migration with zero or minimal downtime: phased plan, compatibility check, rollback scripts, for schemas, databases and services.
- `claude-skills/minimalist` — Write the least code: no over-engineering, fewer dependencies.
- `claude-skills/monorepo-navigator` — Use for Turborepo, Nx, pnpm-workspace or Lerna setup, affected-only builds, remote caching or a multi-repo to monorepo move.
- `claude-skills/month-end-close` — Use when running, planning or speeding up a month-end (or quarter-end) close — building or reviewing the close checklist and calendar, reco…
- `claude-skills/ms365-tenant-manager` — Use for Microsoft 365 tenant administration (Entra ID users, Exchange Online, Teams, licenses, Conditional Access, compliance reports).
- `claude-skills/named-persona-adversarial-review` — Use when a PR has architectural or UX impact, or automated review feels generic, and you want it reviewed through named engineers' document…
- `claude-skills/notebooklm` — Use for anything in Google NotebookLM: querying notebooks, adding sources, generating Audio or Video Overviews, reports, flashcards or slid…
- `claude-skills/observability-designer` — Use when adding metrics, logs and traces to a service, fixing noisy alerts or designing dashboards.
- `claude-skills/office-hours` — Founder advice after six YC-style questions.
- `claude-skills/onboard` — Use for /cs-onboard, or when the virtual C-suite lacks company context.
- `claude-skills/onboarding-cro` — Use when activation, time-to-value or a first-run experience after signup needs work, before redesigning it.
- `claude-skills/org-health-diagnostic` — Use for a whole-company health check before a board review or when functions seem at risk.
- `claude-skills/page-cro` — Fix a page that is not converting: section by section audit with fixes ranked by impact.
- `claude-skills/paid-ads` — Use for paid campaign strategy on Google, Meta, LinkedIn or X: structure, targeting, bids, retargeting and budgets.
- `claude-skills/partnerships-architect` — Use when deciding whether to sign a partner, at which tier (referral, reseller, OEM, SI, alliance), with what joint GTM and revshare.
- `claude-skills/passive-deal-screener` — Use when a passive investor shares a private deal (syndication, preferred equity, bridge fund, private credit) to screen as an LP.
- `claude-skills/patent` — Use for prior-art search, freedom-to-operate, patent landscape, acquisition diligence or litigation prior art.
- `claude-skills/paywall-upgrade-cro` — Use when designing or fixing an in-app paywall, upgrade modal, feature gate or trial-expiry screen.
- `claude-skills/performance-profiler` — Use for a slow endpoint, memory leak, CPU spike, large bundle or performance budget in Node.js, Python or Go, before optimizing.
- `claude-skills/pm-skills` — Router for project-management skills: sprints, portfolio health, Jira, Confluence, stakeholder comms, plus a delivery loop.
- `claude-skills/popup-cro` — Use when creating or fixing a popup, modal, exit-intent, slide-in or banner meant to convert.
- `claude-skills/post-mortem` — Use for /c-level-agents:post-mortem, or when a decision hits its 90-day review or kill criteria.
- `claude-skills/postmortem` — Use after a failed launch, missed quarter or bad hire.
- `claude-skills/pr-review-expert` — File-by-file pull request review for bugs, security and quality, with a merge verdict.
- `claude-skills/pricing-strategist` — Use when choosing or revisiting pricing: seat, usage, value-based, freemium or hybrid, Van Westendorp willingness-to-pay analysis, or Good/…
- `claude-skills/pricing-strategy` — Use for SaaS pricing tiers, value metric, packaging, a pricing page or a price increase, before proposing numbers.
- `claude-skills/process-mapper` — Use when documenting an end-to-end business process (procurement, onboarding, handoffs) and finding where work waits.
- `claude-skills/procurement-optimizer` — Cut spend on software and suppliers: SaaS audit, category spend review, slow purchasing cycles, supplier consolidation.
- `claude-skills/product-analytics` — Use when defining product KPIs, building metric dashboards, running cohort or retention analysis, or interpreting feature adoption trends a…
- `claude-skills/product-discovery` — Validate product ideas: map assumptions, plan discovery sprints, test problem-solution fit.
- `claude-skills/product-manager-toolkit` — PM toolkit: RICE prioritization, customer interview synthesis, PRDs and go-to-market.
- `claude-skills/product-research` — Use when planning or synthesizing user research: choosing the method, deciding how many participants, or turning coded notes into insights.
- `claude-skills/product-skills` — Use when a product request needs routing across the product-team skills (prioritization, OKRs, UX research, experiments, discovery, roadmap…
- `claude-skills/product-strategist` — Head of Product: quarterly OKRs cascaded from company to team, product vision, roadmap, team structure.
- `claude-skills/programmatic-seo` — Use when building many SEO pages from a template and data (location, integration, comparison or directory pages), before generating them.
- `claude-skills/promote` — Graduate a proven pattern from auto-memory (MEMORY.md) to CLAUDE.md or .claude/rules/ for permanent enforcement.
- `claude-skills/prompt-engineer-toolkit` — Use when a marketing team's AI prompts need testing, versioning or governance, before shipping a prompt.
- `claude-skills/prompt-governance` — Use when prompts run in production and need versioning, a registry, A/B tests, regression checks or an eval pipeline.
- `claude-skills/pulse` — Use for what people are saying right now about a topic (trends, sentiment, complaints, tool comparisons) across Reddit, Hacker News and the…
- `claude-skills/pw` — Use for any Playwright or end-to-end browser testing work: writing tests, fixing flaky ones, migrating from Cypress or Selenium, CI setup,…
- `claude-skills/pw-init` — Use when setting up Playwright in a project ('set up playwright', 'add e2e tests', 'configure playwright', 'init playwright').
- `claude-skills/pw-review` — Use when reviewing Playwright tests for quality ('review tests', 'audit tests', 'playwright best practices check').
- `claude-skills/qms-audit-expert` — Use for ISO 13485 internal audits: planning the program, running an audit, classifying findings or preparing for an external audit.
- `claude-skills/quality-documentation-manager` — Use for QMS document control: numbering, versioning, change control or 21 CFR Part 11 e-signatures.
- `claude-skills/quality-manager-qmr` — Use for QMR duties under ISO 13485 5.5.2: management review, quality policy and objectives, quality KPIs and cost of quality.
- `claude-skills/quality-manager-qms-iso13485` — Build or maintain an ISO 13485 medical device QMS: design, documentation, CAPA, audit prep.
- `claude-skills/ra-qm-skills` — Router for regulatory and quality skills: ISO 13485, MDR, FDA, ISO 14971, CAPA, ISO 27001, ISO 42001, EU AI Act, GDPR, SOC 2.
- `claude-skills/rag-architect` — Design a RAG pipeline: chunk size, embedding model, vector database and retrieval quality metrics.
- `claude-skills/red-green-proof` — Turns a suspected bug into a proven one.
- `claude-skills/red-team` — Use when planning or running an authorized red team engagement or attack path analysis.
- `claude-skills/referral-program` — Use when designing or fixing a referral, affiliate or ambassador program, before setting rewards.
- `claude-skills/reflect` — Use when the user says 'step back', 'zoom out', 'are we on track' or 'sanity check this', or work has gone deep into details without a chec…
- `claude-skills/regulatory-affairs-head` — Use for medical device market access strategy: FDA 510(k), De Novo or PMA packages, CE marking under MDR, pre-sub meetings, agency deficien…
- `claude-skills/remember` — Save something important to auto-memory with a timestamp and context.
- `claude-skills/report` — Summarize Playwright results.
- `claude-skills/research` — Use for any research request that doesn't clearly match a research specialist ('research X', 'look into Y').
- `claude-skills/research-finance` — Use for R&D program money: multi-period budgets with indirect cost split, burn and runway against milestones, or capitalize vs expense rout…
- `claude-skills/research-ops-skills` — Use when an enterprise research request needs routing (clinical study design, R&D finance, market sizing, user research): 'what sample size…
- `claude-skills/research-summarizer` — Use when summarizing a research paper, article or report, comparing several sources or extracting citations into a brief.
- `claude-skills/revenue-operations` — Check sales pipeline and forecasts: pipeline coverage, forecast accuracy, magic number, CAC payback.
- `claude-skills/rfp-responder` — Use when an RFP, RFI, RFQ or security or vendor questionnaire arrives.
- `claude-skills/risk-management-specialist` — Use for ISO 14971 medical device risk management: hazard analysis, FMEA, fault trees, risk controls, benefit-risk or residual risk.
- `claude-skills/roadmap-communicator` — Write roadmap narratives, release notes, changelogs, stakeholder updates.
- `claude-skills/roast` — Roast an idea: a 5-angle panel (Critic, Champion, Analyst, Investigator, Customer) attacks it, then a Judge returns one GO / RESHAPE / KILL…
- `claude-skills/run-without-you` — Use when a graded managed agent should run on a schedule, on an event trigger or on demand ('run it every morning').
- `claude-skills/runbook-generator` — Use when a service needs runbooks for deploy, incident response, maintenance or rollback, before launch.
- `claude-skills/saas-metrics-coach` — Use when someone shares SaaS revenue or customer numbers, or asks about ARR, MRR, churn, LTV, CAC, NRR or how their SaaS is doing.
- `claude-skills/saas-scaffolder` — Use when starting a new SaaS app with auth, database, Stripe billing and a dashboard (Next.js App Router, TypeScript, Tailwind, shadcn/ui,…
- `claude-skills/sales-engineer` — Use for pre-sales work: RFP coverage gaps, competitive feature matrices or planning and scoring a proof of concept.
- `claude-skills/scenario-war-room` — Use for compound what-if questions ('what if X and Y both happen?') with major downside across functions.
- `claude-skills/schema-markup` — Use for any JSON-LD, schema.org, rich-result or structured-data request, before writing markup.
- `claude-skills/scrum-master` — Use for sprint and team analytics: velocity forecasts, sprint health, retrospectives, burndown or blockers.
- `claude-skills/secrets-vault-manager` — Use when setting up HashiCorp Vault, AWS Secrets Manager, Azure Key Vault or GCP Secret Manager, rotating secrets or auditing secret access.
- `claude-skills/security-guidance` — Use when installing or tuning the PreToolUse security hook that warns before Claude writes command injection, XSS, SQL injection, unsafe de…
- `claude-skills/security-pen-testing` — Authorized penetration testing of an app or API: vulnerability scans, OWASP Top 10 checks, dependency audits and a pentest report.
- `claude-skills/self-eval` — Grade finished work honestly on two axes with a devil's-advocate pass against inflation.
- `claude-skills/self-improving-agent` — Curate what the agent has learned into durable project knowledge.
- `claude-skills/senior-architect` — System architecture decisions with a written rationale: monolith vs microservices, database choice, scaling limits, ADRs, Mermaid diagrams.
- `claude-skills/senior-backend` — Build and fix backend services: REST or GraphQL APIs, auth, microservices, PostgreSQL queries, migrations and load tests.
- `claude-skills/senior-computer-vision` — Computer vision models: object detection, segmentation, training a custom model, and optimizing or deploying inference (YOLO, DETR, SAM, ON…
- `claude-skills/senior-data-engineer` — Data pipelines: Airflow DAGs, Spark, dbt, Kafka, ETL/ELT, data quality checks.
- `claude-skills/senior-data-scientist` — Design experiments and analyze tabular data: A/B tests, causal inference, feature engineering, model evaluation.
- `claude-skills/senior-devops` — Set up CI/CD pipelines, infrastructure as code, containers and deployments on AWS, GCP or Azure.
- `claude-skills/senior-frontend` — Build and review React, Next.js, TypeScript or Tailwind frontends: components, scaffolding, performance and bundle size.
- `claude-skills/senior-fullstack` — Start a fullstack project or audit a codebase: pick a stack (Next.js, FastAPI, MERN, Django), scaffold it and score code quality.
- `claude-skills/senior-ml-engineer` — Use for putting ML models or LLM features into production: deployment, MLOps, drift monitoring, RAG pipelines, LLM API cost and retries.
- `claude-skills/senior-pm` — Project and portfolio management for multi-workstream programs: plans, status reports, risk registers, capacity, executive reporting.
- `claude-skills/senior-prompt-engineer` — Improve prompts and measure LLM quality: fix inconsistent prompts, build eval sets, score RAG retrieval, check agent tool configs.
- `claude-skills/senior-qa` — Write and improve tests for React or Next.js apps: Jest, React Testing Library, MSW mocks, Playwright E2E, coverage gaps.
- `claude-skills/senior-secops` — Find and fix application security problems: security reviews, CVE remediation, hardening, secrets and auth, SOC 2, PCI-DSS, HIPAA and GDPR…
- `claude-skills/senior-security` — Check if a design or code is secure: STRIDE threat model, DREAD risk scores, leaked secret scan.
- `claude-skills/seo-audit` — Find why a site is not ranking: technical SEO, on-page issues, meta tags, site health.
- `claude-skills/session-handoff` — Write a handoff document so a fresh session or another agent can pick up exactly where this one left off: goal, current state, decisions, n…
- `claude-skills/setup` — Use for /autoresearch-agent:setup, or to start a new autoresearch experiment: target, eval command, metric, direction, evaluator.
- `claude-skills/ship-gate` — Use before deploying or going live ('am I ready to ship', 'can I deploy', 'preflight check').
- `claude-skills/signup-flow-cro` — Use when signup, registration or trial-start conversion is low or a signup flow is being designed.
- `claude-skills/site-architecture` — Use for URL structure, navigation, internal linking, hub pages or orphan pages, or when SEO problems are structural.
- `claude-skills/skill-retro` — Use when the user wants their skills graded from real session history, asks which installed skills actually work, or wants evidence-backed…
- `claude-skills/skill-security-auditor` — Use before installing any skill or plugin from an untrusted source, or when asked if a skill is safe.
- `claude-skills/skill-tester` — Use when authoring or auditing a skill in this ecosystem, before release.
- `claude-skills/skillopt-sleep` — Use when the user wants their Claude agent to self-improve from past usage, asks about a nightly/offline 'sleep' or 'dream' cycle, memory/s…
- `claude-skills/slo-architect` — Use when defining or reviewing SLOs, SLIs, error budgets or burn-rate alerts.
- `claude-skills/snowflake-development` — Use for Snowflake work: SQL, Dynamic Tables, Streams and Tasks, Cortex AI functions and agents, Snowpark Python, dbt on Snowflake, or Snowf…
- `claude-skills/soc2-audit-prep` — Use for /compliance-os:soc2-audit-prep, or before or during a SOC 2 Type II observation period.
- `claude-skills/soc2-compliance` — Use when the user asks to prepare for SOC 2 audits, map Trust Service Criteria, build control matrices, collect audit evidence, perform gap…
- `claude-skills/social-content` — Write a LinkedIn post, X thread, Instagram, TikTok or Facebook post with each platform's hook, length and format.
- `claude-skills/social-media-analyzer` — Score social performance: engagement rate, reach, ROI per platform, benchmarks.
- `claude-skills/social-media-manager` — Plan social media: strategy, content calendar, community management, follower growth.
- `claude-skills/spawn` — Launch the competing agents in isolated worktrees.
- `claude-skills/spec-driven-workflow` — Use when a feature should be specified before coding (acceptance criteria, spec-first, tests from specs).
- `claude-skills/spec-to-repo` — Use when the user says 'build me an app', 'create a project from this spec', 'scaffold a new repo', 'generate a starter', 'turn this idea i…
- `claude-skills/spinning-up-deep-rl` — Learn or apply deep reinforcement learning with OpenAI Spinning Up: policy gradients, VPG, PPO, SAC, TD3, DDPG, TRPO.
- `claude-skills/sql-database-assistant` — Write, fix and speed up SQL: slow queries, EXPLAIN plans, indexes, ORM migrations (Prisma, Drizzle, SQLAlchemy).
- `claude-skills/stage-launch` — Use when a managed-agent build sheet is ready to launch ('launch it', 'deploy the agent').
- `claude-skills/statistical-analyst` — Is a difference real?
- `claude-skills/stock-analysis` — Analyze, research or value a listed stock or company (US, global, NSE or BSE) with verified data, ratios, scores and valuation.
- `claude-skills/strategic-alignment` — Use when teams pull in different directions, OKRs don't connect or departments optimize locally.
- `claude-skills/stress-test` — Stress-test a plan built on untested assumptions.
- `claude-skills/strict-api` — Use when the user says 'no hallucinations', 'verify APIs' or 'don't invent functions', or code depends on a library version you have not ch…
- `claude-skills/stripe-integration-expert` — Use for any Stripe integration: subscriptions, trials, proration, checkout, usage billing, webhooks, customer portal or invoicing in Next.j…
- `claude-skills/swedish-mentor` — Use when someone learning Swedish wants a learning path or YouTube clips and podcasts matched to their CEFR level and skill (SFI, Lätt Sven…
- `claude-skills/syllabus` — Use when the user shares a course syllabus or outline and wants supplementary readings.
- `claude-skills/tc-tracker` — Use when tracking technical changes as records, or handing work between AI sessions with a change record.
- `claude-skills/tdd-guide` — Test-first development and test generation for Jest, Pytest, JUnit, Vitest or Mocha: red-green-refactor, fixtures and mocks, coverage gaps.
- `claude-skills/team-communications` — Use for any internal communication: 3P updates, weekly or status reports, newsletters, FAQs, incident reports, leadership updates ('write m…
- `claude-skills/tech-debt-tracker` — Find, rank and track tech debt in a codebase.
- `claude-skills/tech-stack-evaluator` — Compare frameworks or tech stacks before committing: side-by-side scoring, total cost of ownership, ecosystem health and migration risk.
- `claude-skills/terraform-patterns` — Use for any Terraform module, state backend, provider setup or IaC security review, before editing .tf files.
- `claude-skills/testrail` — Use when syncing Playwright tests with TestRail ('testrail', 'sync test cases', 'push results to testrail', 'import from testrail').
- `claude-skills/threat-detection` — Use when hunting threats, sweeping IOCs or looking for anomalies in logs and telemetry.
- `claude-skills/ui-design-system` — Use when building a design system: tokens, component docs, responsive scales or developer handoff.
- `claude-skills/universal-scraping-architect` — Build a scraper or extractor for sites, PDFs or paginated APIs and validate the fields (Firecrawl or local Python).
- `claude-skills/ux-researcher-designer` — UX research: personas, journey maps, usability test plans, synthesis.
- `claude-skills/vendor-management` — Use when scoring or auditing vendors: scorecards, SLA compliance and service credits, third-party risk tier or a tier-1 vendor review.
- `claude-skills/video-content-strategist` — Use for video strategy, scripts, YouTube SEO, short-form pipelines (Reels, TikTok, Shorts) or turning long content into video, before scrip…
- `claude-skills/vpe-advisor` — Use when delivery is slowing, eng hiring is broken, team structure is unclear or you need to decide when to add an eng manager.
- `claude-skills/vpe-review` — Challenge a plan on delivery speed, eng hiring, team structure or on-call.
- `claude-skills/webinar-marketing` — Use when planning, promoting or fixing a webinar or virtual event (registrations, show-up, follow-up, conversion).
- `claude-skills/weekly-review` — Use when someone wants to run a weekly review, close open loops, audit stalled projects and commitments, get their system back to trusted,…
- `claude-skills/workflow-builder` — Use when writing or running a Claude Code Workflow-tool script (.js in .claude/workflows/) for fan-out, pipeline, loop or judge-panel sub-a…
- `claude-skills/wrap-up` — Use when closing out a launched managed agent ('wrap up', 'what do I own now').
- `claude-skills/write-a-skill` — Create new agent skills with proper structure, progressive disclosure, and bundled resources.
- `claude-skills/x-twitter-growth` — Use for growing on X/Twitter: tweets, threads, profile audit, competitors or posting plan.
- `claude-skills/youtube-full` — Use for any YouTube URL, video ID or @handle, or a request for transcripts, video search, channel, playlist or new-upload monitoring.
- `claude-skills/zero-hallucination-coder` — Use before high-stakes or multi-file coding (auth, databases, migrations), or when asked to plan carefully and avoid invented APIs.
- `marketing/ab-testing` — When the user wants to plan, run, or read A/B tests, or asks a judgement call on one: is the result real, can we stop, which version won, i…
- `marketing/ad-creative` — When the user wants to write or judge ad creative, or asks which ad, hook, or angle to run or kill: headlines, primary text, and variations…
- `marketing/ads` — When the user wants to plan, run, or fix paid ads on Google, Meta, and LinkedIn, or asks a judgement call on them: are ads worth it, which…
- `marketing/ai-seo` — When the user wants to get cited and recommended in AI answers (ChatGPT, Perplexity, AI Overviews), or asks why AI cites a competitor, whic…
- `marketing/analytics` — When the user wants to set up or audit analytics, or asks whether a metric or number is calculated right, what to track, or how to name eve…
- `marketing/aso` — When the user wants to audit or optimize an App Store or Google Play listing, or asks which title, keywords, or screenshots to pick or why…
- `marketing/attribution` — When the user wants to work out which marketing drives revenue, or asks whether a channel is really working, which numbers to trust, or how…
- `marketing/churn-prevention` — When the user wants to reduce churn, or asks why customers cancel, whether to offer a discount or pause: cancellation flows, exit surveys,…
- `marketing/co-marketing` — When the user wants co-marketing partners or joint campaigns, or asks whether a partner fits, a size mismatch matters, or how to split work…
- `marketing/cold-email` — When the user wants to write or run B2B cold outbound, or asks whether an opener, reason to reach out, or email works or why nobody replies…
- `marketing/community-marketing` — When the user wants to build or grow an online community, or asks whether a community is worth it, where to host it, or why members stay qu…
- `marketing/competitor-profiling` — When the user wants to research competitors into dated profiles, or asks what a rival charges, claims, or is doing, or whether a conclusion…
- `marketing/competitors` — When the user wants to create or audit comparison and alternative pages ('X vs Y', 'X alternative', 'best X alternatives'), or asks what a…
- `marketing/content-strategy` — When the user wants to plan content, or asks which topic or piece to prioritize, what to write about, or why posts bring no customers: topi…
- `marketing/conversion-tracking` — When the user wants to set up, audit, or fix conversion tracking to Google Ads, Meta, GA4, LinkedIn, and TikTok, or asks why conversions ar…
- `marketing/copy-editing` — When the user wants to edit, tighten, proofread, or refresh existing copy, or asks whether to keep, cut, or change a line in it, without re…
- `marketing/copywriting` — When the user wants to write or rewrite page copy (homepage, landing, pricing, feature), or asks which headline, promise, or message to lea…
- `marketing/cro` — When the user wants more conversions from a page or form, or asks why a page isn't converting, what to change first, or whether to add or r…
- `marketing/customer-research` — When the user wants to run or synthesize customer research, or asks what customer quotes, reviews, or feedback really mean, what is safe to…
- `marketing/directory-submissions` — When the user wants to list a product in startup, SaaS, AI, MCP, and review directories, or asks which directories are worth it or whether…
- `marketing/emails` — When the user wants to create or improve automated email sequences, or asks what to send, when, or whether an email or flow is working: wel…
- `marketing/events` — When the user wants to plan, run, sponsor, or speak at events, or asks whether an event or booth is worth the money: webinars, conferences,…
- `marketing/free-tools` — When the user wants to plan or build a free tool as marketing, or asks whether a tool idea is worth building or which one to pick: calculat…
- `marketing/image` — When the user wants to create, generate, edit, or optimize marketing images, or asks which approach to take (generate, design, or photograp…
- `marketing/influencer-marketing` — When the user wants creator, influencer, or ambassador partnerships, or asks which creators fit, what to pay, which rights to buy, or wheth…
- `marketing/launch` — When the user wants to plan a product or feature launch, or asks whether it's ready, when to announce, or how to get noticed: Product Hunt,…
- `marketing/lead-magnets` — When the user wants to plan or improve a lead magnet, or asks what to give away for emails or how much to ask in return (gating, form field…
- `marketing/link-building` — When the user wants backlinks and mentions that lift rankings and AI citations, or asks how to get sites to link or whether a link tactic i…
- `marketing/marketing-council` — When the user wants several expert takes on a marketing decision, or asks what a famous marketer would say about it: a simulated board (Set…
- `marketing/marketing-ideas` — When the user wants marketing ideas or growth tactics for a software product, or asks what to try to get attention or the next customers wi…
- `marketing/marketing-loops` — When the user wants a recurring marketing job an AI agent runs on a cadence or trigger, or asks what a weekly or daily automated check shou…
- `marketing/marketing-plan` — When the user wants a full marketing or go-to-market plan for a client, an advised company, or their own product, or asks how to sequence o…
- `marketing/marketing-psychology` — When the user wants to apply psychology to marketing, or asks why buyers behave or value things as they do, or whether a persuasion tactic…
- `marketing/offers` — When the user wants to design or improve the offer itself, or asks why it isn't selling or how to add urgency honestly: value stacking, bon…
- `marketing/onboarding` — When the user wants better onboarding and activation, or asks why new users don't stick or what the first session should do: first-run expe…
- `marketing/paywalls` — When the user wants to create or improve in-app paywalls and upgrade moments, or asks when or how hard to ask free users to pay (after they…
- `marketing/popups` — When the user wants to create or improve popups, modals, slide-ins, sticky bars, and banners, or asks whether one will help or annoy and wh…
- `marketing/pricing` — When the user wants to set pricing and packaging, or asks what to charge, whether to raise prices, or how to move existing customers: tiers…
- `marketing/product-marketing` — When the user wants to create or update the product marketing context doc (.agents/product-marketing.md), or asks what belongs in it or whe…
- `marketing/programmatic-seo` — When the user wants SEO pages at scale from templates and data, or asks whether a page set will rank or look thin: location, integration, c…
- `marketing/prospecting` — When the user wants to find and qualify prospects for outbound, or asks who to target first, which signal to prioritize, or where to spot b…
- `marketing/public-relations` — When the user wants press and media coverage, or asks what to say to a reporter, whether a story is newsworthy, or how to handle a crisis:…
- `marketing/referrals` — When the user wants referral and affiliate programs or word of mouth, or asks what to reward, how much to pay, or which loop to start with:…
- `marketing/reverse-engineer-marketing` — When the user wants to know how another company grew and what to copy, or asks what a competitor did and when: a dated log of their moves a…
- `marketing/revops` — When the user wants to design revenue operations, or asks when a lead is ready for sales or why sales and marketing disagree on lead qualit…
- `marketing/sales-enablement` — When the user wants sales collateral, or asks what to give a champion or rep, or how to answer an objection or make the case: decks, one-pa…
- `marketing/schema` — When the user wants to add, fix, or validate schema markup (JSON-LD), or asks which type fits a page or whether some markup is allowed: pro…
- `marketing/seo-audit` — When the user wants to audit or diagnose SEO, or asks why traffic dropped, a page won't rank, or whether a setup like canonicals, hreflang,…
- `marketing/signup` — When the user wants better signup, registration, and trial start flows, or asks which fields or steps to cut or whether to require a card:…
- `marketing/site-architecture` — When the user wants to plan or restructure a website, or asks which pages they need or where something belongs: hierarchy, navigation, URL…
- `marketing/sms` — When the user wants SMS, MMS, or WhatsApp marketing, or asks whether texting is worth it or a message is allowed: abandoned cart, win-back,…
- `marketing/social` — When the user wants organic social content for LinkedIn, X, Instagram, TikTok, or Facebook, or asks what to post, which format to favor, or…
- `marketing/video` — When the user wants to create video with AI tools or code, or asks which approach to use (screen recording, AI avatar, generated, or templa…
- `pm-setup/competitive-analysis` — Activate on "analyze competitor", "competitive analysis", "compare us to [company]".
- `pm-setup/launch-checklist` — Activate on "launch checklist", "pre-launch check", "ready to launch?", "launch prep".
- `pm-setup/metrics-definer` — Activate on "define metrics", "what should I measure", "success metrics for [feature]", "KPIs for [initiative]".
- `pm-setup/prd-writer` — Activate on "write a PRD", "create a PRD", "draft a PRD", "PRD for [feature]", "spec out [feature]", or "one pager for [feature]".
- `pm-setup/sprint-planner` — Activate on "plan sprint", "sprint planning", "what should we work on", "organize the backlog".
- `pm-setup/user-research` — Activate on "synthesize research", "analyze interviews", "research findings", "interview synthesis".
- `pm-skills/acquisition-channel-advisor` — Evaluate acquisition channels using unit economics, customer quality, and scalability.
- `pm-skills/agent-orchestration-advisor` — Design multi-agent AI workflows with clear boundaries, handoffs, and monitoring.
- `pm-skills/ai-shaped-readiness-advisor` — Assess whether your product work is AI-first or AI-shaped.
- `pm-skills/altitude-horizon-framework` — Understand the PM-to-Director transition through altitude and horizon thinking.
- `pm-skills/ansoff-matrix` — Map evidence-backed growth options across the Ansoff Matrix with risk-rated sequencing.
- `pm-skills/autonomous-investigation` — The protocol behind every investigation skill.
- `pm-skills/battle-card-builder` — Research and draft a competitive battle card from public evidence — every claim labeled and sourced.
- `pm-skills/business-health-diagnostic` — Diagnose SaaS business health across growth, retention, efficiency, and capital.
- `pm-skills/company-intel` — Research a company, industry, or competitor set using web search and seven analytical lenses.
- `pm-skills/company-research` — Create a company research brief with executive quotes, product strategy, and org context.
- `pm-skills/competitive-analysis-process` — Orchestrate a complete competitive analysis across six steps, from landscape to strategic direction.
- `pm-skills/competitive-intel-watch` — Scheduled delta monitoring against a prior competitive snapshot.
- `pm-skills/competitive-research-snapshot` — Research a competitive landscape with cited snapshots, a comparison matrix, and so-what implications.
- `pm-skills/context-engineering-advisor` — Diagnose context stuffing vs.
- `pm-skills/customer-journey-map` — Create a customer journey map across stages, touchpoints, actions, emotions, and metrics.
- `pm-skills/customer-journey-mapping-workshop` — Run a customer journey mapping workshop with adaptive questions and outputs.
- `pm-skills/derisk-measurement-advisor` — Identify what to measure, test, or track to de-risk a product or AI idea.
- `pm-skills/director-readiness-advisor` — Guide the PM-to-Director transition across preparing, interviewing, landing, and recalibrating.
- `pm-skills/discovery-interview-prep` — Plan customer discovery interviews with the right goal, segment, constraints, and method.
- `pm-skills/discovery-process` — Run a full discovery cycle from problem hypothesis to validated solution.
- `pm-skills/eol-checklist` — Build a phase-gated EOL checklist sized to the sunset, with a named owner on every item.
- `pm-skills/eol-internal-enablement` — Build the support FAQ, sales talking points, and objection handling teams need before an EOL announcement.
- `pm-skills/eol-message` — Write a right-sized EOL announcement — brief notice through full phased comms — with rationale, customer impact, and next steps.
- `pm-skills/eol-process` — Run a product sunset end to end — decide, align, plan, prepare, announce, close.
- `pm-skills/eol-readiness-advisor` — Run a go/no-go assessment for retiring a product or feature, then right-size the effort.
- `pm-skills/eol-stakeholder-sequence` — Plan who to talk to about a sunset, in what order, and what each conversation must cover.
- `pm-skills/epic-breakdown-advisor` — Break down epics into user stories with Humanizing Work split patterns.
- `pm-skills/epic-hypothesis` — Frame an epic as a testable hypothesis with target user, expected outcome, and validation method.
- `pm-skills/executive-onboarding-playbook` — Plan a VP or CPO 30-60-90 day diagnostic onboarding path.
- `pm-skills/feature-investment-advisor` — Evaluate feature investments using revenue impact, cost structure, ROI, and strategy.
- `pm-skills/finance-based-pricing-advisor` — Evaluate pricing changes using ARPU, conversion, churn risk, NRR, and payback.
- `pm-skills/finance-metrics-quickref` — Look up SaaS finance metrics, formulas, and benchmarks fast.
- `pm-skills/incoming-request-advisor` — Decode an incoming message into a structured breakdown separating the literal ask from the job-to-be-done.
- `pm-skills/intel-discipline-advisor` — Triage a competitive or market question into the right intelligence disciplines, cadence, and executing skill.
- `pm-skills/intelligence-collection-disciplines` — Run competitive research like an intelligence agency: eight collection disciplines (OSINT to MASINT), signal-to-inference chains, and fusio…
- `pm-skills/jobs-to-be-done` — Uncover customer jobs, pains, and gains in a structured JTBD format.
- `pm-skills/lean-ux-canvas` — Guide teams through Lean UX Canvas v2.
- `pm-skills/lifecycle-play-advisor` — Diagnose where a product sits in its lifecycle and which play fits — extend, replace, or retire.
- `pm-skills/market-landscape-scan` — Map a market's segments, players, substitutes, and whitespace with cited evidence.
- `pm-skills/opportunity-solution-tree` — Build an Opportunity Solution Tree from outcomes to opportunities, solutions, and tests.
- `pm-skills/organic-growth-advisor` — Identify which organic growth path to pursue — new segments, geographies, channels, or products.
- `pm-skills/pestel-analysis` — Analyze political, economic, social, technological, environmental, and legal forces.
- `pm-skills/pestel-delta-monitor` — Quarterly re-scan of a prior PESTEL analysis.
- `pm-skills/pm-skill-creator` — Design a new PM skill through guided conversation.
- `pm-skills/pol-probe` — Define a Proof of Life probe to test a risky hypothesis cheaply.
- `pm-skills/pol-probe-advisor` — Select the right Proof of Life (PoL) probe based on hypothesis, risk, and resources.
- `pm-skills/porters-five-forces` — Read an industry's structure through Porter's Five Forces with documented signals per rating, ending at the profit pool.
- `pm-skills/positioning-statement` — Create a Geoffrey Moore-style positioning statement.
- `pm-skills/positioning-workshop` — Run a positioning workshop that surfaces target customer, unmet need, category, benefits, and differentiation.
- `pm-skills/prd-development` — Build a structured PRD that connects problem, users, solution, and success criteria.
- `pm-skills/press-release` — Write an Amazon-style press release that defines customer value before building.
- `pm-skills/pricing-packaging-tracker` — Track competitor pricing and packaging as a diffable time series.
- `pm-skills/prioritization-advisor` — Choose a prioritization framework based on stage, team context, and stakeholder needs.
- `pm-skills/problem-framing-canvas` — Guide teams through MITRE's Problem Framing Canvas.
- `pm-skills/problem-statement` — Write a user-centered problem statement with who is blocked, what they are trying to do, why it matters, and how it feels.
- `pm-skills/product-lifecycle-plays` — Map a product's lifecycle stage and choose between extension, replacement, and retirement plays.
- `pm-skills/product-sense-interview-answer` — Structure a spoken PM product-sense answer with assumptions, segmentation, pain-point prioritization, and MVP tradeoffs.
- `pm-skills/product-strategy-session` — Run an end-to-end product strategy session across positioning, discovery, and roadmap planning.
- `pm-skills/proto-persona` — Create a proto-persona from current research, market signals, and team knowledge.
- `pm-skills/recommendation-canvas` — Evaluate an AI product idea across outcomes, hypotheses, risks, and positioning.
- `pm-skills/roadmap-planning` — Plan a strategic roadmap across prioritization, epic definition, stakeholder alignment, and sequencing.
- `pm-skills/saas-economics-efficiency-metrics` — Evaluate SaaS unit economics and capital efficiency.
- `pm-skills/saas-revenue-growth-metrics` — Calculate SaaS revenue, retention, and growth metrics.
- `pm-skills/skill-authoring-workflow` — Turn raw PM content into a compliant, publish-ready skill.
- `pm-skills/stakeholder-engagement-advisor` — Plan engagement for a specific stakeholder.
- `pm-skills/stakeholder-identification` — Map every stakeholder before engaging anyone.
- `pm-skills/stakeholder-mapping` — Prioritize stakeholders using two complementary grids.
- `pm-skills/storyboard` — Create a six-frame storyboard that shows a user's journey from problem to solution.
- `pm-skills/swot-analysis` — Build an evidence-cited SWOT of one company — yours or a competitor's — from public sources, ending with the S-O/W-T crossings.
- `pm-skills/tam-sam-som-calculator` — Calculate TAM, SAM, and SOM with explicit assumptions, methods, and caveats.
- `pm-skills/user-story` — Create user stories with Mike Cohn format and Gherkin acceptance criteria.
- `pm-skills/user-story-mapping` — Create a user story map that lays out activities, steps, tasks, and release slices.
- `pm-skills/user-story-mapping-workshop` — Run a user story mapping workshop with adaptive questions and a structured map output.
- `pm-skills/user-story-splitting` — Break a large story or epic into smaller deliverable stories using proven split patterns.
- `pm-skills/voice-of-customer-miner` — Mine public reviews, app stores, and forums for unmet needs, competitor weaknesses, and switching triggers — with quoted evidence.
- `pm-skills/vp-cpo-readiness-advisor` — Guide the transition to VP or CPO across preparing, interviewing, landing, and recalibrating.
- `pm-skills/workshop-facilitation` — Facilitate workshop sessions in a one-step, multi-turn flow.
