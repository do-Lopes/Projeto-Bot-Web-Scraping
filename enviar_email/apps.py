from django.apps import AppConfig

class EnviaemailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enviar_email'

    def ready(self):
        from Repetidor import updater
        updater.start()
