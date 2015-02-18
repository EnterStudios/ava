from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

#Import a user registration form
from apps.ava_core_auth.forms import UserRegisterForm, UserLoginForm

# User Login View
def user_login(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            #This authenticates the user
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    #This logs him in
                    login(request, user)
                else:
                    return HttpResponse("Not active")
            else:
                return HttpResponse("Wrong username/password")
        else:   
            form = UserLoginForm()
            context = {}
            context.update(csrf(request))
            context['form'] = form
            #Pass the context to a template
            return render_to_response('auth/login.html', context)
    return HttpResponseRedirect("/")

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse('User created succcessfully.')
        else:
            form = UserRegisterForm()
        
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('auth/register.html', context)
    else:
        return HttpResponseRedirect('/')
