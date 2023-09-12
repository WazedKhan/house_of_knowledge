from django.contrib import admin
from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "slug",
        "uid",
        "first_name",
        "last_name",
        "created_by",
        "updated_by",
        "created_at",
        "updated_at",
    ]