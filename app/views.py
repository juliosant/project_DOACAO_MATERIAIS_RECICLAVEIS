from django.shortcuts import render

# Create your views here.


def home_page(request):
    content = {
        "Titulo": "Bem-vindo ao nosso site",
        "Sub_titulo": "Nosso objetivo é ajudar o meio ambiente com negócios"
    }
    return render(request, 'page/home_page.html', content)
