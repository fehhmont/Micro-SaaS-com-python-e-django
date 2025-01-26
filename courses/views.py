from urllib import request
from django.shortcuts import render, redirect # type: ignore
from .forms import ContactForm
from .models import Home
from django.contrib import messages # type: ignore



def home(request):
    # recuperar o conteudo da pagina home
    
    home = Home.objects.filter().first()
    return render(request, 'courses/home.html', {'home': home})



def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect('contact')
        else:
            messages.error(request, "Erro ao enviar Mensagem, entre em contato com o suporte!")
    else:
        form = ContactForm()  # Certifique-se de que "ContactForm" é um formulário no models.py ou forms.py
    
    return render(request, 'courses/contact.html', {'form': form})