from django.shortcuts import render

def first_page(request):
	return render(request, 'finder/start.html', {})


def search(request):
    return render(request, 'finder/base.html')
                  # , {'info', request.data})

# Create your views here.
