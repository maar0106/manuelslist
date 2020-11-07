from django.shortcuts import render
from bs4 import BeautifulSoup


def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    frontend = {
        'search': search,
    }
    return render(request, 'new_search.html', frontend)

