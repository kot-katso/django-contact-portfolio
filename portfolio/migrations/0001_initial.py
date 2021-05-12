# Generated by Django 3.2.2 on 2021-05-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=450)),
            ],
        ),
    ]
