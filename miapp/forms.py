from django import forms


class FormularioCreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=100)
    numero_de_telefono = forms.IntegerField()
    producto = forms.CharField(max_length=100)
    metodo_de_pago = forms.CharField(max_length=50)
