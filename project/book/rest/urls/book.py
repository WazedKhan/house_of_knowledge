from django.urls import path

from book.rest.views.book import PublicBooks, PrivateBookUpdateLog

urlpatterns = [
    path("", PublicBooks.as_view(), name="book-list"),
    path("/<uuid:uid>/logs", PrivateBookUpdateLog.as_view(), name="book-update-log"),
]
