from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer, Categories

# Create your views here.
def index(request):
      if not request.user.is_authenticated:
          return render(request, "login.html", {"message": None})
      context = {
          "user": request.user
      }
      return render(request, "index.html", context)

def register(request):
    user = request.POST["user"]
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]
    customer_list = Customer.objects.all()
    for customer in customer_list:
        if customer==user:
            return render(request, "register.html", {"message": "This username is already taken. Please choose another one."})
    user = Customer(username=user, password=password, first_name=name, email=email)
    user.save()
    return render(request, "user.html", {"name": name})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("user"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def user(request):
    return render(request, "user.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def order(request):
    categories = Categories.objects.all()
    return render(request, "orders.html", {"categories":categories})