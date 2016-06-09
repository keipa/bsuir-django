 #<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^search/(?P<r>[0-9]+)/$', views.search, name='search'),
    url(r'^$', views.first_page, name='first_page'),
]
