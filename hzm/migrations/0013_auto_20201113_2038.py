# Generated by Django 3.1.3 on 2020-11-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0012_auto_20201110_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_list',
            name='player_num',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
