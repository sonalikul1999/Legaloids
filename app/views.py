from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *

def about(request):
	return render(request,'about.html',{})
def blog(request):
	page = request.GET.get('page')
	d={}
	l=[]
	obj=BlogData.objects.all()
	for x in obj:
		d={
			'Blog_Title':x.Blog_Title,
			'Blog_Date':x.Blog_Date,
			'Blog_Image':x.Blog_Image,
			'Blog_Body':x.Blog_Body
		}
		l.append(d)
	paginator = Paginator(list(reversed(l)), 5)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	dic={'data':data}
	d={}
	lt=[]
	count=0
	obj=BlogData.objects.all()
	for x in obj:
		if count<6:
			d={
			'title':x.Blog_Title,
			'date':x.Blog_Date,
			'image':x.Blog_Image.url
			}
			lt.append(d)
			count=count+1
		else:
			break
	dic.update({'rdata':reversed(lt)})
	return render(request,'blog.html',dic)
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
			request.session['admin_id'] = e
			return render(request,'adminpannel.html',{})
		else:
			return redirect('/error/')
def error(request):
	return render(request,'error.html',{})
@csrf_exempt
def postblog(request):
	try:
		if request.session['admin_id']=="admin@legaloids.com":
			return render(request,'postblog.html',{})
		else:
			return redirect('/error/')
	except:
		return redirect('/error/')
def allblogs(request):
	try:
		if request.session['admin_id']=="admin@legaloids.com":
			return render(request,'allblogs.html',{'data':BlogData.objects.all()})
		else:
			return redirect('/error/')
	except:
		return redirect('/error/')
@csrf_exempt
def saveblog(request):
	if request.method=="POST":
		title=request.POST.get('title')
		body=request.POST.get('body')
		category=request.POST.get('category')
		image=request.FILES['image']
		p="B00"
		x=1
		pid=p+str(x)
		while BlogData.objects.filter(Blog_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		obj=BlogData(
				Blog_ID=pid,
				Blog_Title=title,
				Blog_Category=category,
				Blog_Body=body,
				Blog_Image=image
			)
		obj.save()
		return render(request,'postblog.html',{'msg':'Blog Posted Successfully'})
	else:
		return redirect('/error/')