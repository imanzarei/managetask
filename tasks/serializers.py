from rest_framework import serializers
from apis.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'status', 'title', 'description', 'created_by')

