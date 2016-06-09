from django.shortcuts import render
from . import htmlgen


def first_page(request):
    print("LANDING")
    return render(request, 'finder/start.html', {})


def search(request):
    print("SEARCHING")
    # htmlgen.modify_html(request)
    return render(request, 'finder/base.html', {})



# Create your views here.


