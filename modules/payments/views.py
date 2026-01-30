from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


def _ok(data=None):
    return Response({'data': data if data is not None else {}}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def payment_view(request, cardId=None, id=None):
    if request.method == 'GET':
        return _ok({} if cardId or id else [])
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
    return _ok({})


@api_view(['POST'])
def create_card_token(request):
    return _ok({})


@api_view(['POST'])
def create_bank_account_token(request):
    return _ok({})


@api_view(['POST'])
def calculate_service_fee_and_tax(request):
    return _ok({})


@api_view(['POST'])
def client_quote_tax(request):
    return _ok({})


@api_view(['POST'])
def subscription_tax(request):
    return _ok({})


@api_view(['POST'])
def calculate_tax(request):
    return _ok({})


@api_view(['POST'])
def get_calculated_tax(request):
    return _ok({})


@api_view(['POST'])
def tax_register(request):
    return _ok({})


@api_view(['GET', 'PUT'])
def tax_register_update(request, id):
    return _ok({})


@api_view(['GET'])
def tax_register_list(request):
    return _ok([])


@api_view(['GET', 'POST'])
def tax_calculate(request, id=None):
    return _ok({})
