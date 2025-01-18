from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tjänster', views.services, name='services'),
    path('kontakt', views.contact, name='contact'),
    path('projekt', views.projects, name='projects'),

]
