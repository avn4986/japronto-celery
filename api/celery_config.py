from celery import Celery

app = Celery(
    'celery_config',
    backend='redis://redis:6379/0',
    broker='redis://redis:6379/0',
    include=['celery_add'],
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json'
)

app.conf.CELERY_RESULT_BACKEND = 'redis'
app.conf.CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
