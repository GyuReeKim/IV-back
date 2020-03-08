from django.urls import path
from . import views

urlpatterns = [
    # 캐릭터
    path('', views.character_list),
    path('create/', views.character_create),
    path('<int:id>/', views.character_detail),
    path('<int:id>/change/', views.set_character_detail),
]
