# Проект DjangoStripe API
## Локальный запуск
Скопировать репозиторий к себе:
```
git clone git@github.com:N89701/StripeAPI.git
```

В папке infra переименовать .env.example на .env и вставить свои значения для STRIPE_PUBLISHABLE_KEY и STRIPE_SECRET_KEY
Перейти в консоли в папку infra и выполнить следующие команды:
```bash
docker compose up -d --build
docker exec infra-web-1 python manage.py makemigrations
docker exec infra-web-1 python manage.py migrate
docker exec infra-web-1 python manage.py loaditems
```

Все готово! Теперь можно открыть в браузере страницу http://localhost:8081/item/1/, нажать Buy
и вас перенаправит на страницу оплаты товара.

## Контакт для обратной связи
Tg: N89701