from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword", name="Test User"
        )
        self.client.login(email="test@example.com", password="testpassword")

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        response = self.client.get(reverse("users:dashboard"))
        self.assertTemplateUsed(response, "dashboard.html")
