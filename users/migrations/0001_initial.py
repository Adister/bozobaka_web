# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fb_users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('secondary_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=6, null=True, blank=True)),
                ('location', models.CharField(default=b'mumbai', max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('image_url', models.TextField()),
                ('profile_url', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('mobile_os', models.CharField(default=b'android', max_length=20, null=True)),
                ('os_version', models.CharField(max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gplus_users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('secondary_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=10, null=True, blank=True)),
                ('location', models.CharField(default=b'mumbai', max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('image_url', models.TextField()),
                ('profile_url', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('mobile_os', models.CharField(default=b'android', max_length=20, null=True)),
                ('os_version', models.CharField(max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254, unique=True, null=True)),
                ('gplus_id', models.IntegerField()),
                ('fb_id', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
