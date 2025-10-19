from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient
from django.urls import reverse

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
        self.assertContains(response, "Nenhum paciente encontrado")
