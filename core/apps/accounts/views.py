from django.shortcuts import render

from django.http import HttpRequest, HttpResponse


def render_account_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'apps/account/index.html')