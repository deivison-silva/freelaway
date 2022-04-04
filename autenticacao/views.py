from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/cadastrar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            return redirect('/auth/cadastrar')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastrar')

        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/auth/cadastrar')

        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            return redirect('/auth/logar')
        except:
            return redirect('/auth/cadastrar')


def logar(request):
    return render(request, 'autenticacao/logar.html')
