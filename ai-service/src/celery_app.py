import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery('ai_service')

# Celery configuration
app.conf.update(
    broker_url=os.getenv('REDIS_URL', 'redis://localhost:6379'),
    result_backend=os.getenv('REDIS_URL', 'redis://localhost:6379'),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=15 * 60,  # 15 minutes
    task_soft_time_limit=10 * 60,  # 10 minutes
)

if __name__ == '__main__':
    app.start()
