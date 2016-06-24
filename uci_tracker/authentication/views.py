from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.template import RequestContext
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