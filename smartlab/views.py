from django.shortcuts import render

from django.http import HttpResponse
import pandas
import os.path
# BASE = os.path.dirname(os.path.abspath(__file__))

import pymongo
from pymongo import MongoClient



# Create your views here.



# with open(os.path.join(BASE, 'data.csv')) as f:
# 	data = pandas.read_csv(f)
# 	sum = 0 
# 	for i in data:
# 		sum = int(float(i)) + sum

def index(request):
	# response = HttpResponse()
	# response.writelines('<h1>Smart Lab </h1>')
	# response.write("Total member (in desk): %d" % sum)
	# with open(os.path.join(BASE, 'data.csv')) as f:
	# 	data = pandas.read_csv(f)
	# 	data = [int(float(i)) for i in data]
	# 	people_in_room = data.pop()
	# 	people_in_desk = 0 
	# 	for i in data:
	# 		people_in_desk = i + people_in_desk
	# 	total_desk = 15
	# 	desk_available = total_desk - people_in_desk
	# return render(request, 'pages/home.html', {'people_in_room': people_in_room,
	# 	'people_in_desk':people_in_desk, 'desk_available':desk_available, 'people_in_room': people_in_room, 'total_desk':total_desk})
	cluster = MongoClient('mongodb+srv://huu:abc123abc@cluster0.ft8ih.mongodb.net/<dbname>?retryWrites=true&w=majority')
	db = cluster['room']
	collection = db['totalPeople']

	result = collection.find({})
	dict_result = list(result)
	return render(request, 'pages/home.html', dict_result[0])
def notification(request):
	return render(request, 'pages/notification.html')

def blog(request):
	return render(request, 'pages/blog.html')

def stastics(request):
    cluster = MongoClient('mongodb+srv://huu:abc123abc@cluster0.ft8ih.mongodb.net/<dbname>?retryWrites=true&w=majority')
    db = cluster['room']
    collection = db['log']
    dic = collection.find({})
    a = list(dic)
    b = sorted(a, key=lambda k: k['_id'], reverse=True)
    items = [b[i] for i in range(10)]
    return render(request, 'pages/stastics.html',{"0":items[0], "1": items[1], "2": items[2], "3": items[3], "4": items[4], "5": items[5], "6": items[6], "7": items[7], "8": items[8], "9": items[9]})




	
