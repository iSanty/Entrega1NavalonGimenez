# Generated by Django 4.0.6 on 2022-07-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masdatosusuario',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
