# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150403_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='nom',
        ),
    ]
