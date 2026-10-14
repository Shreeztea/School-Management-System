from django.test import TestCase

from students.models import Student
from django.contrib.auth.models import User

from django.urls import reverse

class StudentModelTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name="Ram",
            email="ram@example.com",
            age=20,
            address="Kathmandu",
        )

    def test_student_is_created(self):
        self.assertEqual(
            Student.objects.count(), 1
        )

    def test_student_name(self):
        self.assertEqual(
            self.student.name, "Ram"
        )

    def test_update_student(self):
        self.student.name = "Sita"
        self.student.save()

        self.student.refresh_from_db()

        self.assertEqual(self.student.name, "Sita")

class StudentPageTest(TestCase):

    def test_student_list_page(self):
        response = self.client.get(
            reverse("student_list")
        )

        self.assertEqual(response.status_code, 200)

class AuthenticationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="ram",
            password="StrongPass123!"
        )

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(
            reverse("profile")
        )

        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_access_page(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("profile")
        )

        self.assertEqual(response.status_code, 200)