from rest_framework.generics import ListCreateAPIView


from auditlog.mixins import LogAccessMixin

from book.models import Book
from book.rest.serializers.book import BookSerializer


class PublicBooks(LogAccessMixin, ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter()
