from django.shortcuts import render

from .models import Home

def home(request):
    # recuperar o conteudo da pagina home
    
    home = Home.objects.filter().first()
    return render(request, 'courses/home.html', {'home': home})
