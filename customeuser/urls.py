from django.urls import path

from .views import (
                    GetUsersAPIView,
                    UserLoginAPIView,
                    UserSignupAPIView
                 )


urlpatterns = [
    path("signUp", UserSignupAPIView.as_view(), name="sign-up"),
    path("login", UserLoginAPIView.as_view(), name="login"),
    path("getUsers", GetUsersAPIView.as_view(), name="get-users"),
]

