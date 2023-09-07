from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("Это капец")

def home(request):
    return render(request,"home.html",{'greeting':"hello"})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text [::-1]
    words = user_text.split()
    num_words = len(words)
    return render(request,"reverse.html",{'user_text':user_text,'reversed_text':reversed_text,'num_words':num_words})