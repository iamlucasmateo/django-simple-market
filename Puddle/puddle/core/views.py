from django.shortcuts import render

# Create your views here.
def index(request):
    # path in templates folder
    path = "core/index.html"
    return render(request, "core/index.html")

def contact(request):
    return render(request, "core/contact.html")