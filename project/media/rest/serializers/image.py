from rest_framework import serializers

from media.models import ImageStorage


class ImageStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStorage
        fields = "__all__"
