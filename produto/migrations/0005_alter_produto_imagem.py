# Generated by Django 5.0.7 on 2024-09-17 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/produtos/'),
        ),
    ]
