from __future__ import absolute_import

from celery import shared_task

from .models import Course
from django.contrib.contenttypes.models import ContentType
from .utils import request_websoc, save_course_data, notify

@shared_task
def refresh_courses():
    for course in Course.objects.all():
        kwargs = {'YearTerm': '2016-14'}

        info = request_websoc(course.course_code, **kwargs)
        save_course_data(course, info)
        if (course.course_is_open()):
            userProfileType = ContentType.objects.get(app_label='authentication', model='userprofile')
            for user in course.user.all():
                userProfile = userProfileType.get_object_for_this_type(user=user.user)
                notify(userProfile, msg = "Alert: Course: " + course.course_code + " is open!")