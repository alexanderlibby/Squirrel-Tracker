from django.urls import path, re_path
from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index),
    re_path(
        r'^(?P<input_id>[0-9A-Z]+-[APM]{2}-[0-9]{4}-[0-9]{2})/$', views.detail, name='detail'),
]

# '' is what url match (after strip out prior url)
# views.index is what the function will be called
