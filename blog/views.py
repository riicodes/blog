from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'blog/home.html', {'posts': posts})
