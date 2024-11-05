# Yatube - платформа для тех, кому есть, что сказать.

### Пишите свои мысли, наблюдения, истории.
### Следите за интересными людьми, оставляйте свои комментарии.


Чтобы развернуть проект клонируйте репозиторий:
```
https://github.com/ElenaGruzintseva/api_final_yatube
```
Перейдите в папку проекта:
```
cd api_final_yatube
```
Создайте и активируйте виртуальное окружение:
```
python -m venv env
. venv/bin/activate
```
Установите зависимости:
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Запустите проект:
```
python manage.py runserver
```
Приверы запросов к API:
```
POST http://127.0.0.1:8000/api/v1/users/
{
    "username": "Ваше_имя",
    "password": "Ваш_пароль"
}
```
```
GET http://127.0.0.1:8000/api/v1/groups/
```
```
POST http://127.0.0.1:8000/api/v1/posts/
{
