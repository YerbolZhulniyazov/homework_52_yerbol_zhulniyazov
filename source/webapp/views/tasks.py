from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from webapp.models import Task


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    task = Task.objects.create(**task_data)
    return redirect(f'/task/?pk={task.pk}')


def detail_view(request):
    task_id = request.GET.get('pk')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task.html', context=context)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/'


class TaskUpdateView(UpdateView):
    model = Task
    fields = [
        'title',
        'description',
        'status',
        'completion_date'
    ]
    template_name = 'update_task.html'
    success_url = '/'
