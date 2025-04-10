from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.shortcuts import redirect
from .forms import Login_form,Register_form
from django.contrib.auth.models import User
# Create your views here.

def login_redirect(request,flight_id):
     request.session["flight_id"] = flight_id
     if request.user.is_authenticated:
          return redirect("flights:book_flight",flight_id=flight_id)
     return redirect("users:login_view")


def login_view(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        if user:
            flight_id = request.session.get("flight_id")
            login(request,user)
            if flight_id is None:
                return redirect("profiles:profile_view")
            return HttpResponseRedirect(reverse('flights:book_flight',args=[flight_id]))
        else:
            return render(request,'uers/login.html',{'message': "invalid Credintials"})
    return render(request,'users/login.html',{'Login_form':Login_form})

def logout_view(request):
    logout(request)
    return render(request,'users:login_view',{'message':'Logged Out','Login_form':Login_form})

def register_view(request):
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            password_again = form.cleaned_data["password_again"]
            if password != password_again:
                return redirect("users:login_view",{"message":"Passwords do not match"})
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user_check = User.objects.filter(username = username)
            if user_check:
                return redirect("users:login_view",{"message":"User Alredy Exist"})
            user = User.objects.create(username=username,password=password,email=email)
            login(request,user)
            flight_id = request.session.get("flight_id")
            if flight_id is None:
                return redirect("profiles:profile_view")
            return HttpResponseRedirect(reverse('flights:book_flight',args=[flight_id]))
        return render(request,"users/register.html",{"Register_form":Register_form})