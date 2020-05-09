from django.urls import path
from . import views


urlpatterns = [
    path('', views.lists, name="lists"),
    path('tasks/', views.tasks, name="tasks"),
    path('list/<str:listid>', views.tasksIntermediate, name="tasksIntermediate")
]
