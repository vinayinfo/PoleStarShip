# Generated by Django 2.1.5 on 2019-01-29 20:12
import csv
import os
from copy import deepcopy
from django.db import migrations


def setup(apps, schema_editor):
    ShipName = apps.get_model('shiplocation', 'ShipName')
    SheepLocation = apps.get_model('shiplocation', 'ShipLocation')
    os.path.exists('positions.csv')
    for data in csv.DictReader(open('positions.csv')):
        obj, created = ShipName.objects.get_or_create(imo=data['imo'])
        location_data = deepcopy(data)
        location_data['imo'] = obj
        SheepLocation.objects.create(**location_data)


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(setup)
    ]

class Migration(migrations.Migration):

    dependencies = [
        ('shiplocation', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(setup)
    ]