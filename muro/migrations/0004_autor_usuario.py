# Generated by Django 4.0.6 on 2022-08-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0003_autor_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='usuario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]