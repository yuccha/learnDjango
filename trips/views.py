# -*- coding: big5 -*-

from django.shortcuts import render
from datetime import datetime
#from django.shortcuts import render_to_response
# Create your views here.

def im_here (request):
	current_time = datetime.now()
	return render(request, 'im_here.html', locals())

def math (request, a, b):
	add = int(a) + int(b)
	sub = int(a) - int(b)
	mul = int(a)*int(b)
	div = float(a)/float(b)
	#c = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
	#return render_to_response('math.html', c)
	#return render_to_response('math.html', locals())
	return render(request, 'math.html', locals())

def menu (request):
	food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
	food2 = {'name': '宮保雞丁', 'price': 90, 'comment': '招牌', 'is_spicy': True}
	food3 = {'name': '蔥爆牛柳', 'price': 130, 'comment': '家常菜', 'is_spicy': False}
	items = food3.items()
	foods = [food1, food2, food3]
	return render(request, 'menu.html', locals())



# 完成第四章：http://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-database
