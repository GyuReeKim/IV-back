from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:id>/', views.user_detail),
    path('users/<int:id>/profile/', views.user_profile),
]
