from django.urls import path

from .views import (
                    GetUsersAPIView,
                    LoginUserAPIView,
                    SignUpUserAPIView
                 )


urlpatterns = [
    path("signUp", SignUpUserAPIView.as_view(), name="sign-up"),
    path("login", LoginUserAPIView.as_view(), name="login"),
    path("getUsers", GetUsersAPIView.as_view(), name="get-users"),
]

