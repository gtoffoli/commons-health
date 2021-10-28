
from django.apps import AppConfig
import commons

class HealthConfig(AppConfig):
    name = 'health'

    def ready(self):
        import commons.signal_handlers
