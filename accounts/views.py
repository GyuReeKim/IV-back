from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer, ProfileSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from .models import Profile

# Create your views here.

# 유저 리스트
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def user_list(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


# 유저
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def user_detail(request, id):
    user = get_object_or_404(get_user_model(), id=id)

    if request.user != user:
        return HttpResponse(status=403)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)



# 유저 프로필
@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def user_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    print(request.user.id)

    # 유저 프로필
    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)
    
    # 로그인 한 사람과 유저 프로필이 같다면
    if request.user.id == id:
        # 유저 프로필 변경
        if request.method == "PUT":
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return HttpResponse(status=400)