# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=5000)),
                ('polymorphic_ctype', models.ForeignKey(null=True, related_name='polymorphic_chatrooms.message_set+', editable=False, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('allow_anonymous_access', models.NullBooleanField()),
                ('private', models.NullBooleanField()),
                ('password', models.CharField(max_length=32, blank=True)),
                ('polymorphic_ctype', models.ForeignKey(null=True, related_name='polymorphic_chatrooms.room_set+', editable=False, to='contenttypes.ContentType')),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
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
