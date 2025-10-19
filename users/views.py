from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Para mensagens de erro/sucesso
from django.contrib.auth.hashers import make_password  # Para criptografar a senha
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.core.paginator import Paginator  # Importar Paginator
from .models import User  # Importar o modelo User customizado


@login_required
def dashboard_view(request):
    # Filtro corrigido: usa 'nutritionist' (campo correto em inglês do model)
    patients_list = Patient.objects.filter(nutritionist=request.user).order_by(
        "patient_user__name"  # Ordena pelo nome do usuário paciente
        # (lookup no OneToOneField)
    )

    # Lógica de busca corrigida: usa lookup no patient_user__name
    search_query = request.GET.get("search")
    if search_query:
        patients_list = patients_list.filter(patient_user__name__icontains=search_query)

    # Lógica de paginação
    paginator = Paginator(patients_list, 5)  # 5 pacientes por página
    page_number = request.GET.get("page")
    patients = paginator.get_page(page_number)

    context = {
        "patients": patients,
        "search_query": search_query,
    }
    return render(request, "dashboard.html", context)  # Template no root templates/


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
