from django.urls import path
from . import views

urlpatterns = [
    # 캐릭터
    path('', views.character_list),
    path('create/', views.character_create),
    path('<int:id>/', views.character_detail),
    path('<int:id>/change/', views.set_character_detail),

    # 캐릭터 포지션
    path('positions/', views.position_list),
    path('positions/create/', views.position_create),
    path('positions/<int:id>/', views.position_detail),
    path('positions/<int:id>/change/', views.set_position_detail),

    # 캐릭터 인격
    path('personas/', views.persona_list),
]
