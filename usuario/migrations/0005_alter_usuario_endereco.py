# Generated by Django 5.0.7 on 2024-09-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_usuario_nome_alter_usuario_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.TextField(max_length=255),
        ),
    ]
