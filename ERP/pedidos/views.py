from django.shortcuts import render, get_object_or_404
from .models import Pedido

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, id=idPedido)
    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})

def crear_pedido(request):
    if request.method == 'POST':
        # Procesar formulario
        pass
    return render(request, 'pedidos/crear_pedido.html')
