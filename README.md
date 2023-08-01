# code_versus

**Code Versus** - *соревновательная платформа для решения алгоритмических задач*

Стек проекта: 

    Python
    Django/DRF
    Postgres
    Mongodb
    Celery
    Redis
    RPC
    Docker
    ChatGPT
    Pytest
    Poetry
    Dotenv
    JWT

# Архитектура 

![Arch]( https://sun9-21.userapi.com/impg/WDVZ5y5upL70utvIG-LETdeO1rOVyUK6EYoUVg/PMivWRY-hLk.jpg?size=2560x1386&quality=96&sign=2652d33914068c12426f5eeceb3bbb42&type=album )

У нас есть микросервис тестовой системы которая прогоняет и хранит тесты в Mongodb

Также у нас есть основной сервис где у нас есть API на DRF, реляционная бд PostgreSQL и Celery worker с Redis

Также проект покрыт юнит и интеграционными тестами с помощью pytest

# Функционал
 - зарегистрироваться и войти с помощью JWT, подтвердить почту через сообщение а также восстановить пароль
 - получить задачки и использовать фильтры по названию и сложности
 - прогнать тесты на задачку
 - добавить тесты на задачу(для админа)
 - добавить задачу(для админа)
 - сгенерировать вопрос и ответ от нейросети
 - просмотреть профиль

# Как запустить

Надо собрать компоуз с помощью команды `docker-compose up -d --build`, потом сконфигурировать `.env` файл и выполнить команды `python manage.py makemigrations`, `python manage.py migrate` а потом `python manage.py runserver`


    
    

