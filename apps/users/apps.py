from django.apps import AppConfig


class CateringConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'

    def ready(self):
        import users.signals