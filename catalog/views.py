from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.exclude(stock=0).order_by('created')
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
