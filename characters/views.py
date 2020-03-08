from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import CharacterSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Character

# Create your views here.

# 캐릭터 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def character_list(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return JsonResponse(serializer.data, safe=False)