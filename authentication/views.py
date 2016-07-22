from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
def register(request):
    registered = False
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'authentication/register.html',
                              {'user_form': user_form,
                               'profile_form':profile_form,
                               'registered': registered},context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                if request.POST.get('next') != '':
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect(reverse('courses:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'authentication/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))