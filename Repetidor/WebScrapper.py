from enviar_email.models import Noticia
from Usuarios.models import Usuario
from GoogleNews import GoogleNews
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
import unidecode
import ast


def Web_scrapping_sender():
    usuarios = Usuario.objects.all()
    Web_scrapping_config(usuarios)


def Web_scrapping_config(usuarios):
    for usuario in usuarios:
        Noticia.objects.all().delete()
        endereco = []
        locais_decodificado = []
        locais_codificado = ast.literal_eval(usuario.region)
        for local in locais_codificado:
            local = local.replace(" ",",").split(',')
            locais_decodificado.append(local)
        for local in locais_decodificado:
            lang = local[0]
            country = local[1]
            gn = GoogleNews(lang = lang, country = country)
            filtros_codificado = ast.literal_eval(usuario.filtro)            
            for filtro in filtros_codificado:
                print(filtro)
                news = gn.search(filtro, proxies=None, scraping_bee = None)
                for item in news['entries']:
                    item['title'] = unidecode.unidecode(item['title'])
                    noticias = Noticia(link = item['link'], titulo = item['title'], filter = filtro, lingua = local[0], region = local[1])
                    noticias.save()
        noticias = Noticia.objects.all()
        endereco.append(usuario.email)
        html_content = render_to_string('templ_email.html', {'noticias': noticias, 'filtros': filtros_codificado})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives('Chego a noticia', text_content, settings.EMAIL_HOST_USER, bcc=endereco)
        email.attach_alternative(html_content, 'text/html')
        email.send()