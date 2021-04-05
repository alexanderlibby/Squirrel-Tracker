from django.urls import path, re_path
from . import views

app_name = 'sightings'

urlpatterns = [
    path('sightings/', views.index, name='index'),
    re_path(
        r'^sightings/(?P<input_id>[0-9A-Z]+-[APM]{2}-[0-9]{4}-[0-9]{2})/$', views.details, name='details'),
    # path('map/',views.map, name='map')
]



# '' is what url match (after strip out prior url)
# views.index is what the function will be called
