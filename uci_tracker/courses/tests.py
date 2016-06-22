from django.test import TestCase
from .models import Course
# Create your tests here.
class CourseMethodTests(TestCase):

    def test_course_open(self):
        c = Course(course_code= "12345",
                    max_enrollment=300,
                    current_enrollment=200,
                    wait_list=0,
                    restrictions="",
                    status="OPEN",
                    websoc_url=None)

        self.assertTrue(c.course_is_open())

    def test_course_open_new_only(self):
        c = Course(course_code= "12345",
                   max_enrollment=300,
                   current_enrollment=200,
                   wait_list=0,
                   restrictions="",
                   status="NewOnly",
                   websoc_url=None)
        self.assertFalse(c.course_is_open())

    def test_course_full(self):
        c = Course(course_code="12345",
                   max_enrollment=300,
                   current_enrollment=300,
                   wait_list=0,
                   restrictions="",
                   status="FULL",
                   websoc_url= None)
        self.assertFalse(c.course_is_open())


    def test_course_full_not_maxed_enrolled(self):
        c = Course(course_code="12345",
                   max_enrollment=300,
                   current_enrollment=200,
                   wait_list=0,
                   restrictions="",
                   status="FULL",
                   websoc_url=None)
        self.assertFalse(c.course_is_open())