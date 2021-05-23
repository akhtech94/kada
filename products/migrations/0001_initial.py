# Generated by Django 3.2.3 on 2021-05-23 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('available', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('quality', models.IntegerField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, max_length=25, null=True)),
                ('specification', models.CharField(blank=True, max_length=25, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]
