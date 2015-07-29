# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to=b'/static/user_avatar/', blank=True),
        ),
    ]
