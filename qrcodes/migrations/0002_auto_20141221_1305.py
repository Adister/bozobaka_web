# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='download_link',
            field=models.URLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='qr_code_id',
            field=models.ForeignKey(to='qrcodes.qr_code', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qr_code',
            name='url',
            field=models.URLField(max_length=244),
            preserve_default=True,
        ),
    ]
