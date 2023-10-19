from django.shortcuts import render, redirect

from todo.frorms import TaskForm

from.models import Task


def home(request):
     
    tasks = Task.objects.all()
    print(tasks)

   
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        tasks = Task.objects.create(name=name, priority=priority,date=date)
        tasks.save()
        return redirect('todo:home')
    
    context = {
        'tasks': tasks
    }

    return render(request, 'home.html',context=context)


def delete(request, id):

    if request.method == 'POST':
        if Task.objects.filter(id=id).exists():
            task = Task.objects.get(id=id)
            task.delete()
            return redirect('todo:home')
        else:
            pass
    
    return render(request,'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('todo:home')
    
    context = {
        'form': form
    }

    return render(request, 'update.html', context=context)