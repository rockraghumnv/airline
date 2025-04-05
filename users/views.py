from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse

# Create your views here.



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login_view'))
    
    return render(request,'users/index.html')

def login_view(request):
    if request.method == "POST":
        username= request.POST['username']
        request.session['username'] += username
        password = request.POST['password']
        print(f"{request.session['username']}")
        print(password)
        
        user = authenticate(request, username=request.session['username'],password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request,'users/login.html',{'message': "invalid Credintials"})
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return render(request,'users/login.html',{'message':'Logged Out'})
