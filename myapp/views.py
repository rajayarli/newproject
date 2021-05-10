from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import Update
from newproject import settings
from myapp.forms import UserReg,UpdateUser,UpdateProfile
from django.contrib.auth.decorators import login_required
# Create your views here.
def first(request):
	return HttpResponse("hello")
def cllg(request):
	return render(request,'myapp/cllg.html')
def about(request):
	return render(request,'myapp/about.html')
def contact(request):
	return render(request,'myapp/contact.html')
def register(request):
	if request.method=="POST":
		data=UserReg(request.POST)
		if data.is_valid():
			data.save()
			return redirect("login")
	else:
		data=UserReg()
	return render(request,'myapp/register.html',{'data':data})

@login_required
def dashboard(request):
	return render(request,'myapp/dashboard.html')

@login_required
def mailsend(request):
	return render(request,'myapp/mailsend.html')

@login_required
def profile(request):
	return render(request,'myapp/profile.html')

@login_required
def update(request):
	if request.method == 'POST':
		c = UpdateUser(request.POST,instance=request.user)
		y = UpdateProfile(request.POST,request.FILES,instance=request.user.update)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			return redirect('profile')
	c = UpdateUser(instance=request.user)
	y = UpdateProfile(instance=request.user.update)
	return render(request,'myapp/update.html',{'c':c,'y':y})