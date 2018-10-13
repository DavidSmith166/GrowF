from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'api'

    def ready(self):
        from . import tasks
