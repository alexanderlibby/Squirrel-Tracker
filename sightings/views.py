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

def map(request):
    sightings_100 = Sighting.objects.all()[:100]
    context = {
            'sightings_100': sightings_100,
    }
    return render(request, 'sightings/map.html', context)


