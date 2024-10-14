from django.db import models
from authentication.models import (
    User,
)  # Link to the User model in the authentication app


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    is_available = models.BooleanField(default=True)


class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Scheduled", "Scheduled"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
    )
