from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username = username, password = password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/home/')
	else:
		return render_to_response('login.html', RequestContext(request, locals()))

def index(request):
	return render_to_response('index2.html', RequestContext(request, locals()))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/')
	
	else:
		form =UserCreationForm()
	return render_to_response('register.html',RequestContext(request, locals()))

@login_required
def list_page(request):
	a = 'gginin is here'
	return render_to_response('index.html',RequestContext(request,locals()))