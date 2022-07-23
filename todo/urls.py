from argparse import Namespace
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from todo.views import taskviewset

router=DefaultRouter()
router.register(r'todo',taskviewset)
urlpatterns = [
    path('',include(router.urls))
]
