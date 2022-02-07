from django.shortcuts import render

# Create your views here.
from . models import Category, SimFree, SimOnly, SimPlan


def store(request):
    return render(request, "store/store.html")
    