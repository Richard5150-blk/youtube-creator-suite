from src.celery_app import app

if __name__ == '__main__':
    app.worker_level = 'DEBUG'
    app.start()
