from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('top_movies/', views.top_movies),
    path('now_movies/', views.now_movies),
    path('<int:movie_pk>/review/', views.review_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_update_delete),
    path('<int:movie_pk>/likes/', views.likes)
]
