# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0003_differnt_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='type',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
