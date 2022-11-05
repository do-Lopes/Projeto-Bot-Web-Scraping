from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from .models import Noticia
from Usuarios.models import Usuario
import unidecode
from pyGoogleNewsFolder.pyGoogleNews import GoogleNews
import ast


def cria_template(request): 
    usuarios = Usuario.objects.all()
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
        email = EmailMultiAlternatives('News-Bot', text_content, settings.EMAIL_HOST_USER, bcc=endereco)
        email.attach_alternative(html_content, 'text/html')
        email.send()