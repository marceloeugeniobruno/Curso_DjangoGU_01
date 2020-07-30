from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação web com Django Framework',
        'apresentacao': 'Curso fantástico da Geek University'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
