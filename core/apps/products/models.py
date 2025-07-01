from django.db import models

from core.apps.common.models import BaseModel


class ProductSizeChoices(models.TextChoices):
    XL = 'XL', 'XL'
    L = 'L', 'L'
    M = 'M', 'M'
    S = 'S', 'S'


class ProductColorChoices(models.TextChoices):
    RED = 'RED', 'RED'
    BLUE = 'BLUE', 'BLUE'
    BLACK = 'BLACK', 'BLACK'
    GRAY = 'GRAY', 'GRAY'


class ProductBrand(BaseModel):
    name = models.CharField(verbose_name='название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд продукта'
        verbose_name_plural = 'Бренды продуктов'


class ProductTag(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег продукта'
        verbose_name_plural = 'Теги продуктов'


class Product(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(verbose_name='Короткая ссылка', help_text='Данное поле заполнять не нужно')
    preview = models.ImageField(verbose_name='Превью', upload_to='products/previews/', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    additional = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    quantity = models.IntegerField(verbose_name='Количество', default=5)
    sku = models.CharField(verbose_name='SKU', max_length=150, unique=True)
    category = models.ManyToManyField("categories.Category", related_name="products",
                                      verbose_name='Категория')
    size = models.CharField(verbose_name='Размер', choices=ProductSizeChoices.choices, max_length=2, null=True,
                            blank=True)
    color = models.CharField(verbose_name='Цвет', choices=ProductColorChoices.choices, max_length=10, null=True,
                             blank=True)
    brand = models.ForeignKey(ProductBrand, verbose_name='Бренд', on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(ProductTag, related_name='tags', verbose_name='Теги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Продукт')
    image = models.ImageField(verbose_name='Фото', upload_to='products/images/')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотки продуктов'
