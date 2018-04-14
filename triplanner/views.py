from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader



def home(request):
    return render(request, 'test.html', context=None, content_type='application/xhtml+xml')
