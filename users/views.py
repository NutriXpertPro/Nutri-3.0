from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Para mensagens de erro/sucesso
from django.contrib.auth.hashers import make_password  # Para criptografar a senha
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.core.paginator import Paginator  # Importar Paginator
from .models import User  # Importar o modelo User customizado


from django.utils import timezone
from appointments.models import Appointment
from diets.models import Diet


@login_required
def dashboard_view(request):
    # Dados para os cards do dashboard
    total_patients = Patient.objects.filter(nutritionist=request.user).count()
    today = timezone.now().date()
    consultas_hoje = Appointment.objects.filter(
        patient__nutritionist=request.user, date__date=today
    ).count()
    # Lógica para "dietas ativas" - Conta todas as dietas associadas.
    dietas_ativas = Diet.objects.filter(patient__nutritionist=request.user).count()

    # Lógica para "dietas a vencer" - Fixado em 0, pois não há data de validade no modelo.
    dietas_a_vencer = 0

    # Lógica para próxima consulta
    proxima_consulta = (
        Appointment.objects.filter(
            patient__nutritionist=request.user, date__gte=timezone.now()
        )
        .order_by("date")
        .first()
    )

    # Lógica de busca de pacientes (mantida para uso futuro, se necessário)
    search_query = request.GET.get("search")
    patients_list = Patient.objects.filter(nutritionist=request.user).order_by(
        "patient_user__name"
    )
    if search_query:
        patients_list = patients_list.filter(
            patient_user__name__icontains=search_query
        )  # noqa: E501

    paginator = Paginator(patients_list, 5)
    page_number = request.GET.get("page")
    patients = paginator.get_page(page_number)

    context = {
        "total_patients": total_patients,
        "consultas_hoje": consultas_hoje,
        "total_consultas_hoje": 8,  # Valor fixo conforme o design
        "dietas_ativas": dietas_ativas,
        "percentual_dietas_ativas": 93,  # Valor fixo conforme o design
        "dietas_a_vencer": dietas_a_vencer,
        "proxima_consulta": proxima_consulta,
        "patients": patients,
        "search_query": search_query,
    }
    return render(request, "dashboard.html", context)


def nutricionista_login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(
            request, username=email, password=password
        )  # Use 'username=email' se backend custom

        if user is not None:
            if user.user_type == "nutricionista":
                login(request, user)
                return redirect(
                    "users:dashboard"
                )  # Redirecionar para o dashboard do nutricionista
            else:
                messages.error(
                    request, "Você não tem permissão para acessar como nutricionista."
                )
        else:
            messages.error(request, "Email ou senha inválidos.")
    return render(request, "users/nutricionista_login.html")


def nutricionista_register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "users/nutricionista_register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
            return render(request, "users/nutricionista_register.html")

        # Criptografa a senha antes de salvar
        hashed_password = make_password(password)

        User.objects.create(
            name=name,
            email=email,
            password=hashed_password,
            user_type="nutricionista",
            is_active=False,  # Nutricionista precisa de aprovação de pagamento
        )
        messages.success(
            request, "Cadastro realizado com sucesso! Aguarde a aprovação do pagamento."
        )
        return redirect(
            "users:nutricionista_login"
        )  # Redirecionar para a página de login

    return render(request, "users/nutricionista_register.html")


def paciente_login_view(request):
    return render(request, "users/patient_login.html")


def paciente_register_view(request):
    return render(request, "users/patient_register.html")
