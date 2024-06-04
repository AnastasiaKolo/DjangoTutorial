""" Apps config """
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """ Config for Polls app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
