from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.core.paginator import Paginator  # Importar Paginator


@login_required
def dashboard_view(request):
    patients_list = Patient.objects.filter(user=request.user).order_by(
        "name"
    )  # Adicionar .order_by('name')

    # Lógica de busca
    search_query = request.GET.get("search")
    if search_query:
        patients_list = patients_list.filter(name__icontains=search_query)

    # Lógica de paginação
    paginator = Paginator(patients_list, 5)  # 5 pacientes por página
    page_number = request.GET.get("page")
    patients = paginator.get_page(page_number)

    context = {
        "patients": patients,
        "search_query": search_query,
    }
    return render(request, "dashboard.html", context)
