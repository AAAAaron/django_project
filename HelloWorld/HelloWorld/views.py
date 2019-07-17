


from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

