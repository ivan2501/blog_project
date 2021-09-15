from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()

    context = {
        "posts": Post.objects.all(), #posts se koristi vo html  - Post.objects.all() e celata baza
        "title": "Blog Home"
    }

    return render(request, "blog/home.html", context=context)

# Create your views here.
def about(request):
    context = {
        "title": "Blog About"
    }

    return render(request, "blog/about.html", context=context)