from django.shortcuts import render

receitas = {
    1: 'Sopa de Carne',
    2: 'Sorvete',
    3: 'Sopa de Legumes',
    4: 'Lasanha'
}

dados = {
    'nome_das_receitas': receitas
}


def index(request):
    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
