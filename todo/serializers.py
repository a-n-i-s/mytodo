from rest_framework.serializers import ModelSerializer
from .models import Task
class TaskSerializer(ModelSerializer):
  class Meta:
    model=Task
    fields=['owner','title','detail','done']
    read_only_fields=['owner']

  
  