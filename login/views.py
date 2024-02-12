from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_usuario(request):
    if request.method == 'POST':
        loginUsuario = request.POST['loginUsuario']
        senhaUsuario = request.POST['senhaUsuario']
        usuario = authenticate(request, username=loginUsuario, password=senhaUsuario)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/')

def cadastro_usuario(request):
    if request.method == 'POST':
        loginUsuarioCadastro = request.POST['loginUsuarioCadastro']
        senhaUsuarioCadastro = request.POST['senhaUsuarioCadastro']
        usuario = User.objects.create_user(username=loginUsuarioCadastro, password=senhaUsuarioCadastro)
        usuario.save()
        usuario = authenticate(request, username=loginUsuarioCadastro, password=senhaUsuarioCadastro )
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')
    template = loader.get_template('cadastro_usuario.html')
    return HttpResponse(template.render({},request))