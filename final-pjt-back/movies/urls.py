from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('top_movies/', views.top_movies),
    path('now_movies/', views.now_movies),
]
