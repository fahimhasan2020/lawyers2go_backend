from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data if data is not None else []}, status=status.HTTP_200_OK)


# Plan
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def plan_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def plan_by_city(request, cityId):
    return _ok({})


def provider_plan(request):
    return _ok({})


# Subscription
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def subscription_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def subscription_plan(request):
    return _ok({})


def subscription_on(request):
    return _ok({})


def subscription_auto_renewal_off(request):
    return Response(status=status.HTTP_204_NO_CONTENT)


def subscription_history(request):
    return _ok([])


def subscription_billing(request):
    return _ok({})


def retrieve_subscription(request):
    return _ok({})


def resume_subscription(request):
    return _ok({})


def renewal_subscription(request):
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


def cancel_subscription(request):
    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_subscription_by_id(request, id):
    return Response(status=status.HTTP_204_NO_CONTENT)


# SubscriptionTier
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def subscription_tier_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


def active_subscription_tier(request):
    return _ok([])


def subscription_tier_activation(request):
    return _ok({})


def provider_view_case(request):
    return _ok({})


# Package
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def package_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# Coupon
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def coupon_list_create(request, id=None):
    if request.method == 'GET':
        return _ok([] if id is None else {})
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


# UserSubscription
def user_subscription_list(request):
    return _ok([])


def user_subscription_details(request, id):
    return _ok({})
