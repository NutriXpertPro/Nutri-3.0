from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient
from django.urls import reverse
from django.contrib.messages import get_messages

User = get_user_model()


class PatientModelTest(TestCase):
    def setUp(self):
        # Cria um usuário (nutricionista) para associar aos pacientes
        self.user = User.objects.create_user(
            email="nutri@test.com", password="testpass123", name="Test Nutri"
        )

    def test_create_patient(self):
        """
        Testa a criação de um novo paciente associado a um nutricionista.
        """
        patient_user = User.objects.create_user(
            email="joao.silva@example.com",
            password="testpass123",
            name="João da Silva",
        )
        patient = Patient.objects.create(
            patient_user=patient_user,
            nutritionist=self.user,
            birth_date="1990-01-15",
            phone="11999998888",
        )

        # Busca o paciente no banco de dados para verificar se foi salvo
        saved_patient = Patient.objects.get(id=patient.id)

        self.assertEqual(saved_patient.patient_user.name, "João da Silva")
        self.assertEqual(saved_patient.patient_user.email, "joao.silva@example.com")
        self.assertEqual(str(saved_patient.birth_date), "1990-01-15")
        self.assertEqual(saved_patient.patient_user, patient_user)
        self.assertEqual(saved_patient.nutritionist, self.user)
        self.assertEqual(str(saved_patient), "João da Silva")

    def test_patient_str_representation(self):
        """
        Testa a representação em string do modelo Patient.
        """
        patient_user = User.objects.create_user(
            email="maria.oliveira@example.com",
            password="testpass123",
            name="Maria Oliveira",
        )
        patient = Patient.objects.create(
            patient_user=patient_user,
            nutritionist=self.user,
        )
        self.assertEqual(str(patient), "Maria Oliveira")


class PatientListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="nutri@test.com",
            password="testpass123",
            name="Test Nutri",
            user_type="nutricionista",
        )
        self.client.login(email="nutri@test.com", password="testpass123")

    def test_list_patients_empty(self):
        url = reverse("patients:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum paciente cadastrado ainda.")


class PatientCreateViewTest(TestCase):
    def setUp(self):
        # Cria um nutricionista para os testes
        self.nutritionist = User.objects.create_user(
            email="nutri@test.com",
            password="testpass123",
            name="Nutricionista Teste",
            user_type="nutricionista",
        )
        self.client.login(email="nutri@test.com", password="testpass123")

    def test_nutritionist_can_create_patient(self):
        """
        Testa se um nutricionista logado pode criar um novo paciente com sucesso.
        """
        url = reverse("patients:create")
        data = {
            "patient_name": "Paciente Novo",
            "patient_email": "paciente.novo@example.com",
            "patient_password": "ComplexP@ssw0rd123!",
            "patient_password_confirm": "ComplexP@ssw0rd123!",
            "birth_date": "2000-01-01",
            "phone": "11987654321",
        }
        response = self.client.post(url, data)

        self.assertTrue(User.objects.filter(email="paciente.novo@example.com").exists())
        patient_user = User.objects.get(email="paciente.novo@example.com")
        self.assertEqual(patient_user.user_type, "paciente")

        self.assertTrue(Patient.objects.filter(patient_user=patient_user).exists())
        patient_profile = Patient.objects.get(patient_user=patient_user)
        self.assertEqual(patient_profile.nutritionist, self.nutritionist)

        self.assertRedirects(response, reverse("patients:list"))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Paciente Paciente Novo cadastrado com sucesso!"
        )

    def test_non_nutritionist_cannot_access_create_page(self):
        """
        Testa se um usuário que não é nutricionista é redirecionado.
        """
        # Cria e loga um usuário paciente
        User.objects.create_user(
            email="paciente@test.com",
            password="testpass123",
            name="Paciente Teste",
            user_type="paciente",
        )
        self.client.login(email="paciente@test.com", password="testpass123")

        url = reverse("patients:create")
        response = self.client.get(url)

        # Verifica se foi redirecionado para o dashboard
        self.assertRedirects(response, reverse("users:dashboard"))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Acesso negado. Apenas nutricionistas podem cadastrar pacientes.",
        )

    def test_create_patient_with_existing_email_fails(self):
        """
        Testa a falha ao tentar criar um paciente com um email que já existe.
        """
        # Cria um usuário com o email que será reutilizado
        User.objects.create_user(
            email="paciente.existente@example.com",
            password="password123",
            name="Já Existe",
        )

        url = reverse("patients:create")
        data = {
            "patient_name": "Outro Paciente",
            "patient_email": "paciente.existente@example.com",  # Email duplicado
            "patient_password": "newpassword123",
            "patient_password_confirm": "newpassword123",
        }
        response = self.client.post(url, data)

        # Verifica se a mensagem de erro é exibida e não há redirecionamento
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Email do paciente já cadastrado.")
        # Garante que nenhum novo paciente foi criado
        self.assertEqual(Patient.objects.count(), 0)
