from rest_framework import (
                            status,
                            generics
                           )
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import (BaseAuthentication, BasicAuthentication, SessionAuthentication)

from .models import (CustomToken, CustomUser)
from .serializers import (
                          GetUsersSerializer,
                          LoginUserSerializer,
                          SignInUserSerializer
                         )


class SignUpUserAPIView(generics.CreateAPIView):
    """
    Class for creating api for sign up user.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = SignInUserSerializer

    def post(self, request, *args, **kwargs):
        """
        Post Method for sign up user.
        """
        signup_serializer = self.get_serializer(data=request.data)

        if signup_serializer.is_valid(raise_exception=True):
            signup_serializer.save()
            return Response({"SUCCESS", status.HTTP_201_CREATED})

        return Response({status.HTTP_400_BAD_REQUEST})


class LoginUserAPIView(ObtainAuthToken, generics.CreateAPIView):
    """
    Class for create api for user login.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        """
        Post method for login user with session authentication.
        """

        login_serializer = self.get_serializer(data=request.data)
        try:
            if login_serializer.is_valid(raise_exception=True):
                email = login_serializer.validated_data.get("email", None)
                password = login_serializer.validated_data.get("password", None)
                user = authenticate(request, **request.data)
                if user is not None:
                    token, created_at = CustomToken.objects.get_or_create(email=email, user_id=user.id)
                    return Response({"Token": token.key})
                else:
                    raise Exception("Invalid credential.")

        except CustomUser.DoesNotExist:
            return Response({"User does not exist."})

        except BaseException as e:
            return Response({"ERROR": "{}".format(e)})


class GetUsersAPIView(generics.ListAPIView):
    """
    Class for create list of user api.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = GetUsersSerializer

    def get(self, request, *args, **kwargs):
        """
        Get method for get list of user.
        """
        get_users_serializer = super().list(request, *args, **kwargs)
        return Response({"Users": get_users_serializer.data})


