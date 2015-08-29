import requests
import os
import psycopg2

from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from .models import Question
from .models import Choice

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print "poop"
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    
    return render(request, 'db.html', {'greetings': greetings})