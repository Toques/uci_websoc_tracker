from django import forms
from .models import Course

class DetailCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('user',)

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code',)