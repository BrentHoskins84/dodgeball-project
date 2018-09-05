# Generated by Django 2.1 on 2018-09-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0005_auto_20180905_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('BYE', 'BYE'), ('Not Scheduled', 'Not Scheduled'), ('Scheduled', 'Scheduled'), ('Finished', 'Finished')], default='Not Scheduled', max_length=20),
        ),
    ]
