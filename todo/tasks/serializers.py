from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    author = serializers.CharField(source='author.username', max_length=200)