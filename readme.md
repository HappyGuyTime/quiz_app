# Quiz App

Этот репозиторий содержит исходный код для FastAPI-сервиса, который предоставляет API для викторин. Включены инструкции по сборке и запуску Docker-контейнеров для этого сервиса и базы данных PostgreSQL.

## Клонирование репозитория на ваш компьютер

    ```bash
    git clone https://github.com/HappyGuyTime/quiz_app.git
    cd quiz_app
    ```

## Сборка и запуск Docker-контейнеров

   ```bash
   docker-compose up -d --build
   ```

## Пример POST запроса

 - curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 1}' http://localhost:8000/question/
