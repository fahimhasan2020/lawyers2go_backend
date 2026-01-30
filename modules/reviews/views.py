from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data if data is not None else []}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def review_list_create(request):
    if request.method == 'GET':
        return _ok([])
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    if request.method == 'GET':
        return _ok({})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def provider_reviews(request):
    return _ok([])


def provider_reviews_and_rating(request):
    return _ok({})


def client_reviews(request):
    return _ok([])
