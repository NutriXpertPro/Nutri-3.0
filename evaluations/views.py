from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

from .forms import EvaluationForm
from .models import Evaluation, EvaluationPhoto
from patients.models import PatientProfile


@login_required
def evaluation_list(request):
    # Placeholder for listing evaluations
    return render(request, "evaluations/evaluation_list.html")


@login_required
def evaluation_create(request, patient_pk):
    patient = get_object_or_404(PatientProfile, pk=patient_pk, nutritionist=request.user)
    if request.method == "POST":
        form = EvaluationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.patient = patient
            evaluation.save()

            # Handle photo uploads
            photos_to_create = []
            if 'photo_front' in request.FILES:
                photos_to_create.append(
                    EvaluationPhoto(evaluation=evaluation, image=request.FILES['photo_front'], label='FRENTE')
                )
            if 'photo_side' in request.FILES:
                photos_to_create.append(
                    EvaluationPhoto(evaluation=evaluation, image=request.FILES['photo_side'], label='LADO')
                )
            if 'photo_back' in request.FILES:
                photos_to_create.append(
                    EvaluationPhoto(evaluation=evaluation, image=request.FILES['photo_back'], label='COSTAS')
                )
            
            if photos_to_create:
                EvaluationPhoto.objects.bulk_create(photos_to_create)

            messages.success(request, "Nova avaliação salva com sucesso!")
            return redirect('patients:detail', pk=patient.pk)
        else:
            messages.error(request, "Formulário inválido. Corrija os erros.")
    else:
        form = EvaluationForm(user=request.user, initial={'patient': patient.pk})
        form.fields['patient'].widget = forms.HiddenInput()

    context = {
        'form': form,
        'patient': patient
    }
    return render(request, 'evaluations/create.html', context)


@login_required
def evaluation_detail_modal(request, pk):
    evaluation = get_object_or_404(
        Evaluation.objects.prefetch_related('photos'), 
        pk=pk, 
        patient__nutritionist=request.user
    )
    context = {"evaluation": evaluation}
    return render(request, "evaluations/_evaluation_details_partial.html", context)