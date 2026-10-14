from django.contrib.auth.decorators import permission_required
import json
from django.shortcuts import render,redirect
from django.http import JsonResponse
# from django.http import HttpResponse

from students.forms import StudentForm
from .models import AIConversation, Course, Student, Subject
from .ai_service import ask_ai

def ai_chat(request):
    answer = ""
    question = ""
    error = ""

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if question:
            try:
                answer = ask_ai(question)

                AIConversation.objects.create(
                    question=question,
                    answer=answer,
                )
            except Exception as e:
                error = f"Sorry, the AI service is unavailable. {e}"

    conversations = AIConversation.objects.order_by("-created_at")

    return render(
        request,
        "students/ai_chat.html",
        {
            "question": question,
            "answer": answer,
            "error": error,
            "conversations": conversations,
        },
    )

def course_data(request, id):
    course = Course.objects.get(id=id)
    data = {
        "id": course.id,
        "name": course.name,
    }
    return JsonResponse(data)

def course_data_create(request):

    if request.method == "POST":

        data = json.loads(request.body)

        course = Course.objects.create(
            name=data["name"],
        )

        return JsonResponse({
            "message": "Course created",
            "id": course.id
        })

def student_data(request, id):
    student = Student.objects.get(id=id)
    data = {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "age": student.age,
        "address": student.address
    }
    return JsonResponse(data)

def student_data_create(request):

    if request.method == "POST":

        data = json.loads(request.body)

        student = Student.objects.create(
            name=data["name"],
            email=data["email"],
            age=data["age"],
            address=""
        )

        return JsonResponse({
            "message": "Student created",
            "id": student.id
        })

def home(request):
    # return HttpResponse("Hello Django!")
    return render(request, "students/home.html")
# Create your views here.

def about(request):
    # return HttpResponse("Hello Django!")
    return render(request, "students/about.html")

def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        "students/list_student.html", 
        {"students": students}
    )

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )

def course_list(request):
    courses = Course.objects.all()
    return render(request, "students/list_course.html", {"courses": courses})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "students/list_subject.html", {"subjects": subjects})

@permission_required("students.add_student")
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    # courses = Course.objects.all()
    return render(
        request,
        "students/student_create.html",
        {"form": form}
    )
# v1
# def student_create(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         age = request.POST.get("age")
#         address = request.POST.get("address")
#         course_id = request.POST.get("course_id")

#         Student.objects.create(
#             name=name,
#             email=email,
#             age=age,
#             address=address,
#             course_id=course_id
#         )

#         return redirect("student_list")
    
#     courses = Course.objects.all()

#     return render(
#         request,
#         "students/student_create.html",
#         {"courses": courses}
#     )