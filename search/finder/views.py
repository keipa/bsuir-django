from django.shortcuts import render
from finder import get_results
from indexer.indexing import process_one_link

def first_page(request):
    return render(request, 'finder/start.html', {})


def search(request):
    results = get_results(request.GET["request"])
    return render(request, 'finder/search.html', {"results": results})

def index(request):
	process_one_link(request.GET["link"])
	return render(request, 'finder/start.html', {})


