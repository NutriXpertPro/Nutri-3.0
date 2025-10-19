from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Patient
from anamnesis.models import Anamnesis
from evaluations.models import Evaluation
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated


class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra pacientes pelo usuário logado (nutricionista)
        return self.queryset.filter(user=self.request.user)

@login_required
def patient_detail_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id, user=request.user)
    anamnesis = Anamnesis.objects.filter(patient=patient).order_by('-created_at').first()
    evaluations = Evaluation.objects.filter(patient=patient).order_by('-date')

    context = {
        'patient': patient,
        'anamnesis': anamnesis,
        'evaluations': evaluations,
    }
    return render(request, 'patients/patient_detail.html', context)
