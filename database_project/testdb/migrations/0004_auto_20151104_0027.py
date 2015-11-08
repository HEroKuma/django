# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0003_auto_20151104_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testlist',
            options={'permissions': (('can_watch', 'Can_watch'),)},
        ),
    ]
