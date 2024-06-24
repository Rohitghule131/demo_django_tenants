from django.db import models

# Create your models here.

class Physician(models.Model):
    """
    Class to create model for books.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    specialization = models.CharField(max_length=50, null=False, blank=False)
    license_number = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    address = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason_for_visit = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    prescription = models.TextField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)