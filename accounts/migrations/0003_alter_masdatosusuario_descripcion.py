# Generated by Django 4.0.6 on 2022-07-31 19:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_masdatosusuario_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuario',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
