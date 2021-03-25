from django.db import models
from django.utils.translation import gettext as _

# Create your models here


class Sigthings(models.Model):
    latitude = models.FloatField(
        help_text=_('lat cordinate')
    )
    longitude = models.FloatField(
        help_text=_('lon cordinate')
    )
    unique_squirrel_id = models.CharField(
        max_length=100,
        primary_key=True
    )
    shift = models.CharField(
        max_length=5
    )
    date = models.DateField()  # MMDDYYY in CSV
    age = models.CharField(
        max_length=10,
        blank=True
    )
    primary_fur_color = models.CharField(
        max_length=100,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    specific_location = models.TextField(
        blank=True
    )
    running = models.BooleanField(
        default=False
    )
    chasing = models.BooleanField(
        default=False
    )
    climbing = models.BooleanField(
        default=False
    )
    eating = models.BooleanField(
        default=False
    )
    foraging = models.BooleanField(
        default=False
    )
    other_activities = models.TextField(
        blank=True
    )
    kuks = models.BooleanField(
        default=False
    )
    quaas = models.BooleanField(
        default=False
    )
    moans = models.BooleanField(
        default=False
    )
    tail_flags = models.BooleanField(
        default=False
    )
    tail_twitches = models.BooleanField(
        default=False
    )
    approaches = models.BooleanField(
        default=False
    )
    indifferent = models.BooleanField(
        default=False
    )
    runs_from = models.BooleanField(
        default=False
    )
