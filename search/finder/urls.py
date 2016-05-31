 #<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.first_page, name='first_page'),
	url(r'^search/$', views.search, name='search'),	    
]
