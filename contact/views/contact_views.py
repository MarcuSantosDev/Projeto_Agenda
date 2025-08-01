from django.shortcuts import render,get_object_or_404
from contact.models import Contact
from django.http import Http404 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import Q
from django.core.paginator import Paginator
 
# Função para mostrar contatos na página principal
@login_required
def index(request):
  contacts = Contact.objects.filter(show=True).order_by('id')
  paginator = Paginator(contacts, 10)  
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  
  context = {
    'page_obj': page_obj,
    'site_title': 'Contatos - '
  }
  return render(request, 'contact/index.html',context)

# Função pro campo de pesquisa
@login_required
def search(request):
  search_value = request.GET.get('q','').strip() # Se não encontrar a queryset volta string vazia  
  if search_value == '':
    return redirect('contact:index')
 
  contacts = Contact.objects.filter(show=True).order_by('id').filter(
    Q(first_name__icontains=search_value) |   # Classe Q permite usar or usando um "|"
    Q(last_name__icontains=search_value) |
    Q(phone__icontains=search_value) |
    Q(email__icontains=search_value)
    ) # __ icontains é um teste de contenção que não diferencia maiúsculas de minúsculas.
  paginator = Paginator(contacts, 10)  
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
    
  context = {
    'page_obj': page_obj,
    'site_title': 'Site - ',
  }
  return render(request, 'contact/index.html',context)

@login_required
def contact(request,contact_id):
  single_contact = get_object_or_404(Contact,pk=contact_id,show=True) # Se não houver id existente levanta erro 404
  contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
  context = {
    'contact': single_contact,
    'site_title':contact_name
  }
  return render(request, 'contact/contact.html',context)

 
