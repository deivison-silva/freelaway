from django.shortcuts import render

def cadastrar(request):
    return render(request, 'autenticacao/cadastro.html')


def logar(request):
    return render(request, 'autenticacao/logar.html')
