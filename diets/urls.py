from django.urls import path
from . import views

app_name = "diets"

urlpatterns = [
    path("", views.plano_alimentar, name="plano_alimentar"),  # Nova página principal
    path("list/", views.diet_list, name="list"),  # Movido para /list/
    path("create/", views.diet_create, name="create"),
    path("create/<int:patient_pk>/", views.diet_create, name="create_for_patient"),
    path("<int:pk>/", views.diet_detail, name="detail"),
    path("<int:pk>/details/", views.diet_detail_modal, name="detail_modal"),
    
    # AJAX Endpoints
    path("buscar-alimentos/", views.buscar_alimentos, name="buscar_alimentos"),
    path("calcular-necessidades/", views.calcular_necessidades, name="calcular_necessidades"),
    path("gerar-cardapio-ia/", views.gerar_cardapio_ia, name="gerar_cardapio_ia"),
    path("gerar-substituicoes/", views.gerar_substituicoes, name="gerar_substituicoes"),
    
    # PDF Generation
    path("pdf/<int:patient_id>/", views.gerar_pdf, name="gerar_pdf"),
]
