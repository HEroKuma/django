from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import template
from django.template.loader import get_template

# Create your views here.

def home(request):
	a = request.path
	return render_to_response('index.html',locals())