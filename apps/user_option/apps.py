from django.apps import AppConfig


class UserOptionConfig(AppConfig):
    name = 'user_option'
    verbose_name = '用户操作管理'

    def ready(self):
        import user_option.signals
