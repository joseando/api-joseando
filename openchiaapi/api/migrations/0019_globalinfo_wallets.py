# Generated by Django 3.2.6 on 2021-10-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20210929_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalinfo',
            name='wallets',
            field=models.JSONField(default=dict),
        ),
    ]