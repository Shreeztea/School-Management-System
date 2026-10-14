import pytest
from students.models import Course


@pytest.mark.django_db
def test_create_course():
    course = Course.objects.create(
        name="Django"
    )

    assert course.name == "Django"
    assert Course.objects.count() == 1