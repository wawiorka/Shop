from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created')
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]
