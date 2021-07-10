from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
     # for profile creation automatically after user creation
    def ready(self):
        import users.signals
