from rest_framework import generics
from todo_app.serializers import ToDoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


from todo_app.permissions import *
from todo_app.models import Task
from todo_app.paginations import ToDoAPIListPagination



class ToDoAPICreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = ToDoSerializer
    
class ToDoAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = ToDoSerializer
    
class ToDoAPIDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = ToDoSerializer
    
class ToDoAPIView(APIView, ToDoAPIListPagination):
    def get(self,request):
        currentList = Task.objects.filter(user = request.user.id)
        results = self.paginate_queryset(currentList, request, view=self)
        serializer = ToDoSerializer(results,many=True)
        return self.get_paginated_response(serializer.data)
    
        