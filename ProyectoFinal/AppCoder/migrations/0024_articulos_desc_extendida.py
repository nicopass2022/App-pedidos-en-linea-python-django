# Generated by Django 4.0.4 on 2022-04-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0023_alter_clientes_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='desc_extendida',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcion'),
        ),
    ]