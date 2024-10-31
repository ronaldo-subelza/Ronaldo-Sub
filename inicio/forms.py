from django import forms

class CrearIndumentariaFormulario(forms.Form):
    prenda= forms.CharField(max_length=20)
    marca= forms.CharField(max_length=20)
    talla= forms.IntegerField()
    
class BuscarIndumentariaFormulario(forms.Form):
    prenda= forms.CharField(max_length=20, required=False)
    # marca= forms.CharField(max_length=20)
    # talla= forms.IntegerField()