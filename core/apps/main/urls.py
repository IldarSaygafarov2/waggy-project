from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.render_home_page, name='home-page'),
    path('contacts/', views.render_contact_page, name='contact-page'),
    path('about/', views.render_about_page, name='about-page'),
    path('faqs/', views.render_faqs_page, name='faqs-page'),
]
