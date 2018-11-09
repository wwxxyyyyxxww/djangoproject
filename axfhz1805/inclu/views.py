from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel


def home(request):
    a=Wheel.objects.all()
    data={
        "a":a
    }
    return render(request,"test.html",context=data)








