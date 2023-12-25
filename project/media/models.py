import uuid

from django.db import models

from core.choices import UserStatus

from common.models import BaseModelWithUUIDStatus

from versatileimagefield.fields import PPOIField, VersatileImageField

from media.paths import get_image_path


class ImageStorage(BaseModelWithUUIDStatus):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True,
    )
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.DRAFT,
    )
    name = models.CharField(
        "Media Image",
        max_length=110,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image = VersatileImageField(
        upload_to=get_image_path,
        width_field="width",
        height_field="height",
    )
    height = models.PositiveIntegerField(
        "Image Height",
        blank=True,
        null=True,
    )
    width = models.PositiveIntegerField(
        "Image Width",
        blank=True,
        null=True,
    )

    # FKs
    user = models.ForeignKey(
        "core.User",
        on_delete=models.Case,
        blank=True,
        null=True,
    )
