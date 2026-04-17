from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "heading",
        "content",
        "photo_blog",
        "created_at",
        "ispublication",
    )
    list_filter = ("heading",)
    search_fields = (
        "heading",
        "content",
    )
