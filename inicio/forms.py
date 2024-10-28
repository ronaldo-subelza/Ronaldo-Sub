from django import forms   #importando modulos del formulario de django
from .models import Ropa   #importando ropa de modelos

#cree clase de formulario para ropa
class Ropaformu(forms.Form):
    class Meta:
        model = Ropa
#campos de formularios
fields = ['prenda', 'marca', 'talla']
labels = {"prenda":"nombre de la prenda","marca":" marca", "talla":"talla"}
widgets = {"prenda":forms.TextInput(attrs={"placeholder:nombre de la prenda"}),"marca":forms.TextInput(attrs={"placeholder:nombre de la marca"}), "talla":forms.NumberInput(attrs={"placeholder:nombre de la talla"})}
def __str__(self):
   return f'{self.prenda}-{self.marca}-{self.talla}'