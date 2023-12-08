from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    return render(request, "hello.html", {"names": ["hello",2,3, 4]})

def say_playgroundpage(request):
    return render(request, "hello.html", {"names": ["playground",2,3, 4]})