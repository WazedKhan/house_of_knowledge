import uuid

# package imports
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

# projects imports
from common.models import BaseModelWithUUIDStatus
from .utils import get_branch_slug, get_stock_slug


User = get_user_model()


class Branch(BaseModelWithUUIDStatus):
    # uid = models.UUIDField(
    #     db_column=True, unique=True, default=uuid.uuid4, editable=False
    # )
    slug = AutoSlugField(populate_from=get_branch_slug, unique=True, db_index=True)
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(
        "core.User",
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name="branch_managers",
    )
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = PhoneNumberField(db_index=True, unique=True, blank=False, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_default_manager(self):
        # set the first created/specific user as default manager
        manager = User.objects.last()
        # last is the first created user
        if manager:
            return manager.id
        return None


class Stock(BaseModelWithUUIDStatus):
    # uid = models.UUIDField(
    #     db_column=True, unique=True, default=uuid.uuid4, editable=False
    # )
    slug = AutoSlugField(populate_from=get_stock_slug, unique=True, db_index=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content_type} at {self.branch.name}"
