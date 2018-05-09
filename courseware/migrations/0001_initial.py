# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_number', models.IntegerField(serialize=False, primary_key=True)),
                ('c_name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labelname', models.CharField(unique=True, max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('headimg', models.ImageField(upload_to=b'coursecontent')),
                ('bottonadvert', models.ImageField(upload_to=b'coursecontent')),
            ],
            options={
                'db_table': 'coursecontent',
            },
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('d_number', models.CharField(max_length=20)),
                ('d_name', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'directory',
            },
        ),
        migrations.CreateModel(
            name='DirectoryTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('c_name', models.ForeignKey(to='courseware.Course')),
            ],
            options={
                'db_table': 'directorytitle',
            },
        ),
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('s_content', models.TextField(null=True)),
                ('s_coding', models.TextField(null=True)),
                ('s_images', models.ImageField(null=True, upload_to=b'javascoure')),
                ('time', models.DateTimeField()),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'substance',
            },
        ),
        migrations.AddField(
            model_name='directory',
            name='content',
            field=models.ForeignKey(to='courseware.Substance'),
        ),
        migrations.AddField(
            model_name='directory',
            name='directorytitle',
            field=models.ForeignKey(to='courseware.DirectoryTitle'),
        ),
    ]
