from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small','Small'), ('Medium','Medium'), ('Large','Large')])
''' Ejemplo de uso de widgets'''
    # toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple) 
    # size = forms.ChoiceField(label='Size', choices=[('Small','Small'), ('Medium','Medium'), ('Large','Large')])


class PizzaForm(forms.ModelForm):
    # image = forms.ImageField() # Agrega un boton "Adjuntar imagen" en el form
    class Meta:
        model = Pizza
        fields = ['topping_1', 'topping_2', 'size']
        labels = {'topping_1': 'Select Topping 1', 'topping_': 'Select Topping 2'}
        # widgets = {'size':forms.CheckboxSelectMultiple}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)