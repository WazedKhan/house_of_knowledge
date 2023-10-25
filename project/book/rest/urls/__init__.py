from django.urls import path, include


urlpatterns = [
    path("", include("book.rest.urls.book")),
]
