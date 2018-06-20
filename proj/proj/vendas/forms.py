from django import forms
from .models import Venda,Mesa

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['item','mesa','descricao', 'qtd', 'valor_unit','situ']

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero','situ']