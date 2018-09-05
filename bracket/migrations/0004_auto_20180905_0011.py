# Generated by Django 2.1 on 2018-09-04 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0003_auto_20180905_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('current_round', models.IntegerField(default=0)),
                ('rounds', models.IntegerField(default=0)),
                ('icon', models.ImageField(blank=True, upload_to='static/icons', verbose_name='image')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='tournament', to='bracket.Tournament'),
            preserve_default=False,
        ),
    ]