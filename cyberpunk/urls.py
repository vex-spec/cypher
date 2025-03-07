
import django.contrib
from django.urls import path,include

urlpatterns = [
    path('', include('cyberpunkapp.urls')),
]
