from datetime import date, datetime
# import email
from unicodedata import name
from django.shortcuts import render, HttpResponse
from django.contrib import messages

from bookersapp.models import Contacts
from tkinter import *
def index(request):
    return render(request,'index.html')
def Contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        Contacts = Contacts(name=name, email=email, phone=phone, date= datetime.today())
        Contacts.save()
        messages.success(request, 'Your massage has been send.')
    return render(request, "Contacts.html")
    # return HttpResponse("HII this is contact page ")
    