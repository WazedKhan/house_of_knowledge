from rest_framework.generics import ListCreateAPIView

from book.models import Book
from book.rest.serializers.book import BookSerializer


class PublicBooks(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter()
