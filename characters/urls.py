from django.urls import path
from . import views

urlpatterns = [
    # 캐릭터
    path('', views.character_list),
]
