from django.db import models


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length= 5)
    max_enrollment = models.PositiveSmallIntegerField()
    current_enrollment = models.PositiveSmallIntegerField()
    wait_list = models.PositiveSmallIntegerField()
    restrictions = models.CharField(max_length = 5)
    status = models.CharField(max_length = 7)
    websoc_url = models.URLField()

    def __str__(self):
        return self.course_code

    def course_is_open(self):
        return (self.status == "OPEN" and self.current_enrollment < self.max_enrollment)

class CourseRequest(models.Model):
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    user = models.ForeignKey('authentication.UserProfile', on_delete = models.CASCADE)
    def __str__(self):
        return self.course_code + " requested by user: " + self.user