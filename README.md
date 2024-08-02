# api_final
api final

## Описание
Этот проект представляет собой API для работы с постами, комментариями и подписками. Пользователи могут создавать и просматривать посты и комментарии, а также подписываться на других пользователей.

## Установка
1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:GoarikMkrtchyan/api_final_yatube.git
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd project_directory
    ```
3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
4. Примените миграции:
    ```sh
    python manage.py migrate
    ```
5. Запустите сервер:
    ```sh
    python manage.py runserver
    ```

## Примеры запросов к API

### Получение списка постов

```http
GET /api/posts/

Проект разработан [Goarik](https://github.com/GoarikMkrtchyan).