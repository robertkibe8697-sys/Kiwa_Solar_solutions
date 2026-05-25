from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('projects/', views.projects, name='projects'),
path('contact/', views.contact_page, name='contact'),
 path('api/contact/', views.contact, name='api_contact'),
]