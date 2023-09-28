from django.urls import path

from book.rest.views.book import PublicBooks

urlpatterns = [
    path("", PublicBooks.as_view(), name="book-list"),
]
