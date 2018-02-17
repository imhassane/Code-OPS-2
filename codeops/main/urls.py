from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('careers/', CareerList.as_view(), name='careers'),
    path('paths/<int:career_pk>', PathList.as_view(), name='paths'),
    path('courses/<int:path_pk>', CourseList.as_view(), name='courses'),
    path('parts/<slug:course_slug>', PartList.as_view(), name='parts'),

    path('new_career/<str:username>/<int:career_pk>/', career_redirect, name='new_career'),
    path('new_path/<str:username>/<int:path_pk>/', path_redirect, name='new_path'),
    path('new_course/<str:username>/<slug:course_slug>', course_redirect, name='new_course'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
]

