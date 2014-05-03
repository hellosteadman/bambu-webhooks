from django.shortcuts import render, redirect
from django.contrib import messages
from testproject.myapp.forms import ExampleForm

def home(request):
    form = ExampleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        messages.success(request, u'Thanks! Here\'s an alert box as your reward.')
        return redirect('/')
    
    return render(request, 'home.html',
        {
            'form': form
        }
    )