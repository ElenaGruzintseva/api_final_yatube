# Yatube

Yatube - платформа, где авторизованные пользователи могут публиковать посты с изображениями, подписываться на других авторов и оставлять свои комментарии. Анонимным пользователям доступно только чтение.

## Используемые технологии:
- Django
- DRF
- pytest
- djoser
- Pillow
- PyJWT

### Чтобы развернуть проект клонируйте репозиторий:
```
https://github.com/ElenaGruzintseva/api_final_yatube
```

Перейдите в папку проекта:
```
cd api_final_yatube
```

Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
. venv/bin/activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Выполните миграции:
```
python3 manage.py migrate
```

Запустите проект:
```
python3 manage.py runserver
```

Здесь доступна документация для API Yatube: http://127.0.0.1:8000/redoc/

Примеры запросов к API:
```
POST http://127.0.0.1:8000/api/v1/users/
{
    "username": "Ваше_имя",
    "password": "Ваш_пароль"
}
```

```
GET http://127.0.0.1:8000/api/v1/groups/

GET http://127.0.0.1:8000/api/v1/posts/

GET http://127.0.0.1:8000/api/v1/follow/
```

```
POST http://127.0.0.1:8000/api/v1/posts/
{
    "text": "Здесь текст вашего поста."
}
```

Автор: Elena Gruzintseva
https://github.com/ElenaGruzintseva
