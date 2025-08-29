from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

#  Signup View

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # log in after signup
            return redirect("core:home")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


#  Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)            # log in user
            return redirect("core:home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

#  Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect("core:home")
