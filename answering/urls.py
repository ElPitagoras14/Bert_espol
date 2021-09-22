from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('', pregunta),
]