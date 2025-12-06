from django.urls import path
from . import views

app_name = 'bibiapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('generic/', views.generic, name='generic'),
    path('single/', views.single, name='single'),
    path('styles/', views.style_guide, name='styles'),
]
