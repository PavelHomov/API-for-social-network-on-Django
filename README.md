# Проект API для социальной сети
![Примеры API](./media_for_readme/Presentation.gif)
![Примеры API](./media_for_readme/API1.png)
![Примеры API](./media_for_readme/API2.png)
## Описание
Проект представляет собой API на Django Rest Framework. В проекте можно создавать публикации, комментарии к ним, а также к другим созданным постам, оформить подписку на автора и, соответственно, отписаться от него.
В проекте нет фронтенда.
Аутентифицированные пользователи могут  изменять и удалять свой контент, в остальных случаях доступ предоставляется только для чтения.
После запуска проекта по адресу <http://127.0.0.1:8000/redoc/> будет доступна документация для API Yatube.

## Как запустить проект в Docker:

```
docker build -t my-django-app .
```

```
docker run -it --rm -p 8000:8000 my-django-app
```

Проект будет доступен по адресу <b>127.0.0.1:8000</b>

## Установка
Клонировать репозиторий и перейти в него в командной строке:
```text
git clone git@github.com:PavelHomov/API-for-social-network-on-Django.git
```
```text
cd social_network_api
```
Cоздать и активировать виртуальное окружение:
```text
python3 -m venv venv
```
```text
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```text
python3 -m pip install --upgrade pip
```
```text
pip3 install -r requirements.txt
```
Выполнить миграции:
```text
python3 manage.py makemigrations
python3 manage.py migrate
```
Запустить проект:
```text
python3 manage.py runserver
```
## Примеры запросов к API
### Получение публикации
```text
http://127.0.0.1:8000/api/v1/posts/{id}/
```
```text
Ответ:

{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
