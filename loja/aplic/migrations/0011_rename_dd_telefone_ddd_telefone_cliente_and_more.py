# Generated by Django 4.2.7 on 2023-11-24 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0010_telefone_remove_cliente_endereco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefone',
            old_name='dd',
            new_name='ddd',
        ),
        migrations.AddField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telenefone_cliente', to='aplic.cliente'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telenefone_fornecedor', to='aplic.fornecedor'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telenefone_funcionario', to='aplic.funcionario'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='loja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telenefone_loja', to='aplic.loja_celular'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(max_length=50, verbose_name='Telefone'),
        ),
    ]
