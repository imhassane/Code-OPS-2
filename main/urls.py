from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', home, name='home'),

    # Pour les carrières.
    path('careers/', CareerList.as_view(), name='careers'),
    path('career/<slug:slug>/', CareerDetail.as_view(), name='career'),

    # Pour les parcours.
    path('paths/', PathList.as_view(), name='paths'),
    path('path/<slug:slug>/', PathDetail.as_view(), name='path'),

    # Pour les cours.
    path('courses/', CourseList.as_view(), name='courses'),
    path('course/<slug:slug>/', CourseDetail.as_view(), name='course'),

    # Pour le formulaire de recherche.
    path('search/', search, name='search'),

    path('new_course/<slug:slug>/', login_required(course_redirect), name='new_course'),

    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
]
