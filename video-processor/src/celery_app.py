import os
import json
from celery import Celery, group
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

app = Celery('video_processor')

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
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
)

# Beat schedule for periodic tasks
app.conf.beat_schedule = {
    'cleanup-temp-files': {
        'task': 'src.tasks.cleanup.cleanup_temp_files',
        'schedule': crontab(hour=2, minute=0),  # Run at 2 AM daily
    },
}

if __name__ == '__main__':
    app.start()
