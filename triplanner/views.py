from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    content = '<html>home</html>'

    response = HttpResponse(content, content_type='text/html')
    response['Content-Length'] = len(content)

    return response

