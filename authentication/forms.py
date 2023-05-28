from django import forms


class CadastroForm(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40, widget=forms.TextInput(attrs={"class":"form"}))
    last_name = forms.CharField(label="Sobrenome", max_length=40, widget=forms.TextInput(attrs={"class":"form"}))
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class":"form"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form"}))
    password = forms.CharField(label="Senha", max_length=25, min_length=8,widget=forms.PasswordInput(attrs={"class":"form"}))
    confirm_password = forms.CharField(label="Confirme sua senha", max_length=25, min_length=8, widget=forms.PasswordInput(attrs={"class":"form"}))

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class":"login-form"}))
    password = forms.CharField(label="Senha", max_length=25, widget=forms.PasswordInput(attrs={"class":"login-form"}))