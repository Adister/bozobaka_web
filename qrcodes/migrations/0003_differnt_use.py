# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('qrcodes', '0002_auto_20141221_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='differnt_use',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('qr_code_recieved', models.CharField(max_length=244)),
                ('date_added', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('os', models.CharField(max_length=244, null=True, blank=True)),
                ('location', models.CharField(max_length=244, null=True, blank=True)),
                ('user_id', models.ForeignKey(to='users.users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
