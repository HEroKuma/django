# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_auto_20151103_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testlist',
            options={'permissions': (('can_watch', 'Can_watch'), ('cant_watch', 'Cant_watch'))},
        ),
    ]
