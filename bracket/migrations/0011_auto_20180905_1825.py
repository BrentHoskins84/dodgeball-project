# Generated by Django 2.1 on 2018-09-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0010_auto_20180905_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='Tournament',
        ),
        migrations.RemoveField(
            model_name='match',
            name='left_previous',
        ),
        migrations.RemoveField(
            model_name='match',
            name='right_previous',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='winner',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]