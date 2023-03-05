from rest_framework import serializers
from todo_app.models import Task
from django.contrib.auth.models import User



class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Task
        fields = "__all__"
        
