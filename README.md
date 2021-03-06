# Калькулятор стоимости

Простой калькулятор стоимости с учётом скидки и налога в разных штатах.


## Создание базы данных

Для простого калькулятора нет необходимости в большой базе данных,
две маленьких таблички без необходимости постоянного редактирования
можно хранить и в sqlite.


Заполнить начальные данные можно с помощью команды

```shell
docker-compose -f docker-compose.yml -f docker-compose.manage.yml up fill_db
```


## Миграции

После изменения моделей необходимо пересобрать основной образ сервиса

```shell
docker-compose -f docker-compose.yml build billing_service
```

Затем создать миграции командой

```shell
docker-compose -f docker-compose.yml -f docker-compose.manage.yml up makemigrations
```

И применить их командой

```shell
docker-compose -f docker-compose.yml -f docker-compose.manage.yml up migrate
```


## Запуск тестов

```shell
docker-compose -f docker-compose.yml -f docker-compose.manage.yml up --build test
```

## Запуск сервиса

Для запуска сервиса можно использовать docker-compose (флаг --build для пересборки)

```shell
docker-compose up
```


## Админка

Для удобного создания или изменения значений (discount, tax) в базе нужно создать
администратора с помощью команды

```shell
python manage.py createsuperuser
```

И зайти в админку по адресу /admin
