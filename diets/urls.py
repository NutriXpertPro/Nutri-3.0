from django.urls import path
from . import views

app_name = "diets"

urlpatterns = [
    path("", views.diet_list, name="list"),
    path("create/", views.diet_create, name="create"),
]
