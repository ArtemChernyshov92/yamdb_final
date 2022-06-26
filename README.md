![example event parameter](https://github.com/ArtemChernyshov92/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)
# yamdb_final

Проект api_yamdb позволяет пользователям оставлять отзывы на произведения (не более одного на произведение) и выставлять оценки.
К отзывам можно оставлять комментарии.
Проект не хранит произведения, скачать или посмотреть/послушать произведения нельзя.

# Технологии

В проекте используются следующие технологии:
-Python
-Django Rest Framework
-Postgres
-Docker

# Установка и запуск проекта
 На локальном компьютере:
 1. Склонируйте репозитрий на свой компьютер. Для этого выполните команду:
  git clone https://github.com/ArtemChernyshov92/infra_sp2.git
 2. Создайте .env файл, в котором должны содержаться следующие переменные:
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME= # имя базы данных
  POSTGRES_USER= # логин для подключения к базе данных
  POSTGRES_PASSWORD= # пароль для подключения к БД
  DB_HOST=db
  DB_PORT=5432

 3. Перейдите в директорию infra/, соберите образ при помощи команды:
  docker-compose up -d --build
 4. Примените миграции:
  docker-compose exec web python manage.py migrate
 5. Соберите статику:
  docker-compose exec web python manage.py collectstatic --no-input
 6. Создайте суперпользователя для доступа к админке:
  docker-compose exec web python manage.py createsuperuser

На удаленном сервере:
 1. Cкопируйте на сервер файлы docker-compose.yaml и папку nginx командами:
 - scp docker-compose.yaml  <user>@<server-ip>:
 - scp -r nginx/ <user>@<server-ip>:

 2. Создайте переменные окружения в разделе secrets вкладки settings в текущем репозитории:
  DOCKER_PASSWORD # Пароль от Docker Hub
  DOCKER_USERNAME # Логин от Docker Hub
  HOST # Публичный ip адрес сервера
  USER # Пользователь зарегистрированный на сервере
  PASSPHRASE # Если ssh-ключ защищен фразой-паролем
  SSH_KEY # Приватный ssh-ключ
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME= # имя базы данных
  POSTGRES_USER= # логин для подключения к базе данных
  POSTGRES_PASSWORD= # пароль для подключения к БД
  DB_HOST=db
  DB_PORT=5432
  TELEGRAM_TO # ID телеграм-аккаунта
  TELEGRAM_TOKEN # Токен бота


После каждой команды "git push" будет происходить:
 - Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
 - Сборка и доставка докер-образов на Docker Hub.
 - Автоматический деплой.
 - Отправка уведомления в Telegram.

# Автор(ы)
 Автор проекта - студент Яндекс.Практикум Артём Чернышов 