from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msd(request):
    return HttpResponse('<h1>msd is the best captain in this era</h1>')
