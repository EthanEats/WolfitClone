from celery import Celery
import requests

from flask import current_app

celery = Celery(
    'tasks',
    broker='redis://localhost',
    backend='redis://localhost'
)

@celery.task
def post_activity(activity, logger_url):
    post_url = logger_url + "/api/activities"
    r = requests.post(post_url, json=activity)
    r.raise_for_status()