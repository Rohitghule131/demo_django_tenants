import os

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from utilities.utils import ResponseInfo
from .serializers import (PatientSerializer, PhysicianSerializer, AppointmentSerializer,AppointmentListSerializer)
from .models import Physician,Patient,Appointment


class AddPhysicianAPIView(CreateAPIView):
    """
    Class to create api for adding book.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PhysicianSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(AddPhysicianAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])


class AddPatientAPIView(CreateAPIView):
    """
    Class to create api for adding book.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PatientSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(AddPatientAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])


class AddAppointmentAPIView(CreateAPIView):
    """
    Class to create api for adding book.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = AppointmentSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(AddAppointmentAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])


class ListPhysicianAPIView(ListAPIView):
    """
    Class to create api for listing physician.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PhysicianSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(ListPhysicianAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        return Physician.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer(request.data)

        self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])
    

class ListPatientAPIView(ListAPIView):
    """
    Class to create api for listing physician.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PatientSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(ListPatientAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        return Patient.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer()

        self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])


class ListAppointmentAPIView(ListAPIView):
    """
    Class to create api for listing physician.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = AppointmentListSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(ListAppointmentAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        return Appointment.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Post method to save physician details.
        """
        serializer = self.get_serializer()

        self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])



