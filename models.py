from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


# Create your models here.


class Ownable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(Group)

    class Meta:
        abstract = True


class Sortable(models.Model):
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Publishable(models.Model):
    published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Approveable(models.Model):
    approved = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Shareable(models.Model):
    # https://megatags.co/

    class Meta:
        abstract = True
