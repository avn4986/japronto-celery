from celery_config import app


@app.task(name='celery_add.run_et')
def run_et():
    return 900 + 500
