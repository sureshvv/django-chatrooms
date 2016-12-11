# encoding=utf8

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from polymorphic.models import PolymorphicModel


class Room(PolymorphicModel):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField()
    description = models.TextField()
    subscribers = models.ManyToManyField(User, blank=True)
    allow_anonymous_access = models.NullBooleanField()
    private = models.NullBooleanField()
    password = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('room_view', kwargs=dict(slug=self.slug))


class Message(PolymorphicModel):
    user = models.ForeignKey(User, null=True)
    # username field is useful to store guest name of unauthenticated users
    username = models.CharField(max_length=50)
    date = models.DateTimeField()
    room = models.ForeignKey(Room)
    content = models.CharField(max_length=5000)


class UserSettings(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    last_seen_msg_id = models.IntegerField(default=0)
