from rest_framework import serializers
from django.contrib.auth import get_user_model

# Use the CustomUser model (since it extends AbstractUser)
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']  # Add 'role' if needed for serialization

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only for security
        }

    def create(self, validated_data):
        # Use create_user to automatically hash the password
        user = CustomUser.objects.create_user(**validated_data)
        return user

