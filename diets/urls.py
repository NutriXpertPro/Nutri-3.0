from django.urls import path
from . import views

app_name = "diets"

urlpatterns = [
    path("", views.diet_list, name="list"),
    path("create/", views.diet_create, name="create"),
    path("create/<int:patient_pk>/", views.diet_create, name="create_for_patient"),
    path("<int:pk>/", views.diet_detail, name="detail"),
    path('<int:pk>/details/', views.diet_detail_modal, name='detail_modal'),
]
