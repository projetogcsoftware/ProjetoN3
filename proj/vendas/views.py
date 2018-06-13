from django.shortcuts import render,redirect
from .models import Venda
from .forms import VendaForm

def lista_venda(request):
    ven =  Venda.objects.all()
    return render(request, 'pedido.html',{'ven': ven})



def cria_venda(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_Venda')
    return render(request, 'Venda-form.html', {'form': form})


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