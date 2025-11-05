from django.forms import ModelForm, EmailField, CharField
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import PatientProfile

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
        model = PatientProfile
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
                    email=patient_email,
                    password=patient_password,
                    name=patient_name,
                    user_type="paciente",
                    is_active=True,
                )

                # Salva Patient com dados do form
                patient = form.save(commit=False)
                patient.user = patient_user
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


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Outras views (ex.: list, detail) — adicione conforme necessário
@login_required
def patient_list(request):
    patients_list = PatientProfile.objects.filter(nutritionist=request.user)

    # Search
    search_query = request.GET.get('q')
    if search_query:
        patients_list = patients_list.filter(user__name__icontains=search_query)

    # Sort
    sort_by = request.GET.get('sort', '-created_at') # Default sort by most recent
    if sort_by not in ['user__name', '-user__name', 'created_at', '-created_at']:
        sort_by = '-created_at' # Fallback to default if invalid sort is provided
    patients_list = patients_list.order_by(sort_by)

    # Pagination
    paginator = Paginator(patients_list, 20) # Show 20 patients per page
    page_number = request.GET.get('page')
    try:
        patients = paginator.page(page_number)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)

    context = {
        'patients': patients,
        'search_query': search_query or '',
        'sort_by': sort_by,
    }
    return render(request, "patients/list.html", context)


@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(
        PatientProfile, pk=patient_id, nutritionist=request.user
    )
    context = {"patient": patient}
    return render(request, "patients/detail.html", context)
