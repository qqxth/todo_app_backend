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
    )
    list_editable = (
        'text',
    )
    search_fields = (
        'author',
        'text',
    )


admin.site.register(Task, TaskAdmin)
