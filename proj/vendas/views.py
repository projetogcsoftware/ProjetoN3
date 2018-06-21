from django.shortcuts import render,redirect,reverse
from produtos.models import Produto
from .forms import VendaForm,MesaForm
from .models import Venda,Mesa
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = redirect(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
    reponse = redirect()

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "Hello world.")

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
    return response

def lista_venda(request):
    prod =  Produto.objects.all()
    return render(request, 'pedido-form.html',{'prod': prod})

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
    obj_mesa = Mesa.objects.get(id=mesa)
    obj_mesa.situ = 1
    if form.is_valid():
        form.save()
        obj_mesa.save()

        return redirect(reverse(('cria_venda'), kwargs={'mesa': mesa}))
    return render(request, 'pedido-form.html', {'form': form,'prod': prod,'mesa': mesa})

def fecha_venda(request,mesa):
    venda = Venda.objects.filter(mesa=mesa, situ = 0)
    form = VendaForm(request.POST or None)
    total = 0
    for lista in venda:
      total = total + (lista.qtd * lista.valor_unit)

    return render(request, 'venda-fecha-form.html', {'venda': venda,'mesa': mesa, 'total':total})

def libera_produto(request,mesa):
    venda = Venda.objects.filter(mesa=mesa, situ = 0)
    mesa  = Mesa.objects.get(id=mesa)

    if request.method == 'POST':
        altera_situ(venda,mesa)
        return redirect('lista_mesa')

    return render(request, 'venda-fecha-confirm.html',{'mesa': mesa})

def altera_situ(vendas,mesa):

    for lista in vendas:
        lista.situ = 1
        lista.save()

    mesa.situ = 0
    mesa.save()

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


