# Generated by Django 2.0.5 on 2018-09-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=100)),
                ('season', models.CharField(default='season', max_length=100)),
                ('flowers', models.CharField(default='flowers', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
