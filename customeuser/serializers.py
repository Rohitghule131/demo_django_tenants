from rest_framework import serializers

from .models import CustomUser


class SignInUserSerializer(serializers.ModelSerializer):
    """
    Class for serialize the data for creating user object.
    """
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "username", "password", "confirm_password")

    def validate(self, attrs):
        """
        Method for validated the data.
        """
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Password doesn't matched with the confirm password.")

        return attrs

    def create(self, validated_data):
        """
        Method for create user object in database.
        """
        username = validated_data.pop("username", None)
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        user = CustomUser.objects.create_user(username, email, password)
        return user


class LoginUserSerializer(serializers.Serializer):
    """
    Class for serialize login user data.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class GetUsersSerializer(serializers.ModelSerializer):
    """
    Class for serializer for list of users.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email")
