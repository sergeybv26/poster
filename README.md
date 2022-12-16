# Сайт "Афиша Москвы"
Интерактивная карта Москвы, на которой размещаются известные виды активного отдыха с подробными описаниями, фотографиями и комментариями

## Основные системные требования:
* Ubuntu 20.04 LTS
* Python 3.9
* PostgreSQL 13
* Зависимости из файла requirements.txt

## Запуск проекта
### Клонирование репозитория
Для клонирования репозитория необходимо установить git:
```shell
https://git-scm.com/downloads
```
Чтобы выполнить клонирование проекта из репозитория необходимо выполнить команду:
```shell
$ git clone https://github.com/sergeybv26/poster.git
```
После копирования проекта из репозитория появится директория poster

### Создание и активация виртуального окружения
```shell
$ cd poster/
$ python3 -m venv env
$ source env/bin/activate
```
Пример строки-приглашения после выполнения команды:
```shell
(env) user@user-pc:~/poster
```

### Установка зависимостей
```shell
$ pip3 install -r requirements.txt
```
Установка зависимостей должна завершиться сообщением: "Successfully installed ..."
### Создание файла с переменными окружения
Переменные окружения для настройки проекта:
* ```SECRET_KEY``` - Секретный ключ Django https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key
* ```DEBUG``` - Флаг отладки (True или False) https://docs.djangoproject.com/en/4.1/ref/settings/#debug
* ```ALLOWED_HOSTS``` - Имена хостов/доменов через запятую, которые может обслуживать данный Django-сайт https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
* ```ENV_TYPE``` - для локального запуска устанавливается значение ```local```, для продакшен - ```prod```

Создать файл .env и записать в него параметры из файла .env.sample
```shell
$ cd poster/
$ touch .env
$ nano .env
```
### Применение миграций
```shell
$ python3 manage.py migrate
```
### Создание суперпользователя
Для работы в административной панели необходимо создать учетную запись суперпользователя:
```shell
$ python3 manage.py createsuperuser
```
После запуска команды необходимо ввести имя пользователя, адрес электронной почты и пароль с подтверждением
### Запуск сайта
```shell
$ python3 manage.py runserver
```

## Пользование сайтом
После локального запуска сервера можно им пользоваться, перейдя по ссылке http://localhost:8000/
На сайте доступны две страницы: главная и панель администратора.
Главная страница расположена по адресу: http://localhost:8000/

Панель администратора расположена по адресу: http://localhost:8000/admin/

На главной странице отображается карта Москвы с точками интереса. При клике по точке выводится подробное описание с фотографиями.

В панели администратора имеется возможность добавлять новые точки интереса и редактировать существующие.

## Демо-версия сайта
Демо-версия сайта размещена по адресу: https://sergeysukha.pythonanywhere.com/

Административная панель демо-версии размещена по адресу: https://sergeysukha.pythonanywhere.com/admin/

## Автоматическая загрузка данных в базу
### Порядок загрузки данных
Для загрузки данных о местах в базу необходимо в терминале выполнить команду заполнения данных load_place.
Данная команда принимает в качестве параметра ссылку на файл JSON.
Пример использования команды:
```shell
$ python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json
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