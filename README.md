Helping documents:
------------------
https://blog.logrocket.com/optimizing-task-queues-celery-flask/
https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html



Run the app:
-------------
terminal1:
pipenv shell
pipenv install -r requirements.txt
export FLASK_APP=app; python -m flask run

terminal2:
celery -A app.celery worker --loglevel=info


First steps of celery:
-----------------------
Choosing and installing a message transport (broker).
Installing Celery and creating your first task.
Starting the worker and calling tasks.
Keeping track of tasks as they transition through different states, and inspecting return values.