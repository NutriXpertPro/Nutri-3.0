from django.urls import path
from . import views

app_name = "evaluations"

urlpatterns = [
    path("", views.evaluation_list, name="list"),
]
