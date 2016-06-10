 #<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.first_page, name='first_page'),
]
