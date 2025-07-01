from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.render_blog_page, name='home-page'),
]