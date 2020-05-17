from django.urls import path
from . import views


urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("get-user-id/<str:username>", views.getUserId, name="get-user-id"),
    path("lists/<str:username>", views.lists, name="lists"),
    path("list-create/", views.listCreate, name="list-create"),
    path("list-detail/<str:pk>", views.listDetail, name="list-detail"),
    path("list-update/<str:pk>", views.listUpdate, name="list-update"),
    path("list-delete/<str:pk>", views.listDelete, name="list-delete"),
    path("tasks/<str:listid>", views.tasks, name="tasks"),
    path("task-detail/<str:pk>", views.taskDetail, name="task-detail"),
    path("task-create/", views.taskCreate, name="task-create"),
    path("task-update/<str:pk>", views.taskUpdate, name="task-update"),
    path("task-delete/<str:pk>", views.taskDelete, name="task-delete"),
    path(
        "get-user/email/<str:email>", views.getUserFromEmail, name="get-user-from-email"
    ),

]
