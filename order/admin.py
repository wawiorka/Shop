from django.contrib import admin

from .models import Order

# Register your models here.
@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id_product_id", "user_id", "created_at", "status")
    ordering = ("id_product_id", "user_id", "created_at", "status")
    list_filter = ("status",)
