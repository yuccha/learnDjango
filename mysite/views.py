from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib import auth
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


def meta (request):
	values = request.META.items()
	#values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
	if 'usr_name' in request.GET:
		return HttpResponse('Welocom~'+request.GET['usr_name'])
	else:
		return render (request, 'welcome.html', locals())

def set_ck(request):
	response = HttpResponse('Set your lucknum to 8')
	response.set_cookie('lucky_number', 8)
	return response

def get_ck(request):
	if 'lucky_number' in request.COOKIES:
		return HttpResponse('Your lucky number is {0}'.format(request.COOKIES['lucky_number']))
	else:
		return HttpResponse('No Cookies!!')

def use_session(request):
	# request.session['lucky_number']=8	# generate session

	# if 'lucky_number' in request.session:
	# 	lucky_number = request.session['lucky_number']
	# 	response = HttpResponse('Your lucky number is '+str(lucky_number))

	# del request.session['lucky_number']	# kill session lucky_num
	# return response
	sid = request.COOKIES['sessionid']
	sid2 = request.session.session_key
	s = Session.objects.get(pk=sid)
	sinfo = "Session ID1: "+sid+"<br>Session ID2: "+sid2+"<br>Expired Date: "+str(s.expire_date)+"<br>Data: "+str(s.get_decoded())
	return HttpResponse(sinfo)

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/index/')
	else:
		return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')


def index(request):
	return render(request, 'index.html', locals())






