from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if not first_name or not last_name or not username \
        or not email or not password or not password2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Senha precisa de no mínimo 6 caracteres')
        return render(request, 'accounts/register.html')

    if password != password2:
        messages.error(request, 'Senhas não coincidem')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Usuário já existente')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E- mail já cadastrado')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Registrado com sucesso! Faça o login:')
    user = User.objects.create_user(username=username, email=email, 
                                    password=password, first_name=first_name,
                                    last_name=last_name)
    user.save()                               
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact()
        return render(request, 'accounts/dashboard.html',{
            'form': form
        })
    
    form = FormContact(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Confira os campos novamente')
        form = FormContact(request.POST)
        return render(request, 'accounts/dashboard.html',{
            'form': form
        })

    form.save()
    messages.success(request, f'Contato {request.POST.get("name")} adicionado.')
    return redirect('dashboard')