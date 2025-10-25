from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/nutricionista/",
        views.nutricionista_login_view,
        name="nutricionista_login",
    ),
    path(
        "register/nutricionista/",
        views.nutricionista_register_view,
        name="nutricionista_register",
    ),
    path("login/paciente/", views.paciente_login_view, name="login_paciente"),
    path(
        "register/paciente/",
        views.paciente_register_view,
        name="cadastro_paciente",
    ),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("resources/", views.resources_view, name="resources"),
    path("settings/", views.settings_view, name="settings"),
]
