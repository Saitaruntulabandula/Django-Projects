# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Defining a function which
# will receive request and
# perform task depending
# upon function definition

def home(request):
	return render(request,'index.html')

def check(request):
    Username=request.GET['Username']
    Password=request.GET['Password']
    if Username=='root' and Password=='@123':
        status='Login Successful....'
        return render(request,'index.html',{"result":status})
    else:
        status='Unsuccessful Login.... Please Enter Valid Credentials.'
        return render(request,'index.html',{"result":status})
    

