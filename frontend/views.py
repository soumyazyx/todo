from django.shortcuts import render


def lists(request):
    return render(request, 'frontend/lists.html')


def tasks(request, listid):
    context = {
        'listid': listid
    }
    return render(request, 'frontend/tasks.html', context)
