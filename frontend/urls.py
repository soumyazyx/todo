from django.urls import path
from . import views


urlpatterns = [
    path("", views.lists, name="lists"),
    path("tasks/", views.tasks, name="tasks"),
    path("share/", views.sharelist, name="sharelist"),
    path("list/<str:listid>", views.tasksIntermediate, name="tasksIntermediate"),
]
