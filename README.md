# Сайт "Афиша Москвы"
Интерактивная карта Москвы, на которой размещаются известные виды активного отдыха с подробными описаниями, фотографиями и комментариями

## Основные системные требования:
* Ubuntu 20.04 LTS
* Python 3.9
* PostgreSQL 13
* Зависимости из файла requirements.txt

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
Создать файл .env и записать в него параметры из файла .env.sample
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
### Запускаем проект в Docker
```shell
$ cd poster/
$ chmod +x poster/entrypoint.sh
$ sudo docker-compose up --build
```

## Пользование сайтом
На сайте доступны две страницы: главная и панель администратора.
Главная страница расположена по адресу: http://<host>:8000/

Панель администратора расположена по адресу: http://<host>:8000/admin/

На главной странице отображается карта Москвы с точками интереса. При клике по точке выводится подробное описание с фотографиями.

В панели администратора имеется возможность добавлять новые точки интереса и редактировать существующие.

## Демо-версия сайта
Демо-версия сайта размещена по адресу: http://185.20.224.111/
