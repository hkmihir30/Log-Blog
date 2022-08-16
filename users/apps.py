from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # this is done as django prefers it to do this way 
    # i mean to add signals in the apps
    def ready(self):
        import users.signals 
