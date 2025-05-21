from django.contrib import admin

from .models import Order

# Register your models here.
@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created_at", "id_product_id", "user_id")
