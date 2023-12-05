# Проект API для социальной сети
## Описание
Проект представляет собой API на Django Rest Framework. В проекте можно создавать публикации, комментарии к ним, а также к другим созданным постам, оформить подписку на автора и, соответственно, отписаться от него.
В проекте нет фронтенда.
Аутентифицированные пользователи могут  изменять и удалять свой контент, в остальных случаях доступ предоставляется только для чтения.
После запуска проекта по адресу <http://127.0.0.1:8000/redoc/> будет доступна документация для API Yatube.
## Установка
Клонировать репозиторий и перейти в него в командной строке:
```text
git clone https://github.com/PavelHomov/api_final_yatube.git
```
```text
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```text
python -m venv venv
```
```text
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```text
python -m pip install --upgrade pip
```
```text
pip install -r requirements.txt
```
Выполнить миграции:
```text
cd yatube_api
```
```text
python manage.py migrate
```
Запустить проект:
```text
python manage.py runserver
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
