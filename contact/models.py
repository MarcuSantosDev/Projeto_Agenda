from django.db import models
from django.utils import timezone # tempo atual
from django.contrib.auth.models import User


class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'   
  
  def __str__(self) -> str:
    return f'{self.name}'


class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50,blank=True)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=254, blank=True)
  created_date = models.DateTimeField(default=timezone.now)  # Django executa a função timezone.now() quando o objeto Contato é criado
  description = models.TextField(blank=True)
  show = models.BooleanField(default=True)
  picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m') # Depende do pillow
  category = models.ForeignKey(Category,
  on_delete=models.SET_NULL,  # Tipos de on_delete => 1) CASCADE 2) SET_NULL 3) PROTECT 4 ) SET_DEFAULT
  blank=True,null=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
  
  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'      

  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name}'
  

 
