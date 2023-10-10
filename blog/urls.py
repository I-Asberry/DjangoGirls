from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('pst/<int:pk>/', views.post_dtail, name='post_detail'),
]