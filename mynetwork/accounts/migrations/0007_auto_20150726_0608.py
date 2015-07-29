# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150726_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
