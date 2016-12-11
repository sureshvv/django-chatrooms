# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('username', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('last_seen_msg_id', models.IntegerField(default=0)),
            ],
        ),
    ]
