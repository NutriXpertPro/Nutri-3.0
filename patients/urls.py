from django.urls import path
from .views import PatientListAPIView

urlpatterns = [
    path("patients/", PatientListAPIView.as_view(), name="patient-list"),
]
