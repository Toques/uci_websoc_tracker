from .forms import AddCourseForm, DeleteCourseForm
from django.template import RequestContext
from .models import Course
from django.views import generic
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .utils import request_websoc, save_course_data, notify
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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
                data = course_form.cleaned_data
                course_code = data['course_code']
                try:
                    newCourse = False
                    course = Course.objects.get(course_code = course_code)
                except(Course.DoesNotExist):
                    course = course_form.save(commit = False)
                    newCourse = True

                kwargs = {'YearTerm': '2016-14'}

                info = request_websoc(course_code, **kwargs)
                save_course_data(course, info)

                userProfileType = ContentType.objects.get(app_label = 'authentication', model = 'userprofile')
                userProfile = userProfileType.get_object_for_this_type(user = request.user)
                course.user.add(userProfile)
                if(newCourse):
                    course_form.save_m2m()
                if (course.course_is_open()):
                    notify(userProfile, msg="Alert: Course: " + course.course_code + " is open!")
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

def refresh(request):
    for course in Course.objects.all():
        kwargs = {'YearTerm': '2016-14'}

        info = request_websoc(course.course_code, **kwargs)
        save_course_data(course, info)
        if (course.course_is_open()):
            userProfileType = ContentType.objects.get(app_label='authentication', model='userprofile')
            for user in course.user.all():
                userProfile = userProfileType.get_object_for_this_type(user=user.user)
                notify(userProfile, msg = "Alert: Course: " + course.course_code + " is open!")
    return HttpResponseRedirect(reverse('courses:index'))