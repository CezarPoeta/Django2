from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

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
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preco: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}') 

            messages.success(request, 'Produto Salvo com Sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao Salvar Produto')
    else:
        form = ProdutoModelForm()
    
    # deve estar fora do if
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

