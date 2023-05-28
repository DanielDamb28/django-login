from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . import forms

# Create your views here.

def login_screen(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                form = forms.LoginForm()
                return render(request, 'authentication/login.html', {"form": form, "error":"Username ou Senha inválidos"}) 
    else:
        form = forms.LoginForm()
        return render(request, 'authentication/login.html', {"form": form})

def cadastro_screen(request):
    if request.method == "POST":
        form = forms.CadastroForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                valid_user = User.objects.filter(username=username).first()
                if valid_user:
                    return render(request, 'authentication/cadastro.html', {'form': form, 'error': 'Esse usuário já está sendo utilizado'})
                else:
                    new_user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
                    send_mail('Registrado com Sucesso', 'Você foi cadastrado com sucesso em nosso site!', 'settings.EMAIL_HOST_USER', [email])
                    messages.success(request, 'Usuário cadastrado com sucesso!')
                    return HttpResponseRedirect('/auth/login/')
            else:
                return render(request, 'authentication/cadastro.html', {'form': form, 'error': 'As senhas precisam ser iguais'})
        else:
            return render(request, 'authentication/cadastro.html', {'form': form})

    else:
        form = forms.CadastroForm()
        return render(request, 'authentication/cadastro.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')

@login_required(login_url='/auth/login/')
def home_screen(request):
    return render(request, 'authentication/home.html')