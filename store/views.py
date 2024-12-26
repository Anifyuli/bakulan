from django.shortcuts import redirect, render
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(
        request, "pages/home.html", {"products": products, "categories": categories}
    )


def about(request):
    return render(request, "pages/about.html", {})


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Your login is successfully."))
            return redirect("home")
        else:
            messages.success(request, ("Your login is failed."))
            return redirect("login")
    else:
        return render(request, "pages/login.html", {})


def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect("home")


def registerUser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # Login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account registration is successfully.")
            return redirect("home")
        else:
            messages.success(
                request, "Sorry, your registration is failed. Please try again."
            )
            return redirect("register")
    else:
        return render(request, "pages/register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "pages/product.html", {"product": product})

def category(request, category):
    categories = Category.objects.all()
    category = category.replace("-", " ")

    print(f"Searching for category: {category}")  # Debug print

    try:
        category_obj = Category.objects.get(name=category)
        print(f"Found category: {category_obj}")  # Debug print

        products = Product.objects.filter(category=category_obj)
        print(f"Found products: {products.count()}")  # Debug print

        return render(
            request,
            "pages/category.html",
            {
                "products": products,
                "category": category_obj,
                "categories": categories,
            },
        )
    except Category.DoesNotExist:  # Be more specific with exception
        messages.error(request, "Selected category doesn't exist.")  # Changed to error
        return redirect("home")
