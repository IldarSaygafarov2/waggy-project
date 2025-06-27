from django.db import models

from core.apps.common.models import BaseModel


class BlogPostTag(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название тега")

    class Meta(BaseModel.Meta):
        verbose_name = "Тег поста"
        verbose_name_plural = "Теги постов"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class BlogPost(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    short_description = models.TextField(verbose_name="Краткое описание")
    content = models.TextField(verbose_name="Контент")
    preview = models.ImageField(
        upload_to="blog/previews/",
        null=True,
        blank=True,
        verbose_name="Заставка",
    )
    tags = models.ManyToManyField(
        BlogPostTag,
        related_name="blog_posts",
        blank=True,
        verbose_name="Теги",
    )

    class Meta(BaseModel.Meta):
        verbose_name = "Пост блога"
        verbose_name_plural = "Посты блога"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
