# Generated by Django 4.1 on 2022-09-12 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='filtro',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lingua',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]