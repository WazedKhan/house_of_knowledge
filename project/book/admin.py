import logging

from django.contrib import admin

from .models import Author, Book, Chapter, Page, Bookmark, Comment


logger = logging.getLogger("__name__")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "status",
        "first_name",
        "last_name",
        "user",
    ]

    search_fields = [
        "first_name",
        "id",
        "user__first_name",
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "slug",
        "title",
        "get_authors",
        "publication_date",
    ]

    @admin.display(description="authors")
    def get_authors(self, object):
        logger.warning("Running all query for retrieving authors!")
        return [
            f"{author.first_name} {author.last_name}"
            for author in object.authors.filter()
        ]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "book",
        "title",
        "chapter_number",
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "chapter",
        "page_number",
    ]


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uid",
        "user",
        "book",
        "page",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
