# Generated by Django 3.0.6 on 2020-05-18 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multichoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ('-Q_No',)},
        ),
    ]
