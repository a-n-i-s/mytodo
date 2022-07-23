
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,related_name='tasks')
    title=models.CharField(max_length=200)
    detail=models.TextField()
    done=models.BooleanField(default=False)
    
    

    class Meta:
        verbose_name ="Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
    