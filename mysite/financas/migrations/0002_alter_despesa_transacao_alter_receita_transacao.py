# Generated by Django 5.1 on 2024-09-06 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="despesa",
            name="transacao",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="des",
                to="financas.transacao",
            ),
        ),
        migrations.AlterField(
            model_name="receita",
            name="transacao",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rec",
                to="financas.transacao",
            ),
        ),
    ]
