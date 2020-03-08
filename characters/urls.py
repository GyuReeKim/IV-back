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
    path('personas/create/<int:parent_id>/', views.persona_create),
    path('personas/<int:id>/', views.persona_detail),
    path('personas/<int:child_id>/update/<parent_id>/', views.update_persona_detail),
    path('personas/<int:id>/delete/', views.delete_persona_detail),

    # 캐릭터 보조 특성
    path('traits/', views.trait_list),
    path('traits/create/', views.trait_create),
    path('traits/<int:id>/', views.trait_detail),
    path('traits/<int:id>/change/', views.set_trait_detail),

    # 생존자
    path('survivors/', views.survivor_list),
    path('survivors/create/<int:character_id>/', views.survivor_create),
    path('survivors/<int:id>/', views.survivor_detail),
    path('survivors/<int:survivor_id>/update/<character_id>/', views.update_survivor_detail),
    path('survivors/<int:id>/delete/', views.delete_survivor_detail),
]
