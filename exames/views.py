from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExames
from datetime import datetime


@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all() #-> Opção para trazer todos os exames
    #if not request.user.is_authenticated:
        #return HttpResponse("VocÊ não está logado!")
    #return HttpResponse('Estou aqui')
    if request.method == "GET":        
        #for i in tipos:
            #print(i)
         #   print(i.nome)
         #   print(i.preco)
         #   print('-' * 10)
        #TiposExames.objects.filter() -> Opção para filtrar um exame específico
        return render(request, 'solicitar_exames.html', {'tipos_exames':tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        print(solicitacao_exames)

        #TODO: verificar o preço dos dados disponiveis
        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco
        
        return render(request, 'solicitar_exames.html', {'tipos_exames':tipos_exames,
                                                          'solicitacao_exames': solicitacao_exames,
                                                          'preco_total':preco_total})
    
def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')
    #print(exames_id)
    pedido_exame = PedidosExames(
        usuario=request.user,
        data=datetime.now()
    )
    pedido_exame.save()

    return HttpResponse('Estou aqui')
