from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import TodoList
import datetime


# Create your views here.
def todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        # print(task)
        todo_task = TodoList(task=task)
        todo_task.save()

    return redirect('fetch_task')


def fetch_task(request):
    all_task = TodoList.objects.all()
    date = datetime.datetime.now()
    # print(date)
    return render(request, 'todo.html', {'all_task': all_task, 'date': date})


def get_task_for_update(request, id):
    get_task = TodoList.objects.get(pk=id)
    # print(get_task)
    return render(request, 'todo.html', {'get_task': get_task})


def task_status(request, id):
    # print(request.POST, "request.POST")
    # keysList = list(request.POST.keys())
    # print('keysList',keysList)
    if request.method == 'POST':
        update_status = TodoList.objects.filter(pk=id)

        # print(update_status)
        if 'status' in request.POST :
            status = request.POST['status']# == status:
            print(status)
            update_status.update(status=status)
            
        # elif request.POST.keys() :  # == task:
        elif 'task' in request.POST :  # == task:
            task = request.POST.get('task')
            update_status.update(task=task)
            print(task)
    return redirect('fetch_task')

# def update_task(request, id):
#     if request.method == 'POST':
#         task = request.POST['task']
#         update_status = TodoList.objects.filter(pk=id)
#         update_status.update(task=task)
#         print(task)
#     return redirect('fetch_task')
