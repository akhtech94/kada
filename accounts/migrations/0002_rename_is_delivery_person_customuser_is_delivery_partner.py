# Generated by Django 3.2.3 on 2021-05-23 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_delivery_person',
            new_name='is_delivery_partner',
        ),
    ]