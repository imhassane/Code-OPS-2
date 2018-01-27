from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

# Nom du namespace.
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

