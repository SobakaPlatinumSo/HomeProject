# Generated by Django 3.2.17 on 2023-02-23 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACdb_app', '0002_alter_airconditition_co2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AirConditition',
            new_name='AirCondition',
        ),
    ]
