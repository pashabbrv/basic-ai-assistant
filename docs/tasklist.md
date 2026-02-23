# План разработки

## Отчёт по прогрессу

| Итерация | Статус | Проверка |
|----------|--------|----------|
| 1. Бот с /start и LLM | ✅ Готово | /start → приветствие; сообщение → ответ от модели |
| 2. Конфиг из .env | ⏳ Не начато | Настройки из .env, есть .env.example |
| 3. Логирование | ⏳ Не начато | Логи в stdout с нужными событиями |
| 4. Сборка и деплой | ⏳ Не начато | make run, Docker, готовность к VPS |

Легенда: ⏳ Не начато · 🔄 В работе · ✅ Готово

---

## Итерации

### Итерация 1. Бот с ответом через LLM

- [x] Структура проекта по vision (bot/, main.py, pyproject.toml)
- [x] Зависимости: aiogram, openai, uv
- [x] Точка входа: запуск бота, Long Polling
- [x] config.py: минимум TELEGRAM_TOKEN (остальное можно хардкод на шаг)
- [x] Хэндлер /start: приветствие, пустая история для user_id
- [x] Хранилище истории в памяти: dict[user_id, list]
- [x] llm.py: ask_llm(history, message) → str, Together AI (openai SDK + base_url)
- [x] Хэндлер текста: сообщение в историю → ask_llm (system_prompt + история) → ответ в историю → отправить пользователю

**Проверка:** /start → приветствие; текстовое сообщение → ответ от модели.

---

### Итерация 2. Конфиг из .env

- [ ] pydantic-settings, get_settings() в config.py
- [ ] Все настройки из .env (токен, LLM_API_KEY, LLM_BASE_URL, MODEL_NAME, SYSTEM_PROMPT, LOG_LEVEL)
- [ ] .env.example в репозитории, .env в .gitignore
- [ ] Убрать хардкод из кода

**Проверка:** запуск с .env — бот работает; смена модели/промпта через .env без правок кода.

---

### Итерация 3. Логирование

- [ ] logging.basicConfig в main.py, уровень из get_settings()
- [ ] Логи: старт бота, входящее сообщение (user_id, текст), ошибки LLM
- [ ] Формат и вывод в stdout по vision

**Проверка:** в консоли видны события при общении с ботом.

---

### Итерация 4. Сборка и деплой

- [ ] Makefile: install, run, run-docker, lint, format
- [ ] Dockerfile (python:3.11-slim, uv), docker-compose.yml
- [ ] Запуск через make run и docker compose

**Проверка:** `make install && make run` и `make run-docker` — бот работает; готовность к выкладке на VPS.
