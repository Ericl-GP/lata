"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('cessao1')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu com sucesso.')
    return redirect('userapp:login')
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Página inicial
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('cessao1')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu com sucesso.')
    return redirect('userapp:login')
#---------------------------------------------------------------------------

def home(request):
    return render(request, 'home.html')

# Função de login (manteve a lógica que você já tinha)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('cessao1')  # Substitua 'cessao1' pelo nome correto da sua página
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

# Função de logout
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu com sucesso.')
    return redirect('userapp:login')
""""""
# Função de registro (criar conta)
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile  # Ajuste conforme a estrutura do seu modelo de perfil

def register_view(request):
    if request.method == 'POST':
        try:
            # Captura os dados do formulário
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            data_conclusao = request.POST['data_conclusao']
            genero = request.POST['genero']
            campus = request.POST['campus']
            curso = request.POST['curso']
            nivel = request.POST['nivel']
            foto_perfil = request.FILES.get('file')  # Para o arquivo de foto de perfil

            # Validação das senhas
            if password1 != password2:
                messages.error(request, 'As senhas não coincidem.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já está em uso.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já está cadastrado.')
            else:
                # Criação do usuário
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()

                # Criar ou atualizar o perfil do usuário com os dados adicionais
                profile = UserProfile(
                    user=user,
                    data_conclusao=data_conclusao,
                    genero=genero,
                    campus=campus,
                    curso=curso,
                    nivel=nivel,
                    foto_perfil=foto_perfil
                )
                profile.save()

                # Mensagem de sucesso e redirecionamento
                messages.success(request, 'Conta criada com sucesso! Faça login.')
                return redirect('userapp:login')  # Ajuste conforme o nome da sua URL de login

        except KeyError as e:
            messages.error(request, f'O campo {e} não foi enviado corretamente.')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro: {e}')
    
    return render(request, 'register.html')

# Função para redefinir senha
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Redefinição de senha"
                    email_template_name = "password_reset_email.html"
                    context = {
                        "email": user.email,
                        "domain": request.get_host(),
                        "site_name": "Seu Site",
                        "uid": user.id,
                        "token": "gerar_token",  # Substituir por uma lógica para token real
                    }
                    email_content = render_to_string(email_template_name, context)
                    send_mail(subject, email_content, settings.DEFAULT_FROM_EMAIL, [user.email])
                messages.success(request, 'E-mail de redefinição de senha enviado.')
                return redirect('userapp:login')
            else:
                messages.error(request, 'Nenhum usuário encontrado com este e-mail.')
    return render(request, 'password_reset.html')
