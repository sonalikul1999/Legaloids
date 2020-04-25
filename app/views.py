from django.shortcuts import render

# Create your views here.
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