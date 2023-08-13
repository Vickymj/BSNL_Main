from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('all',customer_details)
]