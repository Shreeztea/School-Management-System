from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'age', 'address']


# from students.serializers import StudentSerializer
# from students.models import Student

# student = Student.objects.first()
# serializer = StudentSerializer(student)
# serializer.data

# d = {"name":"Rina","email":"non-valid","age":21,"address":"KTM"}
# serializer = StudentSerializer(data=d)
# serializer.is_valid()
# serializer.errors

# d = {"name":"Rina","email":"rina@test.com","age":21,"address":"KTM"}
# serializer = StudentSerializer(data=d)
# serializer.is_valid()
# serializer.save()