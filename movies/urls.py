from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    #path('create_movie/', views.create_movie, name='create_movie'),
    #path('create_screening/', views.create_screening, name='create_screening'),
]
