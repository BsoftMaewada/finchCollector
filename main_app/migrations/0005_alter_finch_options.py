# Generated by Django 4.1.dev20210929182329 on 2021-10-09 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_finch_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finch',
            options={'ordering': ['name']},
        ),
    ]
