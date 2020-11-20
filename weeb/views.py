from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone

now = timezone.now()

from .forms import *

# Create your views here.

def ViewMainPage(request):
    posts = Post.objects.all()

    manga = Post.objects.filter(type='Manga').count()
    manhwa = Post.objects.filter(type='Manhwa').count()
    manhua = Post.objects.filter(type='Manhua').count()
    anime = Post.objects.filter(type='Anime').count()
    all = Post.objects.all().count()

    context = {
        'posts': posts,
        'manga':manga,
        'manhwa':manhwa,
        'manhua':manhua,
        'anime':anime,
        'all':all,
    }
    return render(request, 'public/index.html', context)

def ViewType(request, type):

    allofthem = Post.objects.filter(type=type.capitalize())

    context = {
        'posts': allofthem
    }
    return render(request, 'public/section.html', context)

def ViewPost(request, postID):

    post = Post.objects.get(id=postID)

    context = {
        'post': post
    }
    return render(request, 'public/post.html', context)

def ViewAll(request):
    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'public/all.html', context)