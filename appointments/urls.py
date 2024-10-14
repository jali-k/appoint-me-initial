from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", views.schedule_appointment, name="schedule_appointment"),
    path("my-appointments/", views.my_appointments, name="my_appointments"),
]
