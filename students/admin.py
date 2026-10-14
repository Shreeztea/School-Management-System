from django.contrib import admin
from .models import Student,StudentProfile,Course,Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Subject)
