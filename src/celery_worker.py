from celery import Celery
from celery.schedules import crontab
import requests

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

API_URL = "http://127.0.0.1:8000/fetch_news/"  # Replace with your API endpoint

@celery.task
def call_api():
    try:
        response = requests.post(API_URL)
        print(f"API Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error calling API: {e}")


# Configure periodic tasks
celery.conf.beat_schedule = {
    "run-every-minute": {
        "task": "celery_worker.call_api",
        "schedule": crontab(minute="*"),  # Runs every minute
    },
}

celery.conf.timezone = "Asia/Kolkata"  # Set to IST

if __name__ == "__main__":
    celery.start()
