PROJECT = nodeads_test_assignment

dev-run:
	./manage.py runserver 0.0.0.0:8081 --settings=quickpoller.settings

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +

server:
	gunicorn -k aiohttp.worker.GunicornWebWorker -w 9 -t 60 todo.app:app

restart-psql:
	brew services restart postgresql

check:
	./manage.py check