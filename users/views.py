from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import redirect
from .forms import Login_form, Register_form
from django.contrib.auth.models import User
from django.db import transaction

# Create your views here.

def login_redirect(request):  
    if request.user.is_authenticated:
        return redirect("flights:book")  
    return redirect("users:login_view")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            flight_id = request.session.get("flight")  # Retrieve flight_id from session
            login(request, user)
            if flight_id is None:
                return redirect("profile:profile_view")
            return HttpResponseRedirect(reverse('flights:book'))
        else:
            return render(request, 'users/login.html', {'message': "Invalid credentials", 'Login_form': Login_form()})
    return render(request, 'users/login.html', {'Login_form': Login_form()})

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'message': 'Logged Out', 'Login_form': Login_form()})

@transaction.atomic
def register_view(request):
    if request.method == "POST":
        print("POST")
        print(request.POST)
        form = Register_form(request.POST)

        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            password = form.cleaned_data["password"]
            password_again = form.cleaned_data["password_again"]

            if password != password_again:
                return render(request, "users/register.html", {"message": "Passwords do not match", "Register_form": Register_form()})

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user_check = User.objects.filter(username=username)

            if user_check.exists():
                return render(request, "users/register.html", {"message": "User Already Exists", "Register_form": Register_form()})

            user = User.objects.create_user(username=username, password=password, email=email)
            print("User created")
            login(request, user)
            print("User logged in")
            flight_id = request.session.get("flight")  # Retrieve flight_id from session
            print("Flight ID:", flight_id)
            if flight_id is None:
                return redirect("profile:profile_view")
            print("Redirecting to book")
            return HttpResponseRedirect(reverse('flights:book'))
        print("Form is not valid")
        print(form.errors)
        return render(request, "users/register.html", {"Register_form": Register_form(), "message": "Invalid form"})

    return render(request, "users/register.html", {"Register_form": Register_form()})