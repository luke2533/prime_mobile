from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from . models import Category, SimFree

=======
>>>>>>> dev

def store(request):
    return render(request, "store/store.html")
    