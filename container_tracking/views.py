from .forms import SearchForm
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    form = SearchForm()
    return render(request, 'container_tracking/index.html', {'form': form})


def results(request, container_number):
    return render(request, 'container_tracking/results.html',
                  {'container_number': container_number})

def search(request):
    return HttpResponse("Funcionou!")