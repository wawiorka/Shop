from django.urls import path
from .views import MyOrderListView, CreateOrderView

urlpatterns = [
    path('', MyOrderListView.as_view(), name='create-order'),
    path('my/', CreateOrderView.as_view(), name='my-order'),
]