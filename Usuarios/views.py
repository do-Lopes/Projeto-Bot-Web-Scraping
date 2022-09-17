from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario
from enviar_email.models import Noticia
from hashlib import sha256

filtrado = []

def login(request):
    status = request.GET.get('status')
    return render(request, 'index_login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'index_cadastro.html', {'status': status})

def validar_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, senha = senha, email = email)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

    

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/auth/home')


def cadastrar_filtros(request):
    if request.POST.get("adicionar"): 
        filtro: str = request.POST.get('filtro')
        filtro = filtro.upper().strip()
        if len(filtro) > 0:
            filtrado.append(filtro)
            return redirect('/email/home/?status=0') 
        else: 
            return redirect('/email/home/?status=2')
    elif request.POST.get("salvar"):
        Usuario.objects.filter(id = request.session['usuario']).update(filtro = filtrado)
        filtrado.clear()
        return redirect('/email/home/?status=1')

def home(request):
    status = request.GET.get('status')
    if request.session.get('usuario'):
        noticias = Noticia.objects.all()
        return render(request, 'filtros.html',{'status': status, 'noticia': noticias})
    else:
        return redirect('/auth/login/?status=2')

def sair(request):
    request.session.flush()
    return redirect(f'/email/home/')
