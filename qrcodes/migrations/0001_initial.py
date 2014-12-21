# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('download_link', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='key_value',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=244)),
                ('value', models.CharField(max_length=244)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ordering',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('key_value_id', models.ForeignKey(to='qrcodes.key_value')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='qr_code',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('qr_code_generated', models.CharField(unique=True, max_length=244)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('width', models.IntegerField(default=100)),
                ('height', models.IntegerField(default=100)),
                ('url', models.TextField()),
                ('label', models.CharField(max_length=244, null=True, blank=True)),
                ('response_text', models.TextField(null=True, blank=True)),
                ('headers', models.TextField(null=True, blank=True)),
                ('publisher_id', models.ForeignKey(to='publisher.publishers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('key_value_id', models.ForeignKey(to='qrcodes.key_value')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='usage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('os', models.CharField(max_length=244, null=True, blank=True)),
                ('location', models.CharField(max_length=244, null=True, blank=True)),
                ('qr_code_id', models.ForeignKey(to='qrcodes.qr_code')),
                ('user_id', models.ForeignKey(to='users.users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ratings',
            name='usage_id',
            field=models.ForeignKey(to='qrcodes.usage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordering',
            name='usage_id',
            field=models.ForeignKey(to='qrcodes.usage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='key_value',
            name='qr_code_id',
            field=models.ForeignKey(to='qrcodes.qr_code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='download',
            name='qr_code_id',
            field=models.ForeignKey(to='qrcodes.qr_code'),
            preserve_default=True,
        ),
    ]
