from enviar_email.models import Noticia
from Usuarios.models import Usuario
from GoogleNews import GoogleNews
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
import unidecode


googlenews = GoogleNews()

def Web_scrapping_config():
    noticias = Noticia.objects.all().delete()
    locais = [['pt', 'BR']]
    for local in locais:
        lang = local[0]
        country = local[1]
        gn = GoogleNews(lang = lang, country = country)
        filtros = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'HEALTH', 'SCIENCE']
        for filtro in filtros:
            news = gn.search(filtro, proxies=None, scraping_bee = None)
            for item in news['entries']:
                item['title'] = unidecode.unidecode(item['title'])
                noticias = Noticia(link = item['link'], titulo = item['title'], filter = filtro, lingua = local[0], region = local[1])
                noticias.save()


def Web_scrapping_sender():
    filtros_BR = ['MUNDO', 'PAIS', 'NEGÓCIOS', 'TECNOLOGIA', 'ESPORTES', 'SAÚDE', 'CIÊNCIA E TECNOLOGIA']
    noticias = Noticia.objects.all().delete()
    Web_scrapping_config()    
    noticias = Noticia.objects.all()
    enderecos = Usuario.objects.all()
    html_content = render_to_string('templ_email.html', {'noticias': noticias, 'filtros': filtros_BR})
    text_content = strip_tags(html_content)    
    email = EmailMultiAlternatives('Chego a noticia', text_content, settings.EMAIL_HOST_USER, bcc=enderecos)
    email.attach_alternative(html_content, 'text/html')
    email.send()


