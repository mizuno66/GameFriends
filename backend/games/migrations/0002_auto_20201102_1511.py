# Generated by Django 3.1 on 2020-11-02 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='gamegenres',
            table='game_genres',
        ),
        migrations.AlterModelTable(
            name='gameinfos',
            table='game_infos',
        ),
    ]
