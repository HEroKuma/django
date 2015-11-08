# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testForeign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(default=b'foreign', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='testList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='testforeign',
            name='ref_list',
            field=models.ForeignKey(to='testdb.testList'),
        ),
    ]
