from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Banner


def render_home_page(request: HttpRequest) -> HttpResponse:
    banners = Banner.objects.all()
    context = {
        'banners': banners,
    }
    return render(request, "apps/main/index.html", context)


def render_contact_page(request: HttpRequest) -> HttpResponse:
    return render(request, "apps/main/contact.html")


def render_about_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'apps/main/about.html')


def render_faqs_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'apps/main/faqs.html')