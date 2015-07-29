# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150724_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True),
        ),
    ]
