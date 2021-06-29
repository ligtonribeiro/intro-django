from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria',
                    'tempo_preparo', 'data_receita')
    list_display_links = ('id', 'nome_receita')
    list_filter = ('categoria',)
    search_fields = ('nome_receita',)
    list_per_page = 10


admin.site.register(Receita, ListandoReceitas)
