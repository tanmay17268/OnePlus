from django.shortcuts import render
from django.http import HttpResponse
import pymongo
# Create your views here.
mongo="mongodb://localhost/plus1"

def index(request):
	return render(request,'connect/home.html')

def preview(request):
	dbase=pymongo.MongoClient(mongo).plus1
	a=dbase.users.find({"uid": request.GET['ueid2']})
	s1=dbase.common.find({"game": a['choice1']})
	s2=dbase.common.find({"game": a['choice2']})
	s3=dbase.common.find({"game": a['choice3']})
	return render(request,'connect/zxcv.html',{'a1':a['choice1'],'s1':s1,'a2':a['choice2'],'s3':s2,'a3':a['choice3'],'s3':s3})