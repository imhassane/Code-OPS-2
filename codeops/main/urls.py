from django.urls import path
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('careers/', CareerList.as_view(), name='careers'),
    path('paths/', PathList.as_view(), name='paths'),
]


