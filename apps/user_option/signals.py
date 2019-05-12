from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from user_option.models import UserGoodsFav
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


@receiver(post_save, sender=UserGoodsFav)
def create_usergoodsfav(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserGoodsFav)
def delete_usergoodsfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()


@receiver(post_save, sender=UserGoodsFav)
def create_usergoodsfav(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserGoodsFav)
def delete_usergoodsfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()
