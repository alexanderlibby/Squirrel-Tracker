from django.db import models
from django.utils.translation import gettext as _

# Create your models here


class Sighting(models.Model):
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

    # AM = _('AM')
    # PM = _('PM')
    # SHIFT_CHOICES = [AM, PM]
    shift = models.CharField(
        max_length=5,
        help_text=_('AM or PM')
        # choices=SHIFT_CHOICES
    )

    date = models.DateField()  # MMDDYYY in CSV
    # ADULT = _('Adult')
    # JUVENILE = _('Juvenile')
    # BLANK = _('')
    # AGE_OPTIONS = [ADULT, JUVENILE, BLANK]
    age = models.CharField(
        max_length=10,
        blank=True,
        help_text=_('Adult or Juvenile')
        # choices=AGE_OPTIONS
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

    def __str__(self):
        return self.unique_squirrel_id
