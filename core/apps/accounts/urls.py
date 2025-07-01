from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.render_account_page, name='home-page'),
]