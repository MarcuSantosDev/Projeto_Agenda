from django.contrib import admin
from contact import models

@admin.register(models.Category)
  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # Mostra as informações no Admin
    search_fields = ['name']
@admin.register(models.Contact)
  
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone','show') # Mostra as informações no Admin
    ordering = 'id',
    # list_filter = 'create_date', # Filtro por data
    search_fields = ['id','first_name','last_name'] # Campo de busca
    list_per_page = 10
    list_max_show_all = 10 # Quantidade máxima de registros por paginação
    list_editable = ('show','first_name','last_name') # Permite editar os campos
    list_display_links = 'id','phone' # Cria um link ao clicar para editar ocampo selecionado

    