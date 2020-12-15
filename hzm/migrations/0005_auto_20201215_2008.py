# Generated by Django 3.0 on 2020-12-15 11:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0004_auto_20201215_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='blue_p1_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p2_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p3_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p4_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p5_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p6_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p7_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='blue_p8_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='club',
        ),
        migrations.RemoveField(
            model_name='match',
            name='club_blue',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map10',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map11',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map12',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map13',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map14',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map3',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map4',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map5',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map6',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map7',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map8',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_map9',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p1_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p2_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p3_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p4_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p5_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p6_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p7_name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='red_p8_name',
        ),
        migrations.AddField(
            model_name='match',
            name='blue_player_name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=12, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='match',
            name='club_blue_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='club_red_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='match_map',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='match',
            name='red_player_name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=12, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='match',
            name='blue_goga_avg',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_time_end',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_time_start',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='red_goga_avg',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]