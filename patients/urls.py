from django.urls import path
from . import views  # Assumindo views.py com create_view; ajuste imports se necessário

app_name = (
    "patients"  # Fix: Declara app_name pra suportar namespace no include principal
)

urlpatterns = [
    path("", views.patient_list, name="list"),  # Exemplo: lista de pacientes
    path(
        "create/", views.patient_create, name="create"
    ),  # Rota pro cadastro (link no template)
    path("<int:patient_id>/", views.patient_detail, name="detail"),
    # Adicione outras rotas conforme seu app (ex.: update, delete)
]
