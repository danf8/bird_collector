# Generated by Django 4.1.7 on 2023-04-10 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_feedings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedings',
            new_name='Feeding',
        ),
    ]
