# Generated by Django 3.1.7 on 2021-03-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sigthings',
            fields=[
                ('latitude', models.FloatField(help_text='lat cordinate')),
                ('longitude', models.FloatField(help_text='lon cordinate')),
                ('unique_squirrel_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('shift', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('age', models.CharField(blank=True, max_length=10)),
                ('primary_fur_color', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('specific_location', models.TextField(blank=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.TextField(blank=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]
