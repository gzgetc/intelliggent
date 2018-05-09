# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labelname', models.CharField(unique=True, max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('headimg', models.ImageField(upload_to=b'aboutcontent')),
                ('bottonadvert', models.ImageField(upload_to=b'aboutcontent')),
            ],
            options={
                'db_table': 'aboutcontent',
            },
        ),
        migrations.CreateModel(
            name='AboutGather',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('images', models.ImageField(upload_to=b'aboutgather')),
                ('content', models.TextField(null=True)),
            ],
            options={
                'db_table': 'aboutgather',
            },
        ),
        migrations.CreateModel(
            name='PhotoDescrib',
            fields=[
                ('imgnumber', models.IntegerField(serialize=False, primary_key=True)),
                ('imgname', models.CharField(unique=True, max_length=20)),
                ('imgtitle', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to=b'photodescrib')),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'photodescrib',
            },
        ),
        migrations.CreateModel(
            name='PhotoLbum',
            fields=[
                ('imgnumber', models.IntegerField(serialize=False, primary_key=True)),
                ('imgname', models.CharField(unique=True, max_length=20)),
                ('imgtitle', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to=b'photolbum')),
            ],
            options={
                'db_table': 'photolbum',
            },
        ),
    ]
