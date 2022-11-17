from django.urls import path
from .import views

app_name="community"

urlpatterns = [
    path('', views.community_create),
    path('<int:community_pk>/comment/', views.comment_create)

]
