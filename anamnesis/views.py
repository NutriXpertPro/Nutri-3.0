from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def anamnesis_list(request):
    # A lógica para listar as anamneses virá aqui
    return render(request, "anamnesis/list.html")
