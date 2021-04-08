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


def add(request):
    return render(request, 'sightings/add.html')

    
