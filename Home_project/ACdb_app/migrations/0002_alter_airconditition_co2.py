# Generated by Django 3.2.17 on 2023-02-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACdb_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airconditition',
            name='CO2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
