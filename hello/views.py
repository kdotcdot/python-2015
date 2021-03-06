import requests
import os
import psycopg2

from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('<pre>' + 'poop' * times + '</pre>')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    
    return render(request, 'db.html', {'greetings': greetings})