from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html')

def loggedin(request):
	return render(request,'loggedin.html')

def signup(request):
	return render(request,'signup.html')

def registered(request):
	return render(request,'registered.html')