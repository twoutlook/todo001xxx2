from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

def index(request):
    qry = Todo.objects.order_by('seq')
    print(type(qry))

    user = request.user
    context = {'qry': qry}
    return render(request, 'index.html', context)

# https://docs.djangoproject.com/en/3.0/topics/forms/
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TodoForm()
    return render(request, 'add.html', {'form': form})

