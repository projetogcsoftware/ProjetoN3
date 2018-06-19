from django.shortcuts import render,redirect,reverse
from produtos.models import Produto
from .forms import VendaForm,MesaForm
from .models import Venda,Mesa

def lista_venda(request):
    prod =  Produto.objects.all()
    return render(request, 'pedido-form.html',{'prod': prod})

def lista_venda_pedido(id,mesa,desc,qtd,vl_t,vl_u,listaPedido, request):
    prod =  Produto.objects.all()
    listaPedido.append(id,
                   mesa,
                   desc,
                   qtd,
                   vl_t,
                   vl_u)
    return render(request, 'pedido-form.html',{'prod': prod,'listaPedido': listaPedido,'Venda': Venda})

def lista_venda_pedidotemp(Venda,listaPedido, request):
    prod =  Produto.objects.all()
    listaPedido.append(Venda.item,
                   Venda.mesa,
                   Venda.descricao,
                   Venda.qtd,
                   Venda.valor_total,
                   Venda.valor_unit)
    return render(request, 'pedido-form.html',{'prod': prod,'listaPedido': listaPedido,'Venda': Venda})

def cria_venda(request,mesa):
    prod = Produto.objects.all()
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse(('cria_venda'), kwargs={'mesa': mesa}))
    return render(request, 'pedido-form.html', {'form': form,'prod': prod,'mesa': mesa})

def altera_venda(request,id):
    ven = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance = ven)

    if form.is_valid():
        form.save()
        return redirect('lista_Venda')
    return render(request, 'Venda-form.html', {'form': form, 'ven': ven})

def deleta_venda(request, id):
    ven = Venda.objects.get(id=id)

    if request.method == 'POST':
        ven.delete()
        return redirect('lista_Venda')

    return render(request, 'ven-delete-confirm.html', {'ven':ven})

def lista_mesa(request):
    mesa = Mesa.objects.all()
    return render(request, 'mesa.html', {'mesa': mesa})

def  cria_mesa(request):
    form = MesaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_mesa')
    return render(request, 'mesa-form.html', {'form': form})