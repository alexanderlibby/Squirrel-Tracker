from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Sighting

# Create your views here.


def index(request):
    """
    A view that lists all squirrel sightings with links to view each sighting
        Located at: /sightings
        Methods Supported: GET
        Fields to show:
        - Unique Squirrel ID
        - Date
        - Link to unique squirrel sighting
        - This view should also have a single link to the “add” sighting view
    """
    sightings_all = Sighting.objects.all()
    context = {
        'sightings': sightings_all
    }
    return render(request, 'sightings/index.html', context)


def details(request, unique_squirrel_id):
    
    str(unique_squirrel_id)
    return render(request, 'sighting/')

def stats(request):
    sightings = Sighting.objects.all()

    shift_AM = sightings.filter(shift='AM').count()
    shift_PM = sightings.filter(shift='PM').count()

    shift_AM_pct = shift_AM / (shift_AM + shift_PM)
    shift_PM_pct = shift_PM / (shift_AM + shift_PM)


    age_Adult = sightings.filter(age='Adult').count()
    age_Juvenile = sightings.filter(age='Juvenile').count()

    age_Adult_pct = age_Adult / (age_Adult + age_Juvenile)
    age_Juvenile_pct = age_Juvenile / (age_Adult + age_Juvenile)

    running_true = sightings.filter(running=True).count()
    running_false = sightings.filter(running=False).count()

    running_pct = running_true / (running_true + running_false)

    eating_true = sightings.filter(eating=True).count()
    eating_false = sightings.filter(eating=False).count()
    
    eating_pct = eating_true / (eating_true + eating_false)

    climbing_true = sightings.filter(climbing=True).count()
    climbing_false = sightings.filter(climbing=False).count()
    
    climbing_pct = climbing_true / (climbing_true + climbing_false)

    context = {
            'shift_AM_pct': shift_AM_pct, 
            'shift_PM_pct': shift_PM_pct,
            'age_Adult_pct': age_Adult_pct,
            'age_Juvenile_pct': age_Juvenile_pct,
            'running_pct': running_pct,
            'eating_pct': eating_pct,
            'climbing_pct': climbing_pct,
    }
    return render(request, 'sightings/stats.html', context)
