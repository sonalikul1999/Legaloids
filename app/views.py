from django.shortcuts import render
from django.views.decorators.csrf import *

def about(request):
	return render(request,'about.html',{})
def blog(request):
	return render(request,'blog.html',{})
def casedetails(request):
	return render(request,'case_details.html',{})
def contact(request):
	return render(request,'contact.html',{})
def elements(request):
	return render(request,'elements.html',{})
def index(request):
	return render(request,'index.html',{})
def services(request):
	return render(request,'services.html',{})
def singleblog(request):
	return render(request,'single-blog.html',{})
def study(request):
	return render(request,'study.html',{})
def adminlogin(request):
	return render(request,'adminlogin.html',{})
@csrf_exempt
def adminpannel(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if e=='admin@legaloids.com' and p=='1234':
			return render(request,'adminpannel.html',{})