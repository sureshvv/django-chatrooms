# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=5000)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, related_name='polymorphic_chatrooms.message_set+', null=True, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('allow_anonymous_access', models.NullBooleanField()),
                ('private', models.NullBooleanField()),
                ('password', models.CharField(blank=True, max_length=32)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, related_name='polymorphic_chatrooms.room_set+', null=True, to='contenttypes.ContentType')),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('last_seen_msg_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(to='chatrooms.Room'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
