from tabnanny import verbose
from django.apps import AppConfig


class TaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task'
    verbose_name = 'task.karsu.uz - Task Manager'
