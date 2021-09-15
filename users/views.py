from django.shortcuts import render
from .forms import UserCreationForm

def Register(request):
    form = UserCreationForm()
    return render (request, 'users/register.html', {'form': form})