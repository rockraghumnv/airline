from django.forms import forms

class Search_form(forms.Form):
    origin = forms.CharField(label = "From",max_length = 30)
    destination = forms.CharField(label = "To",max_length = 30) 