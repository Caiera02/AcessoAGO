from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.forms import AcessoForm
from login.models import Acesso
import random

def tela_login(request):
    if request.method == 'POST':
        form = AcessoForm(request.POST)
        if form.is_valid():
            # Salva no banco de dados
            Acesso.objects.create(
                nome=form.cleaned_data['nome'],
                matricula=form.cleaned_data['matricula']
            )
            return redirect('https://youtube.com/live/62DzEKaNSIg?feature=share')
    else:
        form = AcessoForm()
    
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/admin/')
def lista_acessos(request):
    acessos = Acesso.objects.all().order_by('-data_acesso')
    return render(request, 'lista.html', {'acessos': acessos})

@login_required(login_url='/admin/')
def sorteador(request):
    acessos = Acesso.objects.all()
    lista_participantes = list(acessos.values('nome', 'matricula'))
    sorteado = random.choice(lista_participantes)
    
    return render(request, 'sorteio.html', {'numero': sorteado})