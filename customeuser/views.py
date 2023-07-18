from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (BaseAuthentication, BasicAuthentication, SessionAuthentication)

from .models import (
    CustomUser,
)
from .serializers import (
    GetUsersSerializer,
    UserLoginSerializer,
    CustomUserSignUpSerializer
)
from utilities.utils import ResponseInfo
from .utils import get_tokens_for_user
from utilities import messages



class UserSignupAPIView(CreateAPIView):
    """
    Class to create API for signing up users.
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CustomUserSignUpSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting web response to return.
        """
        self.response_format = ResponseInfo().response
        super(UserSignupAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        POST method for registering custom user and generation tokens.
        """
        user_serializer = self.get_serializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):

            user = user_serializer.save()

            jwt_tokens = get_tokens_for_user(user)
            response_data = {
                "user": user_serializer.data,
                "token": jwt_tokens
            }

            self.response_format["status_code"] = status.HTTP_201_CREATED
            self.response_format["data"] = response_data
            self.response_format["error"] = None
            self.response_format["messages"] = [messages.CREATED.format("User")]

        return Response(self.response_format)


class UserLoginAPIView(CreateAPIView):
    """
    Class for creating API view for user login.
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(UserLoginAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        """
        Method to return custom user queryset.
        """
        email = self.request.data.get("email")
        return CustomUser.objects.get(email=email)

    def post(self, request, *args, **kwargs):
        """
        POST Method for validating and logging in the user if valid.
        """
        try:
            user_serializer = self.get_serializer(data=request.data)
            if user_serializer.is_valid(raise_exception=True):
                user = self.get_queryset()

                jwt_token = get_tokens_for_user(user,)
                data = {
                    "id": user.id,
                    "token": jwt_token,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }

                self.response_format["data"] = data
                self.response_format["error"] = None
                self.response_format["status_code"] = status.HTTP_200_OK
                self.response_format["message"] = [messages.LOGIN_SUCCESS]

        except CustomUser.DoesNotExist:
            self.response_format["data"] = None
            self.response_format["error"] = "user"
            self.response_format["status_code"] = status.HTTP_404_NOT_FOUND
            self.response_format["message"] = [messages.UNAUTHORIZED_ACCOUNT]

        return Response(self.response_format)





class GetUsersAPIView(ListAPIView):
    """
    Class for create list of user api.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = GetUsersSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Get method for get list of user.
        """
        get_users_serializer = super().list(request, *args, **kwargs)
        return Response({"Users": get_users_serializer.data})


