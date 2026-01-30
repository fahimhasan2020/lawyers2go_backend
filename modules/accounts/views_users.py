"""User views - same endpoints as old Express /users"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def log_files(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def log_file_details(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_log_file(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def providers_list(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def list_or_create(request):
    if request.method == 'GET':
        return Response({'data': []}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response({'data': {}}, status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        return Response({'data': {}}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_clients(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_providers(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_system_users(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    from .serializers import UserSerializer
    return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_info(request):
    from .serializers import UserSerializer
    return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def provider_services_locations(request, providerId):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def provider_add_services_locations(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def provider_remove_services_locations(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_otp(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_otp(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def email_otp_verification(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def resend_email_otp(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_email(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def resend_email(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def forgot_password(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def reset_password(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_type_update(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def provider_type_update(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_provider_types(request):
    return Response({'data': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_client_profile(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_provider_profile(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def provider_profile_update_new(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_or_delete(request):
    if request.method == 'PUT':
        return Response({'data': {}}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_one(request, userId=None):
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_my_account(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_provider_details(request, providerId):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_email_update(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def confirm_email_update(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_by_id(request, userId):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_client_profile_by_id(request, userId):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_provider_profile_by_id(request, userId):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def provider_profile_update_by_id(request, userId):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def app_logout(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_admin(request):
    return Response({'data': {}}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_profile(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_admin_profile(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_provider_document(request, providerId):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payout_info(request):
    return Response({'data': {}}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_payout_info(request):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def generate_user_password_by_admin(request, id):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_user_account_by_admin(request, userId):
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, userId):
    if request.method == 'GET':
        return Response({'data': {}}, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        return Response({'data': {}}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_user(request, userId):
    return Response({'data': {}}, status=status.HTTP_200_OK)
