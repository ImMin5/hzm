# Generated by Django 3.1 on 2020-11-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0008_auto_20201109_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_list',
            old_name='post_passwd',
            new_name='passwd',
        ),
        migrations.AlterField(
            model_name='post_list',
            name='result',
            field=models.BooleanField(default=True),
        ),
    ]
