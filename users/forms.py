from django import forms

class Login_form(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)

class Register_form(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)
    password_again = forms.CharField(label="Re-enter Password", max_length=30, widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
