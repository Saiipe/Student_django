from django.shortcuts import render


def cadastro(request):
    if request.method == "GET":
        pessoa: dict = {'nome': "Tauan Sãáé",
                        'idade': 20,
                        'profissao': "DEV"}

        return render(request, 'index.html', {'pessoa': pessoa})
