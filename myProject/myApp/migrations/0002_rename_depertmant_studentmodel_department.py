# Generated by Django 5.0.1 on 2024-01-29 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='depertmant',
            new_name='Department',
        ),
    ]
