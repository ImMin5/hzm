# Generated by Django 3.1 on 2020-11-10 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0011_auto_20201110_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_passwd',
            new_name='passwd',
        ),
    ]