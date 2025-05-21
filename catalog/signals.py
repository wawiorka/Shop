from django.db.models.signals import post_save
from django.dispatch import receiver

from order import models
from order.models import Order


@receiver(post_save, sender=Order)
def process_order(sender, instance, created, **kwargs):
    if created:
        id_product = instance.id_product
        if id_product.stock < instance.quantity:
            raise ValueError("Выбранного товара на складе недостаточно!")
        id_product.stock -= instance.quantity
        instance.status= 'bought'
        instance.save()
        id_product.save()