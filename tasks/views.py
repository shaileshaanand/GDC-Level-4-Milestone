from django.http import HttpResponse
from django.shortcuts import render, redirect

TASKS = []
COMPLETED = []


def remove_task(index):
    task = TASKS[index - 1]
    del TASKS[index - 1]
    return task


def complete_task(index):
    task = remove_task(index)
    COMPLETED.append(task)


# Add all your views here
def tasks_view(request):
    task = request.GET["task"]
    TASKS.append(task)
    return redirect("/tasks")


def completed_tasks_view(request):
    return render(request, "completed_tasks.html", {"tasks": COMPLETED})


def all_tasks_view(request):
    return render(request, "tasks.html", {"tasks": TASKS})


def delete_task_view(request, index):
    remove_task(index)
    return redirect("/tasks")


def complete_task_view(request, index):
    complete_task(index)
    return redirect("/tasks")
