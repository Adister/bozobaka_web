# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gplus_users',
            name='user_id',
            field=models.CharField(unique=True, max_length=101),
            preserve_default=True,
        ),
    ]
