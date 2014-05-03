from django import forms

class ExampleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_name = forms.EmailField(required = False)
    date_of_borth = forms.DateField(required = False)