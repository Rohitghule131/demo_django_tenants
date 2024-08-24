from django.urls import path

from .views import (
    AddPatientAPIView,
    ListPatientAPIView,
    AddPhysicianAPIView,
    AddAppointmentAPIView,
    ListPhysicianAPIView,
    ListAppointmentAPIView
)


urlpatterns = [
    path("physician/create", AddPhysicianAPIView.as_view(), name="add-physician"),
    path("patient/create", AddPatientAPIView.as_view(), name="add-patient"),
    path("appointment/create", AddAppointmentAPIView.as_view(), name="add-appointment"),
    path("physician/list", ListPhysicianAPIView.as_view(), name="list-physician"),
    path("appointment/list", ListAppointmentAPIView.as_view(), name="list-appointment"),
    path("patient/list", ListPatientAPIView.as_view(), name="list-patient"),

]
