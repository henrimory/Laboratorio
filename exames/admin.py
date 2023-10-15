from django.contrib import admin
from .models import TiposExames, PedidosExames, SolicitacaoExame


admin.site.register(TiposExames)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExames)

# Register your models here.
