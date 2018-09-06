# Generated by Django 2.1 on 2018-09-05 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0007_remove_match_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_round',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='bracket.Tournament'),
        ),
    ]