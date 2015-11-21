from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from restaurants.models import Restaurant, Food, Comment
from restaurants.forms import CommentForm
from datetime import datetime
#from django.shortcuts import render_to_response

# Create your views here.

def menu (request):#, idx):
	#food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
	#food2 = {'name': '宮保雞丁', 'price': 90, 'comment': '招牌', 'is_spicy': True}
	#food3 = {'name': '蔥爆牛柳', 'price': 130, 'comment': '家常菜', 'is_spicy': False}
	#items = food3.items()
	#foods = [food1, food2, food3]
	if 'id' in request.GET:
		print(request.GET['id'])
		rs = Restaurant.objects.get(id=request.GET['id'])
		return render(request, 'menu.html', locals())

	## another method to implement this##
	#if idx:
	#	rs = Restaurant.objects.get(id=idx)
	#	return render(request, 'menu.html', locals())
	else:
		return HttpResponseRedirect('/restaurants_list/')

	#path = request.path

def comment(request, idx):
	if idx:
		rs = Restaurant.objects.get(id=idx)
		# get the selected restaurants! by the index of idx!
	else:
		return HttpResponseRedirect('/restaurants_list/')
	if 'ok' in request.POST:	# if sb submit the data.
		fm = CommentForm(request.POST)
		if fm.is_valid():
			user=request.POST['user']
			email = request.POST['email']
			content = request.POST['content']
			Comment.objects.create(content=content, user=user, email=email, date_time=datetime.now(), restaurant=rs)
			# 填寫完畢之後要清除CommentForm
			fm = CommentForm(initial={'content':'我沒意見'})
	else:
		#若沒有填寫，要清空CommentForm
		fm = CommentForm(initial={'content':'我沒意見'})
		# if not user or not content or not email:
		# 	errors.append('請填寫所有空格')
		# if '@' not in email:
		# 	errors.append('請輸入email')
		# if not errors:
		# 	Comment.objects.create(content=content, user=user, email=email, date_time=datetime.now(), restaurant=rs)
		# 	user=''
		# 	email=''
		# 	content=''
	return render(request, 'comment.html', locals())	

# 完成第四章：http://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-database


def list_restaurants(request):
	if not request.user.is_authenticated():	# if the user is not logged in. 
		return HttpResponseRedirect('/accounts/login/?next={0}'.format(request.path))
	restaurants = Restaurant.objects.all()
	request.session['restaurants']=restaurants
	return render(request, 'restaurants_list.html', locals())