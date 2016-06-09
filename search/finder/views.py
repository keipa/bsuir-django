from django.shortcuts import render
from finder import get_results

def first_page(request):
    print("LANDING")
    return render(request, 'finder/start.html', {})


def search(request):
    print("SEARCHING")
    # htmlgen.modify_html(request)
    results = get_results(request.GET["request"])
    return render(request, 'finder/search.html', {"results": results})



# Create your views here.


