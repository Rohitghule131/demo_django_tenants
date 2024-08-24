from rest_framework import serializers

from users.models import CustomUser
from .models import Physician,Patient,Appointment


class PhysicianSerializer(serializers.ModelSerializer):
    """
    Class to create doctor serializer.
    """
    class Meta:
        model = Physician
        fields = ("id", "name", "specialization", "license_number", "email", "created_at", "updated_at")


class PatientSerializer(serializers.ModelSerializer):
    """
    Class to create patient serializer.
    """
    class Meta:
        model = Patient
        fields = ("id", "name", "phone_number", "date_of_birth", "gender", "address", "emergency_contact", "created_at", "updated_at")


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Class to create patient serializer.
    """

    class Meta:
        model = Appointment
        fields = ("id", "patient", "physician", "appointment_date", "reason_for_visit", "diagnosis", "prescription", "status", "created_at", "updated_at")


class AppointmentListSerializer(serializers.ModelSerializer):
    """
    Class to create patient serializer.
    """
    patient = PatientSerializer()
    physician = PhysicianSerializer()

    class Meta:
        model = Appointment
        fields = ("id", "patient", "physician", "appointment_date", "reason_for_visit", "diagnosis", "prescription", "status", "created_at", "updated_at")


