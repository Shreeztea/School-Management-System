from django.test import TestCase

from students.models import Student


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