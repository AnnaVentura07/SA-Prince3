from django.contrib import admin
from .models import Categoria, Dica, Estoque, Produto, Ingrediente

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Ingrediente)
admin.site.register(Estoque)
admin.site.register(Dica)