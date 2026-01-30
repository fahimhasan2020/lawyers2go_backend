from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def create_setting(request):
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_setting(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_stripe_public_key(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_setting(request, id):
    return Response({'data': {}}, status=status.HTTP_200_OK)
