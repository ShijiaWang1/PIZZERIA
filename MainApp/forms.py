
from django import forms

from.models import Topping


class PizzaForm(forms.ModelForm):
    class Meta:
        Model = Topping
        fields = ['text']
        labels = {'text':''}