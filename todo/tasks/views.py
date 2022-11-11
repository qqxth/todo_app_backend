from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions

from .classes import CreateRetrieveUpdateDestroy
from .permissions import IsAuthor
from .models import Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskListView(generics.ListAPIView):
    lookup_field = 'author'

    serializer_class = TaskListSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user.id).all()


class TaskView(CreateRetrieveUpdateDestroy):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all().select_related('author')
    serializer_class = TaskSerializer
    permission_classes_by_action = {
        'get': [IsAuthor],
        'update': [IsAuthor],
        'destroy': [IsAuthor],
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


