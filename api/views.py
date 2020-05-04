from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task, List
from .serializers import TaskSerializer, ListSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Tasks': '/tasks/',
        'TaskDetail': '/task-detail/<str:pk>/',
        'TaskCreate': '/task-create/',
        'TaskUpdate': '/task-update/<str:pk>/',
        'TaskDelete': '/task-delete/<str:pk>/',

        'Lists': '/lists/',
        'ListDetail': '/list-detail/<str:pk>/',
        'ListCreate': '/list-create/',
        'ListUpdate': '/list-update/<str:pk>/',
        'ListDelete': '/list-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasks(request):
    tasks = Task.objects.all()
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
def lists(request):
    lists = List.objects.all()
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
    serializer = TaskSerializer(instance=_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def listDelete(request, pk):
    _list = List.objects.get(id=pk)
    _list.delete()
    return Response("List successfully deleted!")
