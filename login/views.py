from django.shortcuts import render, redirect
from login.forms import AcessoForm
from login.models import Acesso

def tela_login(request):
    if request.method == 'POST':
        form = AcessoForm(request.POST)
        if form.is_valid():
            # Salva no banco de dados
            Acesso.objects.create(
                nome=form.cleaned_data['nome'],
                matricula=form.cleaned_data['matricula']
            )
            return redirect('https://www.atesa.com')
    else:
        form = AcessoForm()
    
    return render(request, 'login.html', {'form': form})

def lista_acessos(request):
    acessos = Acesso.objects.all().order_by('-data_acesso')
    return render(request, 'lista.html', {'acessos': acessos})