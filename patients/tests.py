from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient

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
        patient = Patient.objects.create(
            user=self.user,
            name="João da Silva",
            email="joao.silva@example.com",
            birth_date="1990-01-15",
            phone="11999998888",
        )

        # Busca o paciente no banco de dados para verificar se foi salvo
        saved_patient = Patient.objects.get(id=patient.id)

        self.assertEqual(saved_patient.name, "João da Silva")
        self.assertEqual(saved_patient.email, "joao.silva@example.com")
        self.assertEqual(str(saved_patient.birth_date), "1990-01-15")
        self.assertEqual(saved_patient.user, self.user)
        self.assertEqual(str(saved_patient), "João da Silva")

    def test_patient_str_representation(self):
        """
        Testa a representação em string do modelo Patient.
        """
        patient = Patient.objects.create(user=self.user, name="Maria Oliveira")
        self.assertEqual(str(patient), "Maria Oliveira")
