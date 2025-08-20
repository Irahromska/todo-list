from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", "is_done", "tags_list")
    list_filter = ("is_done", "tags")
    search_fields = ("content",)
    date_hierarchy = "created_at"

    def tags_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    tags_list.short_description = "Tags"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
