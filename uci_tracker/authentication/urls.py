from django.conf.urls import url
from . import views

app_name = 'authentication'
urlpatterns = [
    url(r'^$', views.register, name = 'register'),
]