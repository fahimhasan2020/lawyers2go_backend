"""Upload views - same endpoints as old Express /upload"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_photo(request):
    return Response({'data': {'url': ''}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_file(request):
    return Response({'data': {'url': ''}}, status=status.HTTP_200_OK)
