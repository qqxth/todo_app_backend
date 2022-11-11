from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions

from .models import Task
from .serializers import TaskListSerializer


class TaskListView(generics.ListAPIView):
    lookup_field = 'author'

    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user.id).all()

