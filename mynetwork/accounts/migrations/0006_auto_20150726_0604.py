# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20150724_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.CharField(max_length=100, blank=True)),
                ('text', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
