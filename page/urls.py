from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='home'),
   path('home',index),
   path('contact',contact),
   path('project',project),
   path('gallery',gallery),
   path('board',board),
   path('services',services, name='services'),
   path('signin',signin),
   path('about',about),
   path('test',test),
]