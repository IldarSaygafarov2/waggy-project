from django.db import models
from django.urls import reverse

from core.apps.categories.schemas import CategorySchema
from core.apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Короткая ссылка', help_text='Данное поле заполнять не нужно')
    icon = models.ImageField(verbose_name='Иконка', upload_to='categories/icons/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("categories:category-products", kwargs={"category_slug": self.slug})

    def to_entity(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
            slug=self.slug,
            icon=self.icon.url if self.icon else None
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
