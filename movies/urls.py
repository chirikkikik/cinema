from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ScreeningViewSet
from movies import views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'screenings', ScreeningViewSet)


urlpatterns = [
    path('', views.home_page, name='home'),
    path('', include(router.urls)),
    
]
