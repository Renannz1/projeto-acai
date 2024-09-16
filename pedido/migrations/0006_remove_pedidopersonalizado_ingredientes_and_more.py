# Generated by Django 5.0.7 on 2024-09-16 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0006_acompanhamento_sabor'),
        ('pedido', '0005_pedidopersonalizado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidopersonalizado',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='pedidopersonalizado',
            name='acompanhamentos',
            field=models.ManyToManyField(blank=True, to='ingrediente.acompanhamento'),
        ),
        migrations.AddField(
            model_name='pedidopersonalizado',
            name='sabor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ingrediente.sabor'),
            preserve_default=False,
        ),
    ]