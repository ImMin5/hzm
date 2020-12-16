# Generated by Django 3.1.4 on 2020-12-15 20:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0007_club_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='blue_player_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='match',
            name='red_player_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True), blank=True, null=True, size=None),
        ),
    ]
