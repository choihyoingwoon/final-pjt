from django.urls import path
from .import views

app_name="community"

urlpatterns = [
    path('', views.community_create),
    path('<int:community_pk>/', views.community_update_delete),
    path('<int:community_pk>/comment/', views.comment_create),
    path('<int:community_pk>/comment/<int:comment_pk>', views.comment_update_delete),

]
