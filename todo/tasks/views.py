from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class GetTaskInfoView(APIView):
    def get(self, request):
        queryset = Task.objects.all()
        serializer_for_queryset = TaskSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_queryset.data)

