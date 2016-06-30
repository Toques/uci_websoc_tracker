from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'courses'
urlpatterns = [
    url(r'^$', login_required(views.index.as_view()), name = 'index'),
    url(r'^add$', views.add, name = 'add'),

]