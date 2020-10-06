from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('funk',views.funk, name='funk'),
    path('bedroompop',views.bedroompop, name='bedroompop'),
    path('citypop',views.citypop, name='citypop'),
]

