from django.db import models
from users.models import User
from catalog.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=15, default='not bought')


    class Meta:
        # unique_together = ('user', 'id_product')
        ordering = ('id_product',)  # уникальность мешала при проверке
