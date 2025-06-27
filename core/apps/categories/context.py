from django.http import HttpRequest

from core.apps.categories.models import Category
from core.apps.categories.schemas import CategorySchema


def get_categories(request: HttpRequest) -> dict[str, list[CategorySchema]]:
    categories = [category.to_entity() for category in Category.objects.all()]
    return {'categories': categories}
