# Generated by Django 4.0.2 on 2022-02-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='data_filmed',
            field=models.DateField(auto_now_add=True),
        ),
    ]