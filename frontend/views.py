from django.shortcuts import render, redirect


def lists(request):
    return render(request, "frontend/lists.html")


def tasksIntermediate(request, listid):
    listtitle = request.session.get("lists").get(listid)
    request.session["selected_list_id"] = listid
    request.session["selected_list_title"] = listtitle
    return redirect("/tasks")


def tasks(request):
    print(request.session.get("selected_list_id"))
    print(request.session.get("selected_list_title"))
    context = {
        "listid": request.session.get("selected_list_id"),
        "listtitle": request.session.get("selected_list_title"),
    }
    return render(request, "frontend/tasks.html", context)
