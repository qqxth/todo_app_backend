from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Task(models.Model):
    """Task's model
    """
    text = models.TextField(
        verbose_name='Задача',
        max_length=250,
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        related_name='tasks',
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Задача'
