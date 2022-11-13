from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Task's admin panel
    """
    list_display = (
        'pk',
        'author',
        'text',
        'created',
        'is_did',
    )
    list_editable = (
        'text',
        'is_did',
    )
    search_fields = (
        'author',
        'text',
    )


admin.site.register(Task, TaskAdmin)
