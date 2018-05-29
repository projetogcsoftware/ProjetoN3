from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


# Create your views here.

def home(request):
    nome= 'Gabriel'
    prod = Produto.objects.all()
    return render(request, 'produtos.html',{'nome': nome,'prod': prod})

def cria_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'produto-form.html', {'form': form})

def altera_produto(request,id):
    prod = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance = prod)

    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'produto-form.html', {'form': form, 'prod': prod})

def deleta_produto(request, id):
    prod = Produto.objects.get(id=id)

    if request.method == 'POST':
        prod.delete()
        return redirect('lista_produto')

    return render(request, 'prod-delete-confirm.html', {'prod':prod})
