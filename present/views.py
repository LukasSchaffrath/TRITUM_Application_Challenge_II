from django.shortcuts import render
from .models import data
    
def index(request):
	
	context={
	'data':data.objects.all(),
	}
	return render(request,'data/home.html',context) 
def chart(request):
	context={
	'data':data.objects.all(),
	}

	return render(request,'data/about.html',context) 