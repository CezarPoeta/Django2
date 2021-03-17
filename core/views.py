from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            
            messages.success(request, 'email enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro no envio do email')
            form = ContatoForm()

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')

