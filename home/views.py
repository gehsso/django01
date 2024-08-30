from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def perfil(request,usuario):
    return render(request,'perfil.html',{'usuario':usuario})

def diasemana(request, dia):
    dias = ["Domingo","Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
            "Sexta-feira", "Sábado"]
    try:
        diadasemana = dias[dia-1]  # Subtrai 1 porque a lista começa no índice 0
    except IndexError:
        diadasemana = "Dia inválido"

    return render(request, 'diasemana.html', {'diadasemana': diadasemana})


def produto(request):
    contexto = {
        'lista': [
            {'ID':1,'nome':'Notebook','preco':'3500,00'},
            {'ID': 2, 'nome': 'Monitor', 'preco': '1500,00'},
            {'ID': 3, 'nome': 'Teclado', 'preco': '50,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def form_produto(request):
    return render(request, 'produto/formulario.html')





