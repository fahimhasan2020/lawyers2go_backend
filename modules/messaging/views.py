from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data if data is not None else []}, status=status.HTTP_200_OK)


# Conversation
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def conversation_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([])
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# Message
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def message_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})
