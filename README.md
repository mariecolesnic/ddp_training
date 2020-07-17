# ddp_training
Docker Django Postgres training

Обработка запроса от клиента до Django и обратно (dev-версия)
client <==> django runserver

Обработка запроса от клиента до Django и обратно (prod-версия)
client <==> nginx [proxy_pass] <==> uwsgi [gunicorn] <==> django