from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("Это капец")

def home(request):
    return render(request,"home.html",{'greeting':"hello"})