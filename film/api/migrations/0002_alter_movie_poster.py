# Generated by Django 4.1.7 on 2023-04-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='film/', verbose_name='Постер'),
        ),
    ]