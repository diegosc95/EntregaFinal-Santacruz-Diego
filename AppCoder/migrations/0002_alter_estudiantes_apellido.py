# Generated by Django 5.0.2 on 2024-03-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='apellido',
            field=models.CharField(max_length=60),
        ),
    ]