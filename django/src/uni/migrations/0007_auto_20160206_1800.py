# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0006_universitydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='college',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='form_data', to='uni.UniversityData'),
        ),
    ]