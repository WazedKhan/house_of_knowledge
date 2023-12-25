from django.contrib import admin

from .models import Branch, Stock


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "slug",
        "name",
        "manager",
    ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "slug",
        "content_type",
        "object_id",
        "content_object",
        "branch",
        "quantity",
        "purchase_price",
    ]
