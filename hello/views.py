import requests
import os
import psycopg2
import urlparse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

stock = {
	"banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
}
	
prices = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

#Write your code below!
def compute_bill(food):
	total = 0
	for item in food:
		if stock[item] > 0:
			total = total + prices[item]
			stock[item] -= 1
	return total
	
food_order = ["apple", "orange"]

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    #print r.text
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

