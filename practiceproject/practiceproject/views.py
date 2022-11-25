# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.shortcuts import render
# Defining a function which
# will receive request and
# perform task depending
# upon function definition
#def hello_geeks (request) :
	# This will return Hello Geeks
	# string as HttpResponse
	#return HttpResponse("<h1>Hello Team BridgeLabz<h1>")

def home(request):
	return render(request,'index.html')

def add(request):
	value=int(request.GET["value"])
	lst=[1,2,3,4,5,6,7,8,9,10]
	for i in range(len(lst)):
		lst[i]=lst[i]*value
	return render(request,'result.html',{"result":lst})