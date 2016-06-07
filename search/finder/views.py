from django.shortcuts import render
from . import htmlgen


def first_page(request):
	return render(request, 'finder/start.html', {})


def search(request):
    htmlgen.modify_html(request)
    return render(request, 'finder/base.html', {})
                  # , {'info', request.data})

# Create your views here.


