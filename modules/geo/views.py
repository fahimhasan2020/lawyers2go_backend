"""Geo module views - placeholder responses for all endpoints."""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data or []}, status=status.HTTP_200_OK)


# Country
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def country_list_create(request):
    if request.method == 'GET':
        return _ok([])
    return Response({'data': {}}, status=status.HTTP_201_CREATED if request.method == 'POST' else status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, id):
    if request.method == 'GET':
        return _ok({})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# State
@api_view(['GET'])
@permission_classes([AllowAny])
def state_list(request):
    return _ok([])


@api_view(['GET', 'PUT', 'DELETE'])
def state_detail(request, id):
    if request.method == 'GET':
        return _ok({})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


@api_view(['POST'])
def state_create(request):
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


# County
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def county_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([])
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def county_detail(request, id):
    if request.method == 'GET':
        return _ok({})
    if request.method == 'PUT':
        return _ok({})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# City
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def city_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([])
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def city_detail(request, id):
    return _ok({})


# CityRate
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def city_rate_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# StateSubscriptionRate
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def state_subscription_rate_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})
