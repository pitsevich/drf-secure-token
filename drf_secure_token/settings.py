from django.conf import settings as django_settings


DEFAULT_SETTINGS = {
    'TOKEN_AGE': 0,
    'UPDATE_TOKEN': not django_settings.DEBUG,

    'MUTABLE_PERIOD': 60 * 5,  # Five minutes

    'REMOVE_TOKENS_THROUGH_CELERY': False,

    'TOKEN_CHECKERS': [
        'drf_secure_token.checkers.ActiveUserChecker',
        'drf_secure_token.checkers.DeadTokenChecker',
    ],
}


class Settings(object):
    def __init__(self, settings, default_settings):
        self.settings = settings
        self.default_settings = default_settings

    def __getattr__(self, item):
        if item not in self.default_settings:
            raise AttributeError("Invalid settings: '%s'" % item)

        return getattr(self.settings, item, self.default_settings[item])


settings = Settings(django_settings, DEFAULT_SETTINGS)
