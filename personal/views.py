from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import json
from facepy import GraphAPI

mongo="mongodb://localhost/plus1"
#access='EAACEdEose0cBAJWjsNFyuZAM7yocNgriY5DAMsuTcYSyAqT6DCOT3fEAyK8vMuZCN8wZCjXCT2YN3HWqtu4wS8zBLyIUx0cHfhgPBSo86QqME7uc8sEwL2D03UHDmjnk1G2KCz0jKWKHzAv0o7GrNA18ik2ZAGN0EZBUjFuOWPYeOZBPQHDZARzGmGYOAJkZAZC5tanV1WmkqEAZDZD'

def index(request):
	return render(request,'personal/home.html',{"element":"hello"})

def submit(request):
	dbase=pymongo.MongoClient(mongo).plus1
	if 'f1' in request.GET:
		dbase.users.update({"uid":request.GET['ueid']},{'$set': {'choice1':request.GET['f1'] }},upsert= True)
		dbase.common.update( {"game": request.GET['f1']}, {'$push': {'friends': {'$each': [request.GET['ueid']] } } }, upsert=True )
	if 'f2' in request.GET:
		dbase.users.update({"uid":request.GET['ueid']},{'$set': {'choice2':request.GET['f2']}},upsert= True)
		dbase.common.update( {"game": request.GET['f2']}, {'$push': {'friends': {'$each': [request.GET['ueid']] } } }, upsert=True )
	if 'f3' in request.GET:
		dbase.users.update({"uid":request.GET['ueid']},{'$set': {'choice3':request.GET['f3']}},upsert= True)
		dbase.common.update( {"game": request.GET['f3']}, {'$push': {'friends': {'$each': [request.GET['ueid']] } } }, upsert=True )
	return render(request,'personal/basic.html',{'content':"updated"})

def fourth(request):
	return render(request,'personal/qwerty.html')

def work(request):
	dbase=pymongo.MongoClient(mongo).plus1
	#a=dbase.users.find({"uid": request.GET['ueid']})
	a={'choice1':'cricket', 'choice2':'badminton','choice3':'dota'}
	s1=dbase.common.find({"game": a['choice1']})
	s2=dbase.common.find({"game": a['choice2']})
	s3=dbase.common.find({"game": a['choice3']})
	return render(request,'personal/zxcv.html',{'a1':a['choice1'],'s1':s1,'a2':a['choice2'],'s2':s2,'a3':a['choice3'],'s3':s3})

# def check(request):
# 	dbase=pymongo.MongoClient.plus1
# graph = GraphAPI(access)
	# pages = graph.get(request.GET['ueid']+"/friends", page=True)
	# arr=[]
	# for page in pages:
	#     for pag in page['data']:
	#         arr.append(pag)
	# dbase.users.update({"uid":request.GET['ueid']},{'$set': {'friends':arr}},upsert= True)
	