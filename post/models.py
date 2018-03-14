from tkinter import CASCADE
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, Model, DateField, TextField
from django.forms import IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAll(Model):
    email = TextField(null=False, max_length=30)
    login = TextField(null=False, max_length=30)
    password = TextField(null=False, max_length=30)
    birthday = DateField(null=False)
    country = TextField(null=True)
    city = TextField(null=True)

    def __str__(self):
        return '<User email={} login={} password={} birthday={} country={} city={} >'.format(self.email, self.login, self.password, self.birthday, self.country, self.city)


class UserInfo(Model):
    user_fk = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    birthday = DateField(null=False)
    country = TextField(null=True)
    city = TextField(null=True)

    def __str__(self):
        return '<UserInfo birthday={} country={} city={} >'.format(self.birthday, self.country, self.city)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()