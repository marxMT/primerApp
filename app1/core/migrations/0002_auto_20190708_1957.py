# Generated by Django 2.2.2 on 2019-07-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicios',
            old_name='tipo',
            new_name='servicio',
        ),
    ]
