from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery('worker', 
                broker='amqp://guest:guest@127.0.0.1:5672//', 
                CELERY_IMPORTS = ("celery_app.celery_tasks",))

celery_log = get_task_logger(__name__)