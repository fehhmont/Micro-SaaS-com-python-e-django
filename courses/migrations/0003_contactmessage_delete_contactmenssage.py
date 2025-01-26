# Generated by Django 5.0.11 on 2025-01-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_contactmenssage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=255, verbose_name='Assunto')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('creted_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Edção')),
            ],
            options={
                'verbose_name': 'mensagem de contato',
                'verbose_name_plural': 'mensagens de contatos',
            },
        ),
        migrations.DeleteModel(
            name='ContactMenssage',
        ),
    ]