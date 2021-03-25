from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

# '' is what url match (after strip out prior url)
# views.index is what the function will be called
