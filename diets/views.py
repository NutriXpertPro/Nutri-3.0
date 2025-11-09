from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DietForm
from .models import Diet
from patients.models import PatientProfile

@login_required
def diet_list(request):
    return render(request, "diets/diet_list.html")


@login_required
def diet_create(request, patient_pk=None):
    patient = None
    if patient_pk:
        patient = get_object_or_404(PatientProfile, pk=patient_pk, nutritionist=request.user)

    if request.method == "POST":
        form = DietForm(request.POST, user=request.user)
        if form.is_valid():
            try:
                diet = form.save()
                messages.success(request, "Dieta criada com sucesso!")
                return redirect("patients:detail", pk=diet.patient.pk)
            except Exception as e:
                messages.error(request, f"Ocorreu um erro ao criar a dieta: {e}")
        else:
            if 'meals' in form.errors or 'substitutions' in form.errors:
                messages.error(request, "O formato do JSON para Refeições ou Substituições é inválido. Verifique a sintaxe.")
            else:
                messages.error(request, "Formulário inválido. Corrija os erros.")
    else:
        initial_data = {}
        if patient_pk:
            initial_data['patient'] = patient_pk
        form = DietForm(initial=initial_data, user=request.user)

    context = {
        "form": form,
        "patient": patient
    }
    return render(request, "diets/diet_create.html", context)


@login_required
def diet_detail(request, pk):
    diet = get_object_or_404(
        Diet, pk=pk, patient__nutritionist=request.user
    )
    context = {"diet": diet}
    return render(request, "diets/detail.html", context)


@login_required
def diet_detail_modal(request, pk):
    diet = get_object_or_404(
        Diet, pk=pk, patient__nutritionist=request.user
    )
    context = {"diet": diet}
    return render(request, "diets/_diet_details_partial.html", context)
