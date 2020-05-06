from django.urls import path
from . import views


urlpatterns = [
    path('', views.lists, name="lists"),
    path('list/<str:listid>', views.tasks, name="tasks")
]
