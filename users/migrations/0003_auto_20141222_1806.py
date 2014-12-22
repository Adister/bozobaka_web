# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141222_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gplus_users',
            name='user_id',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
