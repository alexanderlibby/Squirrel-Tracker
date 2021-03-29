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


def detail(request, input_id):
    """
    A view that show a detail of a sighting

        - Latitude
        - Longitude
        - Unique Squirrel ID
        - Shift
        - Date
        - Age
    """
    squirrel = get_object_or_404(Sighting, pk=input_id)
    context = {
        'squirrel': squirrel
    }
    return render(request, 'sightings/detail.html', context)
