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
        # Criar usuários para os pacientes
        self.patient_user1 = User.objects.create_user(
            email="patient1@example.com",
            password="testpassword",
            name="Paciente Alfa",
            user_type="paciente",
        )
        self.patient_user2 = User.objects.create_user(
            email="patient2@example.com",
            password="testpassword",
            name="Paciente Beta",
            user_type="paciente",
        )
        self.patient_user3 = User.objects.create_user(
            email="patient3@example.com",
            password="testpassword",
            name="Outro Paciente",
            user_type="paciente",
        )

        self.patient1 = Patient.objects.create(
            nutritionist=self.user, patient_user=self.patient_user1
        )
        self.patient2 = Patient.objects.create(
            nutritionist=self.user, patient_user=self.patient_user2
        )
        self.patient3 = Patient.objects.create(
            nutritionist=self.user, patient_user=self.patient_user3
        )

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertTemplateUsed(response, "dashboard.html")

    def test_dashboard_pagination(self):
        # Criar mais pacientes para testar a paginação
        for i in range(10):
            patient_user = User.objects.create_user(
                email=f"patient_pag_{i}@example.com",
                password="testpassword",
                name=f"Paciente Paginação {i}",
                user_type="paciente",
            )
            Patient.objects.create(nutritionist=self.user, patient_user=patient_user)

        # Assumindo que a paginação padrão é 10 itens por página
        response = self.client.get(reverse("users:dashboard"), {"page": 2})
        # Verifica se a resposta contém pacientes da segunda página (se houver)
        # Este teste será mais robusto quando a paginação for implementada na view
        self.assertEqual(response.status_code, 200)

    def test_dashboard_new_design_elements(self):
        # Simula um usuário logado com nome "Anderson"
        self.user.name = "Anderson"
        self.user.save()

        response = self.client.get(reverse("users:dashboard"))
        self.assertContains(response, "Bem-vindo, Anderson!")
        self.assertContains(response, "Ações Rápidas")
        self.assertContains(response, "Áreas Principais")

    def test_login_cadastro_urls_resolve(self):
        # Teste para URLs de login
        login_nutricionista_url = reverse("users:nutricionista_login")
        self.assertEqual(login_nutricionista_url, "/users/login/nutricionista/")

        login_paciente_url = reverse("users:login_paciente")
        self.assertEqual(login_paciente_url, "/users/login/paciente/")

        # Teste para URLs de cadastro
        cadastro_nutricionista_url = reverse("users:nutricionista_register")
        self.assertEqual(cadastro_nutricionista_url, "/users/register/nutricionista/")

        cadastro_paciente_url = reverse("users:cadastro_paciente")
        self.assertEqual(cadastro_paciente_url, "/users/register/paciente/")


class NutricionistaLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("users:nutricionista_login")

        # Create an inactive nutricionista user (pending payment)
        self.inactive_nutricionista = User.objects.create_user(
            email="inactive@example.com",
            password="testpassword",
            name="Inactive Nutricionista",
            user_type="nutricionista",
            is_active=False,
        )

        # Create an active nutricionista user
        self.active_nutricionista = User.objects.create_user(
            email="active@example.com",
            password="testpassword",
            name="Active Nutricionista",
            user_type="nutricionista",
            is_active=True,
        )

    def test_inactive_nutricionista_cannot_login(self):
        response = self.client.post(
            self.login_url,
            {"email": "inactive@example.com", "password": "testpassword"},
        )
        self.assertContains(response, "Conta pendente de aprovação de pagamento.")
        self.assertNotContains(
            response, "Bem-vindo"
        )  # Should not redirect to dashboard
        self.assertTemplateUsed(
            response, "users/nutricionista_login.html"
        )  # Should stay on login page

    def test_active_nutricionista_can_login(self):
        response = self.client.post(
            self.login_url, {"email": "active@example.com", "password": "testpassword"}
        )
        self.assertRedirects(
            response, reverse("users:dashboard")
        )  # Should redirect to dashboard
