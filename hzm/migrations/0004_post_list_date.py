# Generated by Django 3.1 on 2020-11-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0003_auto_20201107_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_list',
            name='date',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]