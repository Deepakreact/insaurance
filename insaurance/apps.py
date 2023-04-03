from django.apps import AppConfig


class InsauranceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insaurance'

    def ready(self):
        import insaurance.signals
