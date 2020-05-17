from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Task, List
from .serializers import TaskSerializer, ListSerializer, UserSerialzer

User = get_user_model()


@api_view(["GET"])
@login_required
def apiOverview(request):
    api_urls = {
        "Tasks": "/tasks/",
        "TaskDetail": "/task-detail/<str:pk>/",
        "TaskCreate": "/task-create/",
        "TaskUpdate": "/task-update/<str:pk>/",
        "TaskDelete": "/task-delete/<str:pk>/",
        "Lists": "lists/<str:username>",
        "ListDetail": "/list-detail/<str:pk>/",
        "ListCreate": "/list-create/",
        "ListUpdate": "/list-update/<str:pk>/",
        "ListDelete": "/list-delete/<str:pk>/",
        "GetUserId": "get-user-id/<str:username>",
    }
    return Response(api_urls)


@api_view(["GET"])
@login_required
def tasks(request, listid):
    tasks = Task.objects.filter(_list_id=listid).order_by("completed", "-id")
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@login_required
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@login_required
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@login_required
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("ERROR OCCURED!")
        print(serializer.errors)
    return Response(serializer.data)


@api_view(["DELETE"])
@login_required
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item succesfully deleted!")


@api_view(["GET"])
@login_required
def lists(request, username):
    # query = f"SELECT AL.ID, USER_ID AS USER, AL.TITLE AS LIST_TITLE, COUNT(TSK._LIST_ID) AS TASKS_COUNT FROM PUBLIC.AUTH_USER AU,PUBLIC.API_LIST AL,PUBLIC.API_TASK TSK WHERE AL.USER_ID = AU.ID AND AL.ID = TSK._LIST_ID AND AU.USERNAME = 'soumya_ranjan' GROUP BY AL.ID,TSK._LIST_ID"
    lists = List.objects.filter(users__username=username)

    request.session["lists"] = {}
    for lst in lists:
        request.session["lists"][lst.id] = lst.title

    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@login_required
def listDetail(request, pk):
    _list = List.objects.get(id=pk)
    serializer = ListSerializer(_list, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@login_required
def listCreate(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(["POST"])
@login_required
def listUpdate(request, pk):
    _list = List.objects.get(id=pk)
    serializer = ListSerializer(instance=_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
@login_required
def listDelete(request, pk):
    print(f"pk passed in = {pk}")
    _list = List.objects.get(id=pk)
    _list.delete()
    return Response("List successfully deleted!")


@api_view(["GET"])
@login_required
def listShare(request, list_id, user_id):
    print(f"{list_id}|{user_id}")
    # Check if the record already exists
    if List.users.through.objects.filter(list_id=list_id, user_id=user_id).count() > 0:
        # Record already exist - its not an error
        return Response("List already shared!")
    else:
        # Insert record
        List.users.through.objects.create(list_id=list_id, user_id=user_id)
        return Response("List successfully shared!")


@api_view(["GET"])
@login_required
def getUserIdFromUsername(request, username):
    query = f"SELECT ID,USERNAME,EMAIL FROM PUBLIC.AUTH_USER AU WHERE AU.USERNAME = '{username}'"
    querySet = User.objects.raw(query)
    for rec in querySet:
        username = rec.username
        userid = rec.id
    return JsonResponse({"username": username, "id": userid})


@api_view(["GET"])
def getUserIdFromEmail(request, email):
    user = User.objects.filter(email=email)
    if user.count() == 0:
        return JsonResponse({"user_id": -1, "email_id": email})

    for rec in user:
        user_id = rec.id
        user_name = rec.username
        first_name = rec.first_name
        last_name = rec.last_name
        date_joined = rec.date_joined
    return JsonResponse(
        {
            "email_id": email,
            "user_id": user_id,
            "user_name": user_name,
            "first_name": first_name,
            "last_name": last_name,
            "date_joined": date_joined,
        }
    )
