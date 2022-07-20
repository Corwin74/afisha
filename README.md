# Интерактивная карта Москвы

Карта Москвы с интересными местами.


## Пример
[Пример сайта](https://is.shockland.ru)

[Админка на сайте](https://is.shockland.ru/admin)

Данные для входа в админке:
* Login: `admin`
* Password: `test123`

## Инструкции по установке

Скачать репозиторий

Установить зависимости

* `pip install -r requirements.txt`

В корне проекта создать файл `.env`

Положить внутрь переменную `SECRET_KEY`, например

SECRET_KEY=h33%#6*uci8e5(3(9xw(x4^*d=j57t1g(=zccawvjk(+rxmt#d

Сгенерировать свой ключ можно [здесь](https://djecrety.ir/)

Сделать миграции
* `python manage.py migrate`

Создать суперпользователя(администратора)
* `python manage.py createsuperuser`

Запустить сайт и наслаждаться по адресу http://127.0.0.1/
* `python manage.py runserver` 
    
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
