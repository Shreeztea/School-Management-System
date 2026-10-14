from django.db import models

class AIConversation(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]
    
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Student(models.Model): #table name
    name = models.CharField(max_length=100) 
    email = models.EmailField() #column name
    age = models.IntegerField() #column name
    address = models.CharField(max_length=200) #column name
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='students') #foreign key to Course model
    subjects = models.ManyToManyField(Subject)
    document = models.FileField(upload_to="documents/", blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.name}"

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: Profile of {self.student.name}"

# One to Many Relationship: 1 course has multiple students
# Many to One Relationship: Many students belong to 1 course

#One to One
#Many to Many

# Student.objects.create(name='John Doe', email='john.doe@example.com', age=20, address='123 Main St')

# Student.objects.create(name='Sita', email='sita@example.com', age=22, address='456 Oak Ave')


# Course ────────< Student
#   1                Many

# Student >────────< Subject
#  Many               Many

# Student >────────< StudentProfile
#   1                1
 