from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length= 5)
    max_enrollment = models.PositiveSmallIntegerField
    current_enrollment = models.PositiveSmallIntegerField
    wait_list = models.PositiveSmallIntegerField
    restrictions = models.CharField(max_length = 5)
    status = models.CharField(max_length = 4)
    websoc_url = models.URLField

    def __str__(self):
        return self.course_code

    def course_is_open(self):
        return (status == 'OPEN' and current_enrollment < max_enrollment)

