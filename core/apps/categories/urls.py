from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.render_shop_page, name='shop-page'),
    path('<slug:category_slug>/', views.render_category_page, name='category-products'),
]
