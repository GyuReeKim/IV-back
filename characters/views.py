from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import CharacterSerializer, PositionSerializer, PersonaSerializer, PersonaChildSerializer, TraitSerializer, SurvivorSerializer, SurvivorSetSerializer, HunterSerializer, HunterSetSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Character, Position, Persona, Trait, Survivor, Hunter

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



# 캐릭터 보조 특성 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def trait_list(request):
    traits = Trait.objects.all()
    serializer = TraitSerializer(traits, many=True)
    return JsonResponse(serializer.data, safe=False)


# 캐릭터 보조 특성 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def trait_create(request):
    serializer = TraitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 캐릭터 보조 특성 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def trait_detail(request, id):
    trait = get_object_or_404(Trait, id=id)
    serializer = TraitSerializer(trait)
    return JsonResponse(serializer.data)


# 캐릭터 보조 특성
@api_view(['PUT', 'DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def set_trait_detail(request, id):
    trait = get_object_or_404(Trait, id=id)

    # 캐릭터 보조 특성 수정
    if request.method == "PUT":
        serializer = TraitSerializer(trait, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse(status=400)
        
    # 캐릭터 보조 특성 삭제
    elif request.method == "DELETE":
        trait.delete()
        return HttpResponse(status=204)



# 생존자 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def survivor_list(request):
    survivors = Survivor.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    return JsonResponse(serializer.data, safe=False)


# 생존자 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def survivor_create(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    set_serializer = SurvivorSetSerializer(data=request.data)
    if set_serializer.is_valid():
        survivor = set_serializer.save(character=character)
        serializer = SurvivorSerializer(survivor)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 생존자 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def survivor_detail(request, id):
    survivor = get_object_or_404(Survivor, id=id)
    serializer = SurvivorSerializer(survivor)
    return JsonResponse(serializer.data)


# 생존자 수정
@api_view(['PUT'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def update_survivor_detail(request, survivor_id, character_id):
    survivor = get_object_or_404(Survivor, id=survivor_id)
    character = get_object_or_404(Character, id=character_id)
    set_serializer = SurvivorSetSerializer(survivor, data=request.data)
    if set_serializer.is_valid():
        update_survivor = set_serializer.save(character=character)
        serializer = SurvivorSerializer(update_survivor)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 생존자 삭제
@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def delete_survivor_detail(request, id):
    survivor = get_object_or_404(Survivor, id=id)
    survivor.delete()
    return HttpResponse(status=204)



# 감시자 리스트
@api_view(['GET'])
@permission_classes((AllowAny,))
def hunter_list(request):
    hunters = Hunter.objects.all()
    serializer = HunterSerializer(hunters, many=True)
    return JsonResponse(serializer.data, safe=False)


# 감시자 생성
@api_view(['POST'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def hunter_create(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    set_serializer = HunterSetSerializer(data=request.data)
    if set_serializer.is_valid():
        hunter = set_serializer.save(character=character)
        serializer = HunterSerializer(hunter)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 감시자 정보
@api_view(['GET'])
@permission_classes((AllowAny,))
def hunter_detail(request, id):
    hunter = get_object_or_404(Hunter, id=id)
    serializer = SurvivorSerializer(hunter)
    return JsonResponse(serializer.data)


# 감시자 수정
@api_view(['PUT'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def update_hunter_detail(request, hunter_id, character_id):
    hunter = get_object_or_404(Hunter, id=hunter_id)
    character = get_object_or_404(Character, id=character_id)
    set_serializer = HunterSetSerializer(hunter, data=request.data)
    if set_serializer.is_valid():
        update_hunter = set_serializer.save(character=character)
        serializer = HunterSerializer(update_hunter)
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


# 감시자 삭제
@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
@authentication_classes((JSONWebTokenAuthentication,))
def delete_hunter_detail(request, id):
    hunter = get_object_or_404(Hunter, id=id)
    hunter.delete()
    return HttpResponse(status=204)
