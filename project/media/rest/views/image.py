from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from media.rest.serializers.image import ImageStorageSerializer


from media.models import ImageStorage


class ImageStorageList(ListCreateAPIView):
    queryset = ImageStorage.objects.all()
    serializer_class = ImageStorageSerializer
    permission_classes = [AllowAny]
