from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from .models import Compromisso
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    if request.method == 'POST':
        oque = request.POST['oquecadastro']
        onde = request.POST['ondecadastro']
        quedia = request.POST['quediacadastro']
        comquem = request.POST['comquemcadastro']
        obs = request.POST['obscadastro']
        usuarioidcadastro = request.POST['usuarioidcadastro']
        dbCompromisso = Compromisso(oque=oque, onde=onde , dia=quedia , comQuem=comquem , obs=obs , usuario=User(usuarioidcadastro) )
        dbCompromisso.save()
        return HttpResponseRedirect('/')
    template = loader.get_template('create.html')
    return HttpResponse(template.render({},request))

def delete_item(request,id):
    dbCompromisso = Compromisso.objects.get(id=id)
    dbCompromisso.delete()
    return HttpResponseRedirect('/')

def update_compromisso(request,id):
     compromissoId = Compromisso.objects.get(id=id)
     basicoCompromisso = Compromisso.objects.all()
     context = {
         'compromissoId':compromissoId,
         'basicoCompromisso':basicoCompromisso,
     }
     if request.method == 'POST':
        oque = request.POST['oquecadastro']
        onde = request.POST['ondecadastro']
        quedia = request.POST['quediacadastro']
        comquem = request.POST['comquemcadastro']
        obs = request.POST['obscadastro']
        compromissoId.oque = oque
        compromissoId.onde = onde
        compromissoId.dia = quedia
        compromissoId.comQuem = comquem
        compromissoId.obs = obs
        compromissoId.save()
        return HttpResponseRedirect('/')
     else:
        template = loader.get_template('update.html')
        return HttpResponse(template.render(context,request))