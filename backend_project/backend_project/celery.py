import os
from celery import Celery

# ✅ Correct: Sets the default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')

# ✅ Correct: Create a Celery app instance with the project name
app = Celery('backend_project')

# ✅ Correct: Load configuration from Django settings (with CELERY_ prefix)
app.config_from_object('django.conf:settings', namespace='CELERY')

# ✅ Correct: Autodiscover tasks from all registered Django apps
app.autodiscover_tasks()

# ✅ Optional but Good: Test task to ensure everything works
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
