# Generated by Django 3.2.17 on 2023-02-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirConditition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=100)),
                ('CO2', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
