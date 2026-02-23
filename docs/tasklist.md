# План разработки

## Отчёт по прогрессу

| Итерация | Статус | Проверка |
|----------|--------|----------|
| 1. Бот и конфиг из .env | ✅ Готово | /start и ответ от модели; настройки из .env, .env.example |
| 2. Логирование | ✅ Готово | Логи в stdout с нужными событиями |
| 3. Сборка и деплой | ✅ Готово | make run, Docker, готовность к VPS |

Легенда: ⏳ Не начато · 🔄 В работе · ✅ Готово

---

## Итерации

### Итерация 1. Бот с ответом через LLM и конфиг из .env

- [x] Структура проекта по vision (bot/, main.py, pyproject.toml)
- [x] Зависимости: aiogram, openai, uv, загрузка .env (python-dotenv)
- [x] Точка входа: запуск бота, Long Polling
- [x] config.py: get_settings(), все настройки из окружения / .env
- [x] Хэндлер /start: приветствие, пустая история для user_id
- [x] Хранилище истории в памяти: dict[user_id, list]
- [x] llm.py: ask_llm(history, message) → str, Together AI (openai SDK + base_url)
- [x] Хэндлер текста: сообщение в историю → ask_llm (system_prompt + история) → ответ в историю → отправить пользователю
- [x] .env.example в репозитории, .env в .gitignore, без хардкода в коде

**Проверка:** /start → приветствие; текстовое сообщение → ответ от модели; запуск с .env, смена модели/промпта через .env без правок кода.

---

### Итерация 2. Логирование

- [x] logging.basicConfig в main.py, уровень из get_settings()
- [x] Логи: старт бота, входящее сообщение (user_id, текст), ошибки LLM
- [x] Формат и вывод в stdout по vision

**Проверка:** в консоли видны события при общении с ботом.

---

### Итерация 3. Сборка и деплой

- [x] Makefile: install, run, run-docker, lint, format
- [x] Dockerfile (python:3.11-slim, uv), docker-compose.yml
- [x] Запуск через make run и docker compose

**Проверка:** `make install && make run` и `make run-docker` — бот работает; готовность к выкладке на VPS.
