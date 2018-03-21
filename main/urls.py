from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Pour les carrières.
    path('careers/', CareerList.as_view(), name='careers'),
    path('career/<slug:slug>/', CareerDetail.as_view(), name='career'),

    # Pour les parcours.
    path('paths/<int:career_pk>', PathList.as_view(), name='paths'),
    path('path/<slug:slug>/', PathDetail.as_view(), name='path'),

    # Pour les cours.
    path('courses/<int:path_pk>', CourseList.as_view(), name='courses'),
    path('course/<slug:slug>/', CourseDetail.as_view(), name='course'),

    # Pour les parties.
    path('parts/<slug:course_slug>', PartList.as_view(), name='parts'),
    path('part/<slug:part_slug>/<int:pk>/', PartDetail.as_view(), name='part'),

    # Pour le formulaire de recherche.
    path('search/', search, name='search'),

    path('new_career/<int:career_pk>/', login_required(career_redirect), name='new_career'),
    path('new_path/<slug:slug>/<int:career_pk>/', login_required(path_redirect), name='new_path'),
    path('new_course/<slug:course_slug>/<int:path_pk>/', login_required(course_redirect), name='new_course'),

    path('dashboard/', dashboard, name='dashboard'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
]
