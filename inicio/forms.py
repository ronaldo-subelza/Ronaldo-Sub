from django import forms   #importando modulos del formulario de django
from .models import Ropa   #importando ropa de modelos

#cree clase de formulario para ropa
class Ropaformu(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['prenda', 'marca', 'talla']  # Asegúrate de que estos son los campos correctos
        labels = {
            'prenda': 'Nombre de la prenda',
            'marca': 'Marca',
            'talla': 'Talla',
        }
        widgets = {
            'prenda': forms.TextInput(attrs={'placeholder': 'Nombre de la prenda'}),
            'marca': forms.TextInput(attrs={'placeholder': 'Nombre de la marca'}),
            'talla': forms.NumberInput(attrs={'placeholder': 'Talla'}),
        }
        
class RopaSearch(forms.Form):
    prenda = forms.CharField(required=False,label='prenda',max_length=20)
    marca = forms.CharField(required=False,label='marca',max_length=20)
    talla = forms.IntegerField(required=False,label='talla',min_value=0)