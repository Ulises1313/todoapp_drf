from .models import Task
from rest_framework import viewsets, permissions,status
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def completed_tasks(self,request):
        completed_tasks = Task.objects.filter(is_done = True)
        serializer = self.get_serializer(completed_tasks, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)