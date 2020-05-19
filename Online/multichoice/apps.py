from django.apps import AppConfig


class MultichoiceConfig(AppConfig):
    name = 'multichoice'

    def ready(self):
        import multichoice.mysignal

    
