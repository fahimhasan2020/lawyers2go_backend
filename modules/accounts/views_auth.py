"""Auth views - same endpoints as old Express /auth"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    return Response({'message': 'Register endpoint'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_app(request):
    return Response({'message': 'Register app endpoint'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    return Response({'message': 'Login endpoint'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def facebook_login(request):
    return Response({'message': 'Facebook login'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def google_login(request):
    return Response({'message': 'Google login'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def apple_login(request):
    return Response({'message': 'Apple login (v1)'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def apple_login_v2(request):
    return Response({'message': 'Apple login (v2)'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_by_app(request):
    return Response({'message': 'Login by app'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def web_portal_login(request):
    return Response({'message': 'Web portal login'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    return Response({'message': 'Admin login'}, status=status.HTTP_200_OK)
