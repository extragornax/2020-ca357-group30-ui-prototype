from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Index route


def index(request):
    context = {}
    return render(request, 'dashboard/index.html', context)