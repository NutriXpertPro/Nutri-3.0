from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient  # Importar o modelo Patient


@login_required
def dashboard_view(request):
    patients = Patient.objects.filter(user=request.user)
    context = {"patients": patients}
    return render(request, "dashboard.html", context)
