from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['item','mesa','descricao', 'qtd', 'valor_unit', 'valor_total']