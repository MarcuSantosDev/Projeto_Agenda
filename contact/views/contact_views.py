from django.shortcuts import render,get_object_or_404
from contact.models import Contact
from django.http import Http404 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import Q

@login_required
def index(request):
  contacts = Contact.objects.filter(show=True).order_by('id')
  context = {
    'contacts': contacts,
    'site_title': 'Contatos - '
  }
  return render(request, 'contact/index.html',context)

@login_required
def search(request):
  search_value = request.GET.get('q','').strip() # Se não encontrar a queryset volta string vazia
  print('search_value',search_value)
  
  if search_value == '':
    return redirect('contact:index')
  print(search_value)
  contacts = Contact.objects.filter(show=True).order_by('id').filter(
    Q(first_name__icontains=search_value) |   # Classe Q permite usar or usando um "|"
    Q(last_name__icontains=search_value) |
    Q(phone__icontains=search_value) |
    Q(email__icontains=search_value)
    ) # __ icontains é um teste de contenção que não diferencia maiúsculas de minúsculas.

  print(contacts.query)
  context = {
    'contacts': contacts,
    'site_title': 'Site - '
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

 
