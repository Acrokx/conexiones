# views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Vista para listar y crear tareas
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()  # Obtenemos todas las tareas de la base de datos
    serializer_class = TaskSerializer  # Usamos el serializador para convertir las tareas a JSON
