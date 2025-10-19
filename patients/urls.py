from django.urls import path
from .views import PatientListAPIView, patient_detail_view

urlpatterns = [
    path("patients/", PatientListAPIView.as_view(), name="patient-list"),
    path("patients/<int:patient_id>/", patient_detail_view, name="patient_detail"),
]
