from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('careers/', login_required(CareerList.as_view()), name='careers'),
    path('paths/<int:career_pk>', login_required(PathList.as_view()), name='paths'),
    path('courses/<int:path_pk>', login_required(CourseList.as_view()), name='courses'),

    path('new_career/<str:username>/<int:career_pk>/', career_redirect, name='new_career'),
    path('new_path/<str:username>/<int:path_pk>/', path_redirect, name='new_path'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
]

