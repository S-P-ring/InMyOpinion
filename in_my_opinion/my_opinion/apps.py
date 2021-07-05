from django.apps import AppConfig


class MyOpinionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_opinion'
    verbose_name = 'Мені здається'
