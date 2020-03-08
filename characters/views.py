from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import CharacterSerializer, PositionSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Character, Position

# Create your views here.

# 캐릭터 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def character_list(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return JsonResponse(serializer.data, safe=False)


# 캐릭터 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def character_create(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 캐릭터 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def character_detail(request, id):
    character = get_object_or_404(Character, id=id)
    serializer = CharacterSerializer(character)
    return JsonResponse(serializer.data)


# 캐릭터
@api_view(['PUT', 'DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def set_character_detail(request, id):
    character = get_object_or_404(Character, id=id)

    # 캐릭터 수정
    if request.method == "PUT":
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse(status=400)
        
    # 캐릭터 삭제
    elif request.method == "DELETE":
        character.delete()
        return HttpResponse(status=204)



# 캐릭터 포지션 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def position_list(request):
    positions = Position.objects.all()
    serializer = PositionSerializer(positions, many=True)
    return JsonResponse(serializer.data, safe=False)


# 캐릭터 포지션 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def position_create(request):
    serializer = PositionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 캐릭터 포지션 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def position_detail(request, id):
    position = get_object_or_404(Position, id=id)
    serializer = PositionSerializer(position)
    return JsonResponse(serializer.data)


# 캐릭터 포지션
@api_view(['PUT', 'DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def set_position_detail(request, id):
    position = get_object_or_404(Position, id=id)

    # 캐릭터 포지션 수정
    if request.method == "PUT":
        serializer = PositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse(status=400)
        
    # 캐릭터 포지션 삭제
    elif request.method == "DELETE":
        position.delete()
        return HttpResponse(status=204)