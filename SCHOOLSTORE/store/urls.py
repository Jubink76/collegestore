from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('form/', views.show_form, name='form'),
    path('get_courses/', views.get_courses, name='get_courses'),

]
