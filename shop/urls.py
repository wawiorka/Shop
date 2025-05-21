from django.contrib import admin
from django.urls import path, include
from .views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ping, name='ping'),
    path('auth/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('api/order/', include('order.urls'))
]

