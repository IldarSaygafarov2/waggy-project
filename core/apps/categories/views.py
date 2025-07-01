from django.http import HttpRequest
from django.shortcuts import HttpResponse, render


def render_shop_page(request: HttpRequest) -> HttpResponse:
    return render(request, "apps/categories/index.html")


def render_category_page(request: HttpRequest, category_slug: str):
    return HttpResponse(f'category with slug: {category_slug}')
