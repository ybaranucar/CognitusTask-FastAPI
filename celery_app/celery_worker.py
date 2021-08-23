from celery import Celery
from celery.utils.log import get_task_logger
import os

BROKER_URL = os.environ.get('BROKER_URL')
celery = Celery('worker', 
                broker=BROKER_URL, 
                CELERY_IMPORTS = ("celery_app.celery_tasks",))

celery_log = get_task_logger(__name__)