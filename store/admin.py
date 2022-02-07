from django.contrib import admin
from .models import Category, SimFree, SimOnly, SimPlan

# Register your models here.
admin.site.register(Category)
admin.site.register(SimFree)
admin.site.register(SimOnly)
admin.site.register(SimPlan)