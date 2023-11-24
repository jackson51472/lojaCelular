from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from aplic.models import Celular, Cliente, User

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['celular'] = Celular.objects.all()
        return context

class DetalhesView(TemplateView):
    template_name = 'detalhes.html'

class ContatoView(TemplateView):
    template_name = 'contato.html'

class CelularesView(TemplateView):
    template_name = 'celulares.html'

class ManutencaoView(TemplateView):
    template_name = 'manutencao.html'

def cadastro (request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        
        username = request.POST.get('username')
        password = request.POST.get('senha')

        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
            return HttpResponse("Já existe usuario com esse cpf")
        
        user = User.objects.create_user(username=username, password=password)
        cliente = Cliente.objects.create(nome=nome, cpf=cpf, user=user)
        cliente.save()

        return HttpResponse("Cadastrado")


def cliente_login(request):
    if request.method == 'POST':
    
        nome = request.POST.get['nome']
        senha = request.POST.get['password']

        cliente = authenticate(request, username=nome, password=senha)

        if cliente is not None:         
            login(request, cliente)
            return redirect('/index')
    
    return render(request, 'login.html')