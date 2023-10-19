from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def solicitar_exames(request):
    #if not request.user.is_authenticated:
        #return HttpResponse("VocÊ não está logado!")
    return HttpResponse('Estou aqui')
