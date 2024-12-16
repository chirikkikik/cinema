from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('register/', views.register_view, name='register'),
    path('user_profile/', views.user_profile, name='profile'),
]

