from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from dashboard.models import Compromisso


# Create your views here.
def index(request):
    template = loader.get_template('home.html')
    dbCompromisso = Compromisso.objects.all()
    context = {
        'dbCompromisso':dbCompromisso,
    }
    return HttpResponse(template.render(context,request))

