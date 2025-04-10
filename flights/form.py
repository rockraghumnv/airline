from django import forms

class Search_form(forms.Form):
    origin = forms.CharField(label = "From",max_length = 30)
    destination = forms.CharField(label = "To",max_length = 30) 

class Book_form(forms.Form):
    firstname = forms.CharField(label = "Firstname",max_length = 30)
    lastname = forms.CharField(label="lastname",max_length=30)
    