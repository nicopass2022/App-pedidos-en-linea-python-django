# Generated by Django 4.0.3 on 2022-04-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_alter_pedido_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.CharField(max_length=50, verbose_name='fecha'),
        ),
    ]
