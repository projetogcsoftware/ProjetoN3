from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from datetime import datetime
from .models import Venda,Mesa

#exemplo de impressão
def some_view1(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def imprime_venda(mesa):
    venda = Venda.objects.filter(mesa=mesa, situ = 1)
    total = 0
    #for lista in venda:
    #  total = total + (lista.qtd * lista.valor_unit)

    return venda

def some_view(request):
    dataHora =  datetime.now()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    c.drawString(30, 750, 'SISTEMA DE RESTAURANTE')
    c.drawString(30, 725, 'GERENCIAMENTO DE COMANDA')
    c.drawString(450, 750, 'Dia')
    c.drawString(500, 750, dataHora.strftime('%d/%m/%Y'))
    c.line(480, 747, 580, 747)

    c.drawString(30, 690, 'RELATORIO DE FATURAMENTO:')
    #c.line(120, 700, 580, 700)
    #c.drawString(120, 703, "JOHN DOE")

    c.drawString(30, 675, 'ID PEDIDO:')
    c.drawString(100, 675, 'NOME PROD:')
    c.drawString(350, 675, 'QTD')
    c.drawString(400, 675, 'UNIT')
    c.drawString(450, 675, 'TOTAL')
    venda = imprime_venda(1)
    i = 660
    total = 0
    for lista in venda:
        c.drawString(30, i, str(lista.id))
        c.drawString(100, i, str(lista.descricao))
        c.drawString(350, i, str(lista.qtd))
        c.drawString(400,i, str(lista.valor_unit))
        c.drawString(450, i, str(lista.qtd * lista.valor_unit))
        total = total + (lista.qtd * lista.valor_unit)
        i  = i - 15

    c.drawString(450, 725, 'Total')
    c.drawString(500, 725, str(total))
    c.line(480, 723, 580, 723)
    c.showPage()
    c.save()
    return response