#BaseCommand: classe para criar comandos personalizados no Django. Ao herdar,
#ao herdar dessa classe pode ser criado comandos que sao executados pelo manage.py no terminal

from django.core.management.base import BaseCommand

# Home: importar os modelos, o modelo representa a tebela no banco de dados onde os dados seram manipulados

from courses.models import Home


class Command(BaseCommand):
    # mensagem de ajuda que descreve o proposito do comando
    
    help = 'Seed para cadastrar registro na tebela Home'
    
    # o self permite que o metodo acesse os atributos e outros metodos definidos na classe
    # args: tupla de argumentos posicionais
    # kwargs: dicionario de arqugmentos noemados
    def handle(self, *args, **kwargs):
        # criar a lista de planos com os dados a serem cadastrados 
         home = {
            'title': 'Bem-vindo à Academia Xxxxx!',
            'subtitle': 'Transforme seu corpo e sua mente com treinos personalizados e alcance seus objetivos de forma eficiente.',
            'text_btn': 'Explore Nossos Planos',
            'link_btn': 'https://celke.com.br',
            'title_topics': 'Por Que Treinar Conosco?',
            'subtitle_topics': 'Cuidar da saúde e bem-estar é essencial para uma vida equilibrada e feliz. Treinar na nossa academia ajuda você a:',
            'title_topic_one': 'Manter-se Saudável',
            'description_topic_one': 'Melhore sua saúde física e mental com treinos que se adaptam ao seu estilo de vida.',
            'title_topic_two': 'Alcançar Resultados',
            'description_topic_two': 'Conte com profissionais qualificados para ajudar você a atingir suas metas de forma eficiente.',
            'title_topic_three': 'Ganhar Confiança',
            'description_topic_three': 'Melhore sua autoestima e bem-estar geral com um corpo saudável e ativo.',
        }
         
         # atualizar o registro existente ou cria um novo com base no titulo
         Home.objects.update_or_create(
             title=home['title'], #criterio de busca: titulo
             defaults=home # Valores padrao para criar ou atualizar   
         )
         
         # exbir mensagem de sucesso
         
         self.stdout.write(self.style.SUCCESS('Conteudo da pagina inicial adicionado com sucesso'))
            

        