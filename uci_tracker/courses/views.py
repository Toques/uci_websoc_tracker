from .forms import AddCourseForm, DeleteCourseForm
from django.template import RequestContext
from .models import Course
from django.views import generic
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .utils import request_websoc
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from twilio.rest import TwilioRestClient

# Create your views here.

# def index(request):
#     context = RequestContext(request)
#     print(request.GET)
#     return render(request, 'courses/index.html')


class index(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(user__user = self.request.user)

@login_required()
def add(request):
        context = RequestContext(request)
        if request.method == 'POST':
            course_form = AddCourseForm(data=request.POST)

            if course_form.is_valid():
                try:
                    newCourse = False
                    course = Course.objects.get()
                except(Course.DoesNotExist):
                    course = course_form.save(commit = False)
                    newCourse = True
                data = course_form.cleaned_data
                course_code = data['course_code']
                kwargs = {'YearTerm': '2016-14'}

                info = request_websoc(course_code, **kwargs)

                length = len(info)
                max_enroll = int(info[length - 5 - 1])
                enrolled = int(info[length - 4 - 1])
                waitlist = info[length - 3 - 1]
                restr = info[length - 1 - 1]
                status = info[length -1]

                course.max_enrollment = max_enroll
                course.current_enrollment = enrolled
                course.wait_list = waitlist
                course.restrictions = restr
                course.status = status

                course.save()
                userProfileType = ContentType.objects.get(app_label = 'authentication', model = 'userprofile')
                userProfile = userProfileType.get_object_for_this_type(user = request.user)
                course.user.add(userProfile)
                if(newCourse):
                    course_form.save_m2m()
                return HttpResponseRedirect(reverse('courses:index'))
            else:
                print(course_form.errors)

        else:
            course_form = AddCourseForm()

        return render(request, 'courses/add_course_form.html',
                      {'course_form': course_form}, context)

@login_required()
def delete(request):
    context = RequestContext(request)
    if request.method == 'POST':
        course_form = DeleteCourseForm(data=request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course_code = data['course_code']

            course = Course.objects.get(course_code = course_code)
            userProfileType = ContentType.objects.get(app_label='authentication', model='userprofile')
            userProfile = userProfileType.get_object_for_this_type(user=request.user)

            course.user.remove(userProfile)

            if(course.user.count() == 0):
                course.delete()
            return HttpResponseRedirect(reverse('courses:index'))

    else:
        course_form = DeleteCourseForm()

    return render(request, 'courses/delete_course_form.html',
                  {'course_form': course_form}, context)