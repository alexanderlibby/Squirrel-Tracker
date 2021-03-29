from django.shortcuts import render
from django.shortcuts import get_object_or_404

from sightings.models import Sighting

def index(request):
    sightings_100 = Sighting.objects.all()[:100]
    context = {
            'sightings':sightings_100,
    }
    return render(request, 'map/index.html', context)



# Create your views here.
