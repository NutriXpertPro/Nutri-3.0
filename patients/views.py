from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.forms import ModelForm, EmailField, CharField
from django import forms
from .models import Patient

User = get_user_model()


class PatientForm(ModelForm):
    # Form customizado pra Patient + User paciente (se novo)
    patient_email = EmailField(label="Email do Paciente", required=True)
    patient_name = CharField(label="Nome do Paciente", max_length=255, required=True)
    patient_password = CharField(
        label="Senha do Paciente", widget=forms.PasswordInput, required=True
    )
    patient_password_confirm = CharField(
        label="Confirme Senha", widget=forms.PasswordInput, required=True
    )

    class Meta:
        model = Patient
        fields = ["birth_date", "phone", "address"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("patient_password")
        password_confirm = cleaned_data.get("patient_password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data


@login_required
def patient_create(request):
    if request.user.user_type != "nutricionista":
        messages.error(
            request, "Acesso negado. Apenas nutricionistas podem cadastrar pacientes."
        )
        return redirect("users:dashboard")

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            try:
                # Cria User paciente se email não existir
                patient_email = form.cleaned_data["patient_email"]
                patient_name = form.cleaned_data["patient_name"]
                patient_password = form.cleaned_data["patient_password"]

                if User.objects.filter(email=patient_email).exists():
                    messages.error(request, "Email do paciente já cadastrado.")
                    return render(request, "patients/create.html", {"form": form})

                # Cria User paciente
                patient_user = User.objects.create_user(
                    username=patient_email,  # Ou gere username único se necessário
                    email=patient_email,
                    password=patient_password,
                    name=patient_name,
                    user_type="paciente",
                    is_active=True,  # Ativo por padrão; ajuste se precisar aprovação
                )

                # Salva Patient com dados do form
                patient = form.save(commit=False)
                patient.patient_user = patient_user
                patient.nutritionist = request.user
                patient.save()

                messages.success(
                    request, f"Paciente {patient_name} cadastrado com sucesso!"
                )
                return redirect("patients:list")  # Ou 'users:dashboard' se preferir
            except Exception as e:
                messages.error(request, f"Erro ao cadastrar: {str(e)}")
        else:
            messages.error(request, "Formulário inválido. Corrija os erros.")
    else:
        form = PatientForm()

    return render(request, "patients/create.html", {"form": form})


# Outras views (ex.: list, detail) — adicione conforme necessário
@login_required
def patient_list(request):
    # Exemplo: lista para redirect
    patients = Patient.objects.filter(nutritionist=request.user)
    return render(request, "patients/list.html", {"patients": patients})
