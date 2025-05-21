from django.db.models import F
from rest_framework import serializers

from .models import Order
from catalog.serializers import ProductSerializers


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializers(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id_product', 'quantity']

    def validate_name(self, id_product):
        user = self.context['request'].user
        if Order.objects.filter(user=user, id_product=id_product).exists():
            raise serializers.ValidationError("Вы уже забронировали этот товар.")

        return id_product

    def create(self, validated_data):
        user = self.context['request'].user
        return Order.objects.create(user=user, **validated_data)