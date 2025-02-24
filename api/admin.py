from django.contrib import admin
from .models import Order, OrderItem


class OrderAdminInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderAdminInline
    ]