from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse


class Oauth(object):
    def hello(request):
        return HttpResponse("Hello world ! ")

    client_id = "603724490484088842"
    client_secret = "vo94_4fDE_z4_dkpU_Nl8DU_RwXK6ilo"
    scope = "identify%20guilds%20email"
    redirect_url = "http://127.0.0.1:8000//login"
    discord_login_url = f"https://discordapp.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code&scope={scope}"

