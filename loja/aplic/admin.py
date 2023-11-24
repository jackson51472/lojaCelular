from django.contrib import admin
from aplic.models import Cargo, Celular, Cliente, Endereco,  Fornecedor, Funcionario, Loja_Celular, Pedido, Telefone,Manutenção


class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1 

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", 'cpf', ]
    inlines = [EnderecoInline, TelefoneInline ]

    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf',"email", "salario", 'cargo',]
    inlines = [TelefoneInline ]


@admin.register(Loja_Celular)
class Loja_CelularAdmin(admin.ModelAdmin): 
    list_display = ['nome', 'cnpj',"telefone", 'funcionarios',]
    inlines = [EnderecoInline, TelefoneInline ]

@admin.register(Manutenção)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ["descricao", 'valor',"funcionarios" ]

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["data_pedido", 'data_entrega',"status_pedido", "cliente", ]


@admin.register(Celular)
class CelularAdmin(admin.ModelAdmin):
    list_display = ["nome", "fabricante", "sistema_operacionasl"]

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["nome", "telefone"]
    inlines = [EnderecoInline, TelefoneInline ]


