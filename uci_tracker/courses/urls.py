from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^$', views.index.as_view(), name = 'index'),
    url(r'^add$', views.add, name = 'add'),
]