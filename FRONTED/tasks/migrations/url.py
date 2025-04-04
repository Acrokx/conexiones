# urls.py
from django.urls import path
from tasks.views import TaskListCreateView 

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
