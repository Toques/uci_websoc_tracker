from django.db import models
from django.core.urlresolvers import reverse
from .utils import request_websoc, save_course_data

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length= 5)
    max_enrollment = models.PositiveSmallIntegerField()
    current_enrollment = models.PositiveSmallIntegerField()
    wait_list = models.PositiveSmallIntegerField()
    restrictions = models.CharField(max_length = 5)
    status = models.CharField(max_length = 7)
    user = models.ManyToManyField('authentication.UserProfile')

    def __str__(self):
        return self.course_code

    def course_is_open(self):
        return (self.status == "OPEN" and self.current_enrollment < self.max_enrollment)

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})
