from django.urls import path
from . import views

urlpatterns = [
    path('api/get_movies/', views.get_movies, name='get_movies'),
]