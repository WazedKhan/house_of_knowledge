import uuid
from django.db import models

from autoslug import AutoSlugField
from auditlog.registry import auditlog
from simple_history.models import HistoricalRecords

from common.models import BaseModelWithUID

from .choices import BookStatus
from .utils import get_book_slug


class Author(BaseModelWithUID):
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        "core.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def set_author_name_if_user(self):
        if self.user:
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.save()


class Book(BaseModelWithUID):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_book_slug, unique=True, db_index=True)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title


class Chapter(BaseModelWithUID):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    chapter_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - Chapter {self.chapter_number}: {self.title}"


class Page(BaseModelWithUID):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField()
    page_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.chapter.book.title} - Chapter {self.chapter.chapter_number}, Page {self.page_number}"


class Bookmark(BaseModelWithUID):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Bookmark on {self.page}"


class Comment(BaseModelWithUID):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.page}"


# audit log model history
auditlog.register(Book)
