from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.core.paginator import Paginator
from .models import User
from django.utils import timezone
from appointments.models import Appointment
from diets.models import Diet
import json
from evaluations.models import Evaluation

@login_required
def dashboard_view(request):
    total_patients = Patient.objects.filter(nutritionist=request.user).count()
    today = timezone.now().date()
    appointments_today = Appointment.objects.filter(
        patient__nutritionist=request.user, date__date=today
    ).order_by("date")
    consultas_hoje = appointments_today.count()
    dietas_ativas = Diet.objects.filter(patient__nutritionist=request.user).count()
    dietas_a_vencer = 0
    proxima_consulta = (
        Appointment.objects.filter(
            patient__nutritionist=request.user, date__gte=timezone.now()
        )
        .order_by("date")
        .first()
    )
    search_query = request.GET.get("search")
    patients_list = Patient.objects.filter(nutritionist=request.user).order_by(
        "patient_user__name"
    )
    if search_query:
        patients_list = patients_list.filter(
            patient_user__name__icontains=search_query
        )
    paginator = Paginator(patients_list, 5)
    page_number = request.GET.get("page")
    patients = paginator.get_page(page_number)
    chart_labels = []
    chart_data = []
    chart_patient_name = ""
    first_name = request.user.name.split()[0]

    # Encontra a avaliação mais recente para selecionar um paciente
    latest_evaluation = (
        Evaluation.objects.filter(patient__nutritionist=request.user)
        .order_by("-date")
        .first()
    )
    # Logic for Patient in Focus
    patient_in_focus = Patient.objects.filter(nutritionist=request.user).order_by('-created_at').first()
    if patient_in_focus:
        # Add placeholder goal and progress metric for demonstration
        patient_in_focus.goal = "Perda de Peso" # Placeholder
        patient_in_focus.progress_metric = "-5kg desde o início" # Placeholder
    
    context = {
        "total_patients": total_patients,
        "consultas_hoje": consultas_hoje,
        "appointments_today": appointments_today,
        "total_consultas_hoje": 8,
        "dietas_ativas": dietas_ativas,
        "percentual_dietas_ativas": 93,
        "dietas_a_vencer": dietas_a_vencer,
        "proxima_consulta": proxima_consulta,
        "patients": patients,
        "search_query": search_query,
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data),
        "chart_patient_name": chart_patient_name,
        "first_name": first_name,
        "patient_in_focus": patient_in_focus, # Add patient in focus to context
    }
    return render(request, "dashboard.html", context)

def nutricionista_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if hasattr(user, "user_type") and user.user_type == "nutricionista":
                if user.check_password(password):
                    if user.is_active:
                        login(request, user)
                        return redirect("users:dashboard")
                    else:
                        messages.error(
                            request, "Conta pendente de aprovação de pagamento."
                        )
                else:
                    messages.error(request, "Email ou senha inválidos.")
            else:
                messages.error(request, "Email ou senha inválidos.")
        except User.DoesNotExist:
            messages.error(request, "Email ou senha inválidos.")
    return render(request, "users/nutricionista_login.html")

def nutricionista_register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        professional_title = request.POST.get("professional_title")
        gender = request.POST.get("gender")
        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "users/nutricionista_register.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
            return render(request, "users/nutricionista_register.html")
        hashed_password = make_password(password)
        User.objects.create(
            name=name,
            email=email,
            password=hashed_password,
            user_type="nutricionista",
            professional_title=professional_title,
            gender=gender,
            is_active=False,
        )
        messages.success(
            request,
            ("Cadastro realizado com sucesso! " "Aguarde a aprovação do pagamento."),
        )
        return redirect(
            "users:nutricionista_login"
        )
    return render(request, "users/nutricionista_register.html")

def paciente_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if hasattr(user, "user_type") and user.user_type == "paciente":
                if user.check_password(password):
                    if user.is_active:
                        login(request, user)
                        return redirect("users:patient_dashboard")
                    else:
                        messages.error(request, "Sua conta de paciente está inativa.")
                else:
                    messages.error(request, "Email ou senha inválidos.")
            else:
                messages.error(request, "Email ou senha inválidos.")
        except User.DoesNotExist:
            messages.error(request, "Email ou senha inválidos.")
    return render(request, "users/patient_login.html")

def paciente_register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "users/patient_register.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
            return render(request, "users/patient_register.html")
        hashed_password = make_password(password)
        User.objects.create(
            name=name,
            email=email,
            password=hashed_password,
            user_type="paciente",
            is_active=True,
        )
        messages.success(
            request,
            "Cadastro de paciente realizado com sucesso! Faça login para continuar.",
        )
        return redirect("users:login_paciente")
    return render(request, "users/patient_register.html")

@login_required
def resources_view(request):
    return render(request, "users/resources.html")

@login_required
def settings_view(request):
    return render(request, "users/settings.html")

@login_required
def patient_dashboard_view(request):
    first_name = request.user.name.split()[0]
    context = {
        'message': 'Bem-vindo ao seu dashboard de paciente!',
        'first_name': first_name,
    }
    return render(request, "users/patient_dashboard.html", context)

def logout_view(request):
    logout(request)
    return redirect("theme:home")
