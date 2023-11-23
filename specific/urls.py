from specific.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
    path('mubi/',mubi,name='mubi'),
    path('krish/',krish,name='krish'),
]