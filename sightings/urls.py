from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('stats', views.stats),
]

# '' is what url match (after strip out prior url)
# views.index is what the function will be called
