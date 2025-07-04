# Generated by Django 5.2.3 on 2025-06-27 10:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Данное поле заполнять не нужно', verbose_name='Короткая ссылка')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='categories/icons/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
