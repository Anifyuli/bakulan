from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "pages/home.html", {"products": products})


def about(request):
    return render(request, "pages/about.html", {})


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Your login is successfully"))
            return redirect("home")
        else:
            messages.success(request, ("Your login is failed"))
            return redirect("login")
    else:
        return render(request, "pages/login.html", {})

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect("home")

def registerUser(request):
    return render(request, "pages/register.html", {})