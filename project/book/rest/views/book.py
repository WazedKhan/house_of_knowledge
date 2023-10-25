from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


from auditlog.mixins import LogAccessMixin

from book.models import Book
from book.rest.serializers.book import BookSerializer


class PublicBooks(LogAccessMixin, ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter()


class PrivateBookUpdateLog(APIView):
    def get(self, request, format=None, *args, **kwargs):
        book_uuid = kwargs.get("uid", None)
        book_histories = Book.objects.get(uid=book_uuid)
        historical_records = book_histories.history.all()
        book_update_log = []
        for history in historical_records:
            log = {
                "update_by": history.updated_by,
                "previous_data": (
                    history.prev_record.title if history.prev_record else ""
                ),
                "current_data": history.title,
            }
            book_update_log.append(log)
        return Response(book_update_log)
