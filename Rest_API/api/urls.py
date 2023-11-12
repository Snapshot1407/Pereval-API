from django.urls import path, include
from .views import *

urlpatterns = [
    # Спринт №1
    path('submitData', PerevalAddAPI.as_view()),
    ]