python --version
django-admin --version

##criar projeto em Python

##Criar um ambiente virtual 

    python -m venv venv


ativar o ambiente virtual

    venv\Scripts\activate

#instalar o Django

    pip install Django

criar o projeto com Django

    django-admin startproject admin. (admin é o nome do projeto)

Gerar arquivo com as dependencias
    
    pip freeze > requirements.txt

executar as migration

    python manage.py migrate
    
executar o projeto

    python manage.py runserver

Criar o super usuario.

    python manage.py createsuperuser


Criar novo app dentro do projeto 

    python manage.py startapp nome-do-app

    python manage.py start app courses

   
Criar as migration que sera responsavel em criar a tebelas no banco de dados
    
    python manage.py makemigrations


Executar as migrations para criar as tebelas no banco de dados

    python manage.py migrate

executar as SEEDS para cadastrar registro de teste.

    python manage.py seed_home


Subir para p Github as alteracoes

    git status   # verifica o estado do repositorio
    
    git add .     # adicionar as alteracoes no indice

    git commit - m ""

    git push origin main   # envia as alteracoes para o git



atualizar o repositirio com o do git 

    git pull origin main