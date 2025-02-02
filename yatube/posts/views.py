from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import POST_PER_PAGE


def index(request):
    posts = Post.objects.all()[:POST_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
