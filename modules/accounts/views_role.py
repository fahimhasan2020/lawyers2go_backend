"""Role views - same endpoints as old Express /role"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Role
from .serializers import RoleSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_roles(request):
    roles = Role.objects.filter(is_deleted=False)
    return Response({'data': RoleSerializer(roles, many=True).data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def system_roles(request):
    roles = Role.objects.filter(is_system_user=True, is_deleted=False)
    return Response({'data': RoleSerializer(roles, many=True).data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_role(request, id):
    try:
        role = Role.objects.get(pk=id)
        return Response({'data': RoleSerializer(role).data}, status=status.HTTP_200_OK)
    except Role.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    try:
        role = Role.objects.get(pk=id)
        ser = RoleSerializer(role, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data': ser.data}, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    except Role.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    try:
        role = Role.objects.get(pk=id)
        role.is_deleted = True
        role.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Role.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    ser = RoleSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({'data': ser.data}, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def hard_delete(request, id):
    try:
        role = Role.objects.get(pk=id)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Role.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
