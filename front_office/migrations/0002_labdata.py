# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front_office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BloodGlucoseRange', models.IntegerField(default=0)),
                ('BloodPressure', models.IntegerField(default=0)),
                ('HeartRates', models.IntegerField(default=0)),
                ('SkinThikness', models.FloatField(default=0)),
                ('PragnencyParYear', models.IntegerField(default=0)),
                ('Diabetes', models.IntegerField(default=0)),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_office.Pdata')),
            ],
        ),
    ]