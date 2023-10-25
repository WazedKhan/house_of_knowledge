from rest_framework.serializers import ModelSerializer

from book.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "uid",
            "slug",
            "title",
            "authors",
            "publication_date",
        ]
