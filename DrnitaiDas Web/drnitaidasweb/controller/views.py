from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.
def home(request):
	aboutMe = Aboutme.objects.all()[0]
	chamber = Chamber.objects.all()
	announcement = Announcement.objects.all()
	youtube = Youtube.objects.all().order_by('-id')
	context = {
		'Aboutme':aboutMe,
		'Chamber':chamber,
		'Announcement':announcement,
		'Youtube':youtube
		}
	return render(request,'index.html',context=context)