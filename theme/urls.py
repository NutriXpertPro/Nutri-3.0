from django.urls import path
from .views import landing_page_view

app_name = "theme"

urlpatterns = [
    path("", landing_page_view, name="landing_page"),
]
