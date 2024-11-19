from django.apps import AppConfig


#make sure to update the application in settings.py
class BaseConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
