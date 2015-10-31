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
	food1 = {'name': '�f�X���J', 'price': 60, 'comment': '�n�Y', 'is_spicy': False}
	food2 = {'name': '�c�O���B', 'price': 90, 'comment': '�۵P', 'is_spicy': True}
	food3 = {'name': '���z���h', 'price': 130, 'comment': '�a�`��', 'is_spicy': False}
	items = food3.items()
	foods = [food1, food2, food3]
	return render(request, 'menu.html', locals())



# �����ĥ|���Ghttp://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-database
