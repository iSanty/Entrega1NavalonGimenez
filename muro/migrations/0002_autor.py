# Generated by Django 4.0.6 on 2022-08-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
