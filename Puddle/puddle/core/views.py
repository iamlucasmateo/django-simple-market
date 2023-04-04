from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from items.models import Category, Item
from core.forms import SignUpForm, AuthenticationForm


def index(request):
    items = Item.objects.filter(is_sold=True)[0:6]
    categories = Category.objects.all()

    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
            "request": request,
        }
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    
    form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


def _login_response(request, invalid: bool = False):
    return render(
        request,
        "core/login.html",
        {
            "form": AuthenticationForm(),
            "invalid": invalid,
        }
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return _login_response(request, invalid=True)
        else:
            return _login_response(request, invalid=True)
    
    return _login_response(request)


def inbox(request):
    return render(
        request,
        "core/inbox.html",
        {
            "request": request,
        }
    )


def dashboard(request):
    return render(
        request,
        "core/dashboard.html",
        {
            "request": request,
        }
    )

def logout_view(request):
    logout(request)
    return redirect("/")