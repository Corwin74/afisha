# Интерактивная карта Москвы

Карта Москвы с интересными местами.


## Пример
[Пример сайта](https://is.shockland.ru)

[Админка на сайте](https://is.shockland.ru/admin)


## Инструкции по установке
### Скачать репозиторий
### Установить зависимости
  ```
  pip install -r requirements.txt
  ```
### Настроить переменные окружения
В корне проекта создать файл `.env`  
В файле создать следующие переменные окружения:
```
SECRET_KEY=h33%#6*uci8e5(3(9xw(x4^*d=j57t1g(=zccawvjk(+rxmt#d  
```
Переменная SECRET_KEY является обязательной  

Сгенерировать свой ключ можно [здесь](https://djecrety.ir/)  

```
DEBUG=True  
```
Переменная DEBUG отвечает за режим в котором будет запущен веб-сервер.  
Eсли значение 'True' или 'yes', то веб-сервер будет запущен в отладочном режиме.иЕсли значение 'False' или 'no', то в production mode. Если переменная DEBUG не будет указана, по умолчанию ей будет присвоено значение 'True'  
```
ALLOWED_HOSTS=127.0.0.1,local_host,[::1]
```
Переменная ALLOWED_HOSTS содержит имена хостов и доменных имен, которые будут обслуживаться запущенным веб-сервером. Если переменная не будет указана, по   умолчанию будут подставлены вышеуказнные значения в примере. В `.env` файле следуют указывать имена и адреса без кавычек и пробелов значения разделяются запятыми.  

### Сделать миграции
```
python manage.py migrate
```
### Создать суперпользователя(администратора):
```
python manage.py createsuperuser
```
### Запустить сайт и наслаждаться по адресу http://127.0.0.1:8000/
```
python manage.py runserver
```
Доступ в админку http://127.0.0.1:8000/admin  
Реквизиты входа,созданный ранее суперпользователь.
## Загрузка данных
Данные с новыми местами можно загрузить командой load_place
```
python manage.py load_place <имя json файла>
```
Примеры таких файлов лежат в каталоге places_json. Ссылку на файл можно получить через интерфейс GitHub: выберите файл, откройте его на отдельной странице и нажмите кнопку Raw. Так вы получите ссылку на исходный код файла. Пример загрузки:
```
python manage.py load_place https://raw.githubusercontent.com/Corwin74/afisha/main/places_json/roofs24.json
```
### Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

### Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
