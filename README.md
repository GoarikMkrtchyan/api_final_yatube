# API Final

## Описание

Этот проект представляет собой REST API для социальной сети, где пользователи могут создавать и просматривать посты, оставлять комментарии, а также подписываться на других пользователей. API предоставляет удобные и безопасные методы для работы с данными, поддерживает аутентификацию через JWT, и имеет документацию с использованием ReDoc.

## Установка
1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:GoarikMkrtchyan/api_final_yatube.git
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd project_directory
    ```
3. Создайте и активируйте виртуальное окружение (рекомендуется):
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```
4. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
5. Примените миграции:
    ```sh
    python manage.py migrate
    ```
6. Создайте суперпользователя для доступа к админке (опционально):
    ```sh
    python manage.py createsuperuser
    ```
7. Запустите сервер:
    ```sh
    python manage.py runserver
    ```
## Примеры запросов к API

### Получение списка постов

```http
GET /api/v1/posts/
Проект разработан [Goarik](https://github.com/GoarikMkrtchyan).