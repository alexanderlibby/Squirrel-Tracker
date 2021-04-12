from django.forms import ModelForm
from .models import Sighting


class EditSightingForm(ModelForm):
    """
    Update the sighting in the database

    Support fields
    - Latitude
    - Longitude
    - Shift
    - Date
    - Age
    """
    class Meta:
        model = Sighting
        # this form will look for the fields below when loading the payload from POST
        # fields = '__all__'
        fields = {
            "unique_squirrel_id",
            "latitude",
            "longitude",
            "shift",
            "date",
            "age"
        }

class AddSighting(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
