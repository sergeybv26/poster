# Сайт "Афиша Москвы"
Интерактивная карта Москвы, на которой размещаются известные виды активного отдыха с подробными описаниями, фотографиями и комментариями

## Основные системные требования:
* Ubuntu 20.04 LTS
* Python 3.9
* PostgreSQL 13
* Зависимости из файла requirements.txt

## Переменные окружения
### Настройки Django
* ```SECRET_KEY``` - Секретный ключ Django
* ```DEBUG``` - Флаг отладки (True или False)
### Тип виртуального окружения
```ENV_TYPE``` - для локального запуска устанавливается значение ```local```, для продакшен - ```prod```
### Параметры PostgreSQL
* ```SQL_DATABASE``` - имя базы данных
* ```USER``` - имя пользователя
* ```PASSWORD``` - пароль пользователя
* ```HOST``` - хост, на котором работает база данных
* ```PORT``` - порт, на котором работает база данных
* ```DATABASE``` - тип базы данных (необходим для работы в Docker). Необходимо установить значение ```postgres```
### Параметры администратора сайта
* ```ADMIN_USERNAME``` - имя пользователя
* ```ADMIN_EMAIL``` - email пользователя
* ```ADMIN_PASSWORD``` - пароль пользователя

## Запуск проекта
### Создание и активация виртуального окружения
```shell
$ python3 -m venv env
$ source env/bin/activate
```
### Установка зависимостей
```shell
$ pip3 install -r requirements.txt
```
### Создание файла с переменными окружения
* Создать файл .env и записать в него параметры из файла .env.sample
* Создать файл .env.db и записать в него параметры из файла .env.db.sample. Имя пользователя, пароль и наименование базы должны совпадать с записанными в файле .env.
### Применение миграций
```shell
$ cd poster/
$ python3 manage.py migrate
```
### Запуск сайта
```shell
$ python3 manage.py runserver
```

## Запуск проекта в Docker
### Установка Docker
#### Обновление информации о репозиториях
```shell
 $ sudo apt-get update
 $ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-releas
```
#### Добавление официального GPG ключа Docker
```shell
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
#### Добавление репозитория Docker
```shell
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
#### Установка Docker
```shell
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
### Создание файла с переменными окружения
* Создать файл .env и записать в него параметры из файла .env.sample
* Создать файл .env.db и записать в него параметры из файла .env.db.sample. Имя пользователя, пароль и наименование базы должны совпадать с записанными в файле .env.
### Запускаем проект в Docker
```shell
$ cd poster/
$ chmod +x poster/entrypoint.sh
$ sudo docker-compose up --build
```

## Пользование сайтом
На сайте доступны две страницы: главная и панель администратора.
Главная страница расположена по адресу: http://your_host:8000/

Панель администратора расположена по адресу: http://your_host:8000/admin/

На главной странице отображается карта Москвы с точками интереса. При клике по точке выводится подробное описание с фотографиями.

В панели администратора имеется возможность добавлять новые точки интереса и редактировать существующие.

## Демо-версия сайта
Демо-версия сайта размещена по адресу: http://185.20.224.111/

Административная панель демо-версии размещена по адресу: http://185.20.224.111/admin/

## Автоматическая загрузка данных в базу
### Порядок загрузки данных
Для автоматической загрузки данных в базу необходимо выполнить следующее:
* записать список ссылок на JSON файлы в переменную ```JSON_LINKS```, расположеннуюв модуле ```common.variables```
* в терминале выполнить команду
```shell
$ python3 manage.py fill_db
```
### Требуемый формат файла JSON
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

https://sergeysukha.pythonanywhere.com
Создать media/places