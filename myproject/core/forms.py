from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'address',
                  'complement', 'district', 'city', 'uf', 'cep', 'blocked']
