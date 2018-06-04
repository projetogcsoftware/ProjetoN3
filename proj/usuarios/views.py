from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def lista_usuario(request):
    usu =  Usuario.objects.all()
    return render(request, 'pedido.html',{'usu': usu})



def cria_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_usuario')
    return render(request, 'usuario-form.html', {'form': form})


def altera_usuario(request,id):
    usu = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance = usu)

    if form.is_valid():
        form.save()
        return redirect('lista_usuario')
    return render(request, 'usuario-form.html', {'form': form, 'usu': usu})

def deleta_usuario(request, id):
    usu = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usu.delete()
        return redirect('lista_usuario')

    return render(request, 'usu-delete-confirm.html', {'usu':usu})
