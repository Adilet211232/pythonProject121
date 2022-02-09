# Generated by Django 4.0.2 on 2022-02-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('genre', models.CharField(choices=[('Detective', 'Detective'), ('Comedy', 'Comedy'), ('Drama', 'Drama')], max_length=100)),
                ('data_filmed', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
