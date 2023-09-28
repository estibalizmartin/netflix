from django.urls import path
from .views import NetflixAPI

urlpatterns = [
    path('', NetflixAPI.as_view())
]