from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import EditSightingForm

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


def details(request, input_id):
    """
    A view that show a detail of a sighting and allow edits

        - Latitude
        - Longitude
        - Unique Squirrel ID
        - Shift
        - Date
        - Age
    """
    if request.method == 'GET':
        # fetch the object using input_id
        squirrel = get_object_or_404(Sighting, pk=input_id)
        form = EditSightingForm(None, instance=squirrel)
        context = {
            'squirrel': squirrel,
            'mode': 'You can edit the sighting details below by changing the text and click save.',
            'form': form
        }
        return render(request, 'sightings/details_with_form.html', context)

    if request.method == 'POST':
        # request.POST is the dictionary of payload we got from the POST
        squirrel = get_object_or_404(Sighting, pk=input_id)
        form = EditSightingForm(request.POST, instance=squirrel)
        input_id = request.POST.get('unique_squirrel_id')
        # Data validation will happen in EditSightingForm
        if form.is_valid():
            # The one who modify the database is form, not
            form.save()
            # squirrel = get_object_or_404(Sighting, pk=input_id)
            context = {
                'squirrel': squirrel,
                'mode': 'Saved your changes',
                'form': form
            }
            return render(request, 'sightings/details_with_form.html', context)
        else:
            # status=400
            context = {
                'squirrel': squirrel,
                'mode': 'Some fields are not in the correct format. Please try again.',
                'form': form
            }
            return render(request, 'sightings/details_with_form.html', context)


def map_view(request):
    sightings_100 = Sighting.objects.all()[:100]
    context = {
            'sightings':sightings_100,
    }
    return render(request, 'sightings/map.html', context)

