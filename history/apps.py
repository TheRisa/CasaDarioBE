from django.apps import AppConfig


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'history'

class RecordConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'record'