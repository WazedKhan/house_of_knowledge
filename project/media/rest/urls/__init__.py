from django.urls import path, include

from media.rest.views.image import ImageStorageList

urlpatterns = [
    path(
        "images",
        ImageStorageList.as_view(),
        name="image-list",
    )
]
