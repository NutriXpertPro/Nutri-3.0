from django.urls import path
from . import views

app_name = 'anamnesis'

urlpatterns = [
    path('', views.anamnesis_list, name='list'),
]
