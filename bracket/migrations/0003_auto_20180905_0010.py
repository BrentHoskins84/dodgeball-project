# Generated by Django 2.1 on 2018-09-04 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0002_auto_20180905_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]