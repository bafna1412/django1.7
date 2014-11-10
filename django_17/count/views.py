from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('count/index.html')
    context = RequestContext(request)
    dict = {'message': 'Displays IP of live users and their count'}

    return HttpResponse(template.render(context))
