Helping documents:
------------------
https://blog.logrocket.com/optimizing-task-queues-celery-flask/




Run the app:
-------------
terminal1:
pipenv shell
pipenv install -r requirements.txt
export FLASK_APP=app; python -m flask run

terminal2:
celery -A app.celery worker --loglevel=info