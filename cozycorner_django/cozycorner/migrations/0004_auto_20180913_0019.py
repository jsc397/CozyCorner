# Generated by Django 2.0.5 on 2018-09-13 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozycorner', '0003_auto_20180913_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='flowers',
            field=models.CharField(default='flowers', max_length=100),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='season',
            field=models.CharField(default='season', max_length=100),
        ),
    ]