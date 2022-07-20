# Интерактивная карта Москвы

Карта Москвы с интересными местами.


## Пример
[Пример сайта](http://neverdieone.pythonanywhere.com/map)

[Админка на сайте](http://neverdieone.pythonanywhere.com/admin)

Данные для входа в админке:
* Login: `admin`
* Password: `adminadmin`

## Хочешь такой же?

Скачать репозиторий
* `git clone https://github.com/NeverDieOne/django-afisha.git`

В корне проекта создать файл `.env`

Положить внутрь переменную `SECRET_KEY`

Установить зависимости
* `pip install -r requirements.txt`

Сделать миграции
* `python manage.py migrate`

Создать суперпользователя
* `python manage.py createsuperuser`

Запустить сайт и наслаждаться
* `python manage.py runserver` (команда не подходит для запуска на боевом сервере, см. ниже)
    
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).


## Запуск на боевом сервере

Гайд по деплою проекта Django на боевом сервере от [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04).
