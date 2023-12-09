from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def say_hello(request):
        return HttpResponseRedirect('/home/')
