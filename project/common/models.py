import uuid
from django.db import models


from dirtyfields import DirtyFieldsMixin

from .choices import InstanceStatus


class CreateUpdatedByBaseModel(models.Model):
    entry_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=("entry by"),
        related_name="%(app_label)s_%(class)s_entry_by",
    )
    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=("last updated by"),
        related_name="%(app_label)s_%(class)s_updated_by",
    )

    class Meta:
        abstract = True


class BaseModelWithUID(DirtyFieldsMixin, CreateUpdatedByBaseModel, models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=InstanceStatus.choices,
        db_index=True,
        default=InstanceStatus.ACTIVE,
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def get_auto_fields(self):
        return [
            "updated_at",
        ]
