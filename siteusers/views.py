from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from siteusers.forms import RegistrationForm, LoginForm
from siteusers.models import SiteUser
from django.contrib.auth import authenticate, login, logout

def SiteUserRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], 
				password = form.cleaned_data['password'])
			user.save()
			#siteuser = user.get_profile()
			#siteuser.name = form.cleaned_data['name']
			#siteuser.birthday = form.cleaned_data['birthday']
			#siteuser.save()
			siteuser = SiteUser(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
			siteuser.save()
			return HttpResponseRedirect('/profile/')
		else:
			return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
	else: 
		'''user is not submitting form, show them a blank registration form '''
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			siteuser = authenticate(username=username, password=password)
			if drinker is not None:
				login(request, siteuser)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

	else:
		'''user is not submitting the form, show the login form '''
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')