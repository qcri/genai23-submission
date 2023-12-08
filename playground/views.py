from django.shortcuts import render
from django.http import HttpResponse
from .forms import testingform


# Create your views here.
def say_hello(request):
    form = testingform()
    return render(request, "testingforms.html", {"names": ["hello",2,3, 4], 'form':form})

def say_playgroundpage(request):
    return render(request, "hello.html", {"names": ["playground",2,3, 4], 'form':''})