import email
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from .models import Greetings

def index(request):
    return render(request, 'greetings/index.html', {'title': 'Greetings'})

def submit(request):
    request_data = request.POST
    request_email = request_data['email']
    
    if Greetings.objects.filter(email=request_email).exists():
        return render(request, 'greetings/show_greet.html', {'title': 'Greetings', 'text': f'We have already greeted!'})
    else:
        Greetings.objects.create(email=request_email)
        return render(request, 'greetings/show_greet.html', {'title': 'Greetings', 'text': f'Hello {request_email}!'})

def show_greetings(request):
    greetings = Greetings.objects.all()
    return render(request, 'greetings/show_greet_list.html', {'text':'Greeting list' , "greetings": greetings})
