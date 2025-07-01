from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import BlogPost


def render_blog_page(request: HttpRequest) -> HttpResponse:
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'apps/blog/index.html', context)
