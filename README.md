# Тестовый проект "RandomUserGenerator"

###
    Api запросы из бесплатного проекта - https://randomuser.me/

## Установка зависимостей
    sudo apt install python3.11
```bash
python3.11 -m venv venv
source ./venv/bin/activate
pip install - r requirements.txt
pre-commit install

```
### Перед влитием в ветку выполнять:
```bash
pre-commit run --all-files <- самостоятельно проверяем свои коммиты
```

## Запуск тестов
```bash
pytest --env-cfg=env.dev.yaml - пример запуска теста из конфига env.dev.yaml
```
```
--env-cfg - это ключ на конфиг
```
