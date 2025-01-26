from django.db import models


# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    subtitle = models.CharField(max_length=255, verbose_name="Subtitulo")
    text_btn = models.CharField(max_length=50, verbose_name="Texto do Botão")
    link_btn = models.URLField(max_length=500, verbose_name="Link do Botão")
    title_topics = models.CharField(max_length=255, verbose_name="Titulo dos Tópicos")
    subtitle_topics = models.CharField(max_length=255, verbose_name="Subtitulo dos Tópicos")
    title_topic_one = models.CharField(max_length=255, verbose_name="Titulo do Topico 1")
    description_topic_one = models.TextField(verbose_name="Descrição do Topico 1")
    title_topic_two = models.CharField(max_length=255, verbose_name="Titulo do Topico 2")
    description_topic_two = models.TextField(verbose_name="Descrição do Topico 2")
    title_topic_three = models.CharField(max_length=255, verbose_name="Titulo do topico 3")
    description_topic_three = models.TextField(verbose_name="Descricao do Topico 3")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "Pagina Inicial"
        verbose_name_plural= "Paginas Iniciais"
        
class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    email =models.EmailField(verbose_name="E-mail")
    subject = models.CharField(max_length=255, verbose_name="Assunto")
    message = models.TextField(verbose_name="Mensagem")
    
    creted_at = models.DateTimeField( auto_now_add=True,
    verbose_name="Data de Criação")
    update_at = models.DateTimeField(auto_now_add=True,
    verbose_name="Data de Edção")                                 

    def __str__(self):
        
        return self.subject
    
    class Meta:
        verbose_name= "mensagem de contato"
        verbose_name_plural= "mensagens de contatos"