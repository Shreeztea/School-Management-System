from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    print(request.user)
    print(request.session.session_key)
    # print('has add student permission',request.user.has_perm("students.add_student"))
    request.session["favorite_course"] = "Python"
    print('permission to add student',request.user.has_perm("students.add_student"))
    return render(request, "accounts/profile.html")
