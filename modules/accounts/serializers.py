from rest_framework import serializers
from .models import User, Role, Provider, Client


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'profile_picture', 'phone_number',
                  'email_verified', 'account_status', 'country_id', 'state_id', 'county_id', 'city_id', 'zip_code',
                  'address', 'is_active', 'is_deleted', 'created_at', 'updated_at']
        read_only_fields = ['id']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'role', 'phone_number']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
