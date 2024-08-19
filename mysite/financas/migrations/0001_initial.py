# Generated by Django 5.1 on 2024-08-16 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Balancete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do balancete')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data de criação do balancete')),
                ('saldo', models.FloatField(default=0, verbose_name='Saldo total do balancete')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('transacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financas.transacao')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome da despesa')),
                ('valor', models.FloatField(verbose_name='Valor da despesa')),
                ('boleto', models.ImageField(height_field='30', null=True, unique=True, upload_to='', verbose_name='Foto do boleto da despesa', width_field='10')),
                ('balancete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financas.balancete')),
            ],
            bases=('financas.transacao',),
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('transacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financas.transacao')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome da receita')),
                ('valor', models.FloatField(verbose_name='Valor da receita')),
                ('boleto', models.ImageField(height_field='30', null=True, unique=True, upload_to='', verbose_name='Foto do boleto da receita', width_field='10')),
                ('balancete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financas.balancete')),
            ],
            bases=('financas.transacao',),
        ),
    ]