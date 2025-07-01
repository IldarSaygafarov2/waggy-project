from django.db import models

from core.apps.common.models import BaseModel


class Banner(BaseModel):
    image = models.ImageField(verbose_name='Фото', upload_to='banners/')
    short_description = models.CharField(verbose_name='Краткое описание', max_length=100)
    description = models.CharField(verbose_name='Текст', max_length=150)
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, verbose_name='Категория',
                                 null=True)

    def __str__(self):
        return self.description

    def get_image(self):
        if not self.image:
            return ""
        return self.image.url

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'
