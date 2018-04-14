from django.shortcuts import render

from django.http import HttpResponse


def featured(request):
    content = '<html>home</html>'

    response = HttpResponse(content, content_type='application/liquid')
    response['Content-Length'] = len(content)

    return response

