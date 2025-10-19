from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from patients.models import Patient  # Importar o modelo Patient

User = get_user_model()


class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword", name="Test User"
        )
        self.client.login(email="test@example.com", password="testpassword")
        # Criar pacientes para o usuário logado
        self.patient1 = Patient.objects.create(user=self.user, name="Paciente Um")
        self.patient2 = Patient.objects.create(user=self.user, name="Paciente Dois")

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertTemplateUsed(response, "dashboard.html")

    def test_dashboard_displays_patients(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertContains(response, self.patient1.name)
        self.assertContains(response, self.patient2.name)
