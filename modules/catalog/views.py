from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data if data is not None else []}, status=status.HTTP_200_OK)


# Category
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def category_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([])
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# Function
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def func_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([])
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# ServiceType
@api_view(['GET'])
@permission_classes([AllowAny])
def service_type_list(request):
    return _ok([])


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def service_type_detail(request, id=None):
    if request.method == 'GET':
        return _ok({} if id else [])
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def sub_service_types(request, id=None):
    return _ok([])


# Service
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def service_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def service_search(request):
    return _ok([])


def provider_services(request, id):
    return _ok([])


def my_services(request):
    return _ok([])


def b2b_search(request):
    return _ok([])


# ServiceFee
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def service_fee_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def service_fee_charge(request):
    return _ok({})
