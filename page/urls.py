from django.urls import path
from .views import *

urlpatterns = [
   path('home', index, name='home'),
   path('contact',contact),
   path('project',project),
   path('gallery',gallery),
   path('board',board),
   path('services',services, name='services'),
   path('signin',signin)

]