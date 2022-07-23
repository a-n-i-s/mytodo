from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from rest_framework import permissions
from .models import Task
# Create your views here.

class taskviewset(ModelViewSet):
  serializer_class=TaskSerializer
  queryset=Task.objects.all()
  permission_classes=[permissions.IsAuthenticated]
  def get_queryset(self):
      return self.request.user.tasks.all()
  

  def perform_create(self,serializer):
    serializer.save(owner=self.request.user)
