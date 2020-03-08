from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import CharacterSerializer, PositionSerializer, PersonaSerializer, PersonaChildSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Character, Position, Persona

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



# 캐릭터 인격 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def persona_list(request):
    personas = Persona.objects.all()
    serializer = PersonaSerializer(personas, many=True)
    return JsonResponse(serializer.data, safe=False)


# 캐릭터 인격 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def persona_create(request, parent_id):
    parent = None
    if parent_id != 0:
        parent = get_object_or_404(Persona, id=parent_id)
    child_serializer = PersonaChildSerializer(data=request.data)
    if child_serializer.is_valid():
        persona_parent = child_serializer.save(persona_parent=parent)
        serializer = PersonaSerializer(persona_parent)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 캐릭터 인격 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def persona_detail(request, id):
    persona = get_object_or_404(Persona, id=id)
    serializer = PersonaSerializer(persona)
    return JsonResponse(serializer.data)


# 캐릭터 인격 수정
@api_view(['PUT'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def update_persona_detail(request, child_id, parent_id):
    persona = get_object_or_404(Persona, id=child_id)
    parent = None
    if parent != 0:
        parent = get_object_or_404(Persona, id=parent_id)
    serializer = PersonaSerializer(persona, data=request.data)
    if serializer.is_valid():
        serializer.save(persona_parent=parent)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 캐릭터 인격 삭제
@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def delete_persona_detail(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.delete()
    return HttpResponse(status=204)
