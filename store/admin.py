from django.contrib import admin
from . models import Category, Customer, Order, Product


# Adicionando os itens do BD ao nosso admin com o perfil super
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)

