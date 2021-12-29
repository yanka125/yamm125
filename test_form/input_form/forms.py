from django import forms


class InputForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)