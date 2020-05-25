from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    # List/s management
    path("lists/<str:username>", views.lists, name="lists"),
    path("list-create/", views.listCreate, name="list-create"),
    path("list-detail/<str:pk>", views.listDetail, name="list-detail"),
    path("list-update/<str:pk>", views.listUpdate, name="list-update"),
    path("list-delete/<str:pk>", views.listDelete, name="list-delete"),
    path("list-share/<str:list_id>/<str:user_id>", views.listShare, name="list-share"),
    # Task/s management
    path("tasks/<str:listid>", views.tasks, name="tasks"),
    path("task-detail/<str:pk>", views.taskDetail, name="task-detail"),
    path("task-create/", views.taskCreate, name="task-create"),
    path("task-update/<str:pk>", views.taskUpdate, name="task-update"),
    path("task-delete/<str:pk>", views.taskDelete, name="task-delete"),
    # User management
    path(
        "get-user-id/username/<str:username>",
        views.getUserIdFromUsername,
        name="get-user-id-from-username",
    ),
    path(
        "get-user-id/email/<str:email>",
        views.getUserIdFromEmail,
        name="get-user-from-email",
    ),
]
