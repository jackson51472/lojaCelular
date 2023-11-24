import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return filename

class SistemasChoices(models.IntegerChoices):
    ANDROID = 1, 'Android'
    IOS = 2, 'iOS'
    OUTROS = 3, 'Outros'

class Pessoa(models.Model):   
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    email = models.CharField(_("Email"), blank=False, max_length=11, unique=True)
    telefone = models.CharField(_("Telefone"), blank=False, max_length=11, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome 

class Cargo(models.Model):

    nome= models.CharField(_('Nome Cargo'), max_length=100)
    carga_horaria = models.DecimalField(_("Carga horária"),blank=False, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
    
    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    cargo = models.ForeignKey(Cargo, null=True, on_delete= models.SET_NULL)
    salario = models.DecimalField(_("Salario"), null=True, blank=False, max_digits=8, decimal_places=2)


    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')

    def __str__(self):
        return f"{self.nome} / {self.cargo}"
    
class Cliente(Pessoa):
    entrega = models.CharField(_("Endereço"), blank=False, max_length=50,)
    
    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return f"{self.nome}"
    
class Manutenção(models.Model):
    descricao = models.CharField(_("Decrição do erro"),  max_length=300,) 
    valor = models.DecimalField(_("Custo da Manutenção"), decimal_places=2, max_digits=10)
    funcionarios = models.ForeignKey(Funcionario, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Manutenção')
        verbose_name_plural = _('Manutenções')

    def __str__(self):
        return f"{self.descricao}"
    
class Fornecedor(models.Model):
    nome = models.CharField(_("Nome do Fornecedor"),  max_length=300,) 
    telefone = models.CharField(_("Telefone"), blank=False, max_length=50,)

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')

    def __str__(self):
        return f"{self.nome}"

class Celular(models.Model):
    nome = models.CharField(_("Nome do celular"),  max_length=300,) 
    fabricante = models.CharField(_("Fabricante"),  max_length=300,) 
    sistema_operacionasl = models.IntegerField(choices=SistemasChoices.choices, default=SistemasChoices.OUTROS)
    ram =models.IntegerField(_("Memória Ram"),  ) 
    armazenamento = models.IntegerField(_("Armazenamento"),)
    preco = models.DecimalField(_("Preço Celular"), blank=False, decimal_places=2, max_digits=10) 
    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete= models.SET_NULL)
   

    class Meta:
        verbose_name = _('Celular')
        verbose_name_plural = _('Celulares')

    def __str__(self):
        return f"{self.nome} {self.preco}"

class Pedido(models.Model):
    data_pedido = models.DateTimeField(_("Data pedido",))
    data_entrega = models.DateTimeField(_("Data entrega",))
    status_pedido = models.BooleanField(_("Finalizado"))  
    cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
    manuntecao = models.ForeignKey(Manutenção, blank=True, null=True ,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')
    
    def __str__(self):
        return f"{self.cliente} {self.status_pedido}"

class Loja_Celular(models.Model):    
    nome = models.CharField(_("Nome"), blank=False, max_length=50,) 
    cnpj = models.CharField(_("CPNJ"), blank=False, max_length=50,)
    telefone = models.CharField(_("Telefone"), blank=False, max_length=50,)
    funcionarios = models.ForeignKey(Funcionario, null=True, on_delete= models.SET_NULL)
    celulares = models.ManyToManyField(Celular)

    class Meta:
        verbose_name = _('Loja')
        verbose_name_plural = _('Lojas')

    def __str__(self):
        return f"{self.nome}"
    
class Endereco(models.Model):
    cidade = models.CharField(_("Cidade"), blank=False, max_length=50,)
    bairro = models.CharField(_("Bairro"), blank=False, max_length=50,)
    rua = models.CharField(_("Rua"), blank=False, max_length=50,)
    numero = models.CharField(_("Numero"), blank=False, max_length=50,)
    complemento = models.CharField(_("Complemento"), blank=False, max_length=50,)
    fornedor_end = models.ForeignKey(Fornecedor,  null=True, on_delete=models.SET_NULL, related_name='Fornecedot')
    cliente_end = models.ForeignKey(Cliente,  null=True, on_delete=models.SET_NULL, related_name='Cliente')  
    loja_end = models.OneToOneField(Loja_Celular,  null=True, on_delete=models.SET_NULL, related_name='Loja')  
    
   

    class Meta:   
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        return f"Cidade:{self.cidade} Bairro:{self.bairro}"
    
class Telefone(models.Model):
    ddd = models.CharField("Código de Área", max_length=5)
    numero = models.CharField("Número de Telefone", max_length=15)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete= models.SET_NULL, related_name='telenefone_fornecedor')
    cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL, related_name='telenefone_cliente')
    loja = models.ForeignKey(Loja_Celular, null=True, on_delete= models.SET_NULL, related_name='telenefone_loja')
    funcionario = models.ForeignKey(Funcionario, null=True, on_delete= models.SET_NULL, related_name='telenefone_funcionario')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return f"({self.ddd}) {self.numero}"