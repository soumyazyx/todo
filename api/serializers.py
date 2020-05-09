from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import List, Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
