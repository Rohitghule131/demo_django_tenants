from django.urls import path

from .views import (
    UserSignupAPIView,
    UserLoginAPIView,
)


urlpatterns = [
    path("users/signUp", UserSignupAPIView.as_view(), name="sign-up"),
    path("users/login", UserLoginAPIView.as_view(), name="login-user"),
]

