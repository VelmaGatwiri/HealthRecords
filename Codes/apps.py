from django.apps import AppConfig


class CodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Codes'

    def ready(self):
        import Codes.signals
