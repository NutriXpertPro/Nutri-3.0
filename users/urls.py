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
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
