from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .models import Task, List
from .serializers import TaskSerializer, ListSerializer, UserSerialzer

User = get_user_model()


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Tasks': '/tasks/',
        'TaskDetail': '/task-detail/<str:pk>/',
        'TaskCreate': '/task-create/',
        'TaskUpdate': '/task-update/<str:pk>/',
        'TaskDelete': '/task-delete/<str:pk>/',

        'Lists': 'lists/<str:username>',
        'ListDetail': '/list-detail/<str:pk>/',
        'ListCreate': '/list-create/',
        'ListUpdate': '/list-update/<str:pk>/',
        'ListDelete': '/list-delete/<str:pk>/',

        'GetUserId': 'get-user-id/<str:username>'
    }
    return Response(api_urls)


@api_view(['GET'])
def tasks(request, listid):
    tasks = Task.objects.filter(_list_id=listid)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item succesfully deleted!")


@api_view(['GET'])
def lists(request, username):
    # query = f"SELECT AL.ID, USER_ID AS USER, AL.TITLE AS LIST_TITLE, COUNT(TSK._LIST_ID) AS TASKS_COUNT FROM PUBLIC.AUTH_USER AU,PUBLIC.API_LIST AL,PUBLIC.API_TASK TSK WHERE AL.USER_ID = AU.ID AND AL.ID = TSK._LIST_ID AND AU.USERNAME = 'soumya_ranjan' GROUP BY AL.ID,TSK._LIST_ID"
    query = f"SELECT AL.ID, AL.TITLE, AL.USER_ID FROM PUBLIC.AUTH_USER AU,PUBLIC.API_LIST AL WHERE AL.USER_ID = AU.ID AND AU.USERNAME = '{username}'"
    lists = List.objects.raw(query)
    request.session["lists"] = {}
    for lst in lists:
        request.session["lists"][lst.id] = lst.title

    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listDetail(request, pk):
    _list = List.objects.get(id=pk)
    serializer = ListSerializer(_list, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def listCreate(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def listUpdate(request, pk):
    _list = List.objects.get(id=pk)
    serializer = ListSerializer(instance=_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def listDelete(request, pk):
    print(f"pk passed in = {pk}")
    _list = List.objects.get(id=pk)
    _list.delete()
    return Response("List successfully deleted!")


@api_view(['GET'])
def getUserId(request, username):
    query = f"SELECT ID,USERNAME,EMAIL FROM PUBLIC.AUTH_USER AU WHERE AU.USERNAME = '{username}'"
    querySet = User.objects.raw(query)
    for rec in querySet:
        username = rec.username
        userid = rec.id
    return JsonResponse({'username': username, 'id': userid})
