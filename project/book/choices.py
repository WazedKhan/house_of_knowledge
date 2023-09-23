from django.db import models


class BookStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    INACTIVE = "INACTIVE", "Inactive"
