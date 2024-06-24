from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class CustomUserSignUpSerializer(serializers.ModelSerializer):
    """
    Serializer class for signing up users.
    """
    class Meta:
        model = CustomUser
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_password(self, password):
        """
        Function for validating password.
        """
        password_length = len(password)

        if not 8 <= password_length <= 15:
            raise serializers.ValidationError("Password length should be between 8 and 15.")
        return password

    def create(self, validated_data):
        """
        Function for creating and returning the created instance
        based on the validated data of the user.
        """
        user = CustomUser.objects.create_user(
            name=validated_data.pop('name'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Class for authorizing user for correct login credentials.
    """
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'invalid_credentials': 'Email id or password is invalid.',
    }

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def __init__(self, *args, **kwargs):
        """
        Constructor Function for initializing UserLoginSerializer.
        """
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        """
        Function to validate user credentials.
        """
        self.user = authenticate(username=attrs.pop("email"), password=attrs.pop('password'))
        if self.user:
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class GetUsersSerializer(serializers.ModelSerializer):
    """
    Class for serializer for list of users.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email")


