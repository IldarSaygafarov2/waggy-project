from django.shortcuts import render

from django.http import HttpRequest, HttpResponse


def render_home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home/index.html")
