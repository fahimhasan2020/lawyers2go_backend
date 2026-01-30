from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def contact_create(request):
    return Response({'message': 'OK', 'data': {}}, status=status.HTTP_201_CREATED)
