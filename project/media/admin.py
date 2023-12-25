from django.contrib import admin
from media.models import ImageStorage


@admin.register(ImageStorage)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "name",
        "image",
    ]
