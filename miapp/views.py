from django.shortcuts import render, redirect
from miapp.models import Cliente
from miapp.forms import FormularioCreacionCliente


def inicio(request):
    # return render(request, 'index.html')
    return render(request, 'miapp/inicio.html')


def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'miapp/clientes.html', {'clientes': clientes})


def registar_cliente(request):
    formulario = FormularioCreacionCliente()
    if request.method == 'POST':
        formulario = FormularioCreacionCliente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            email = formulario.cleaned_data.get('email')
            numero_de_telefono = formulario.cleaned_data.get('numero_de_telefono')
            producto = formulario.cleaned_data.get('producto')
            metodo_de_pago = formulario.cleaned_data.get('metodo_de_pago')
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email,
                              numero_de_telefono=numero_de_telefono,
                              producto=producto,
                              metodo_de_pago=metodo_de_pago)
            cliente.save()
            return redirect('clientes')
    return render(request, 'miapp/registrar_cliente.html', {'formulario': formulario})
