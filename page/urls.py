from django.urls import path
from . import views
from . import customerviews
urlpatterns = [
   path('', views.index, name='home'),
   path('home',views.index),
   path('contact',views.contact),
   path('project',views.project),
   path('gallery',views.gallery),
   path('board',views.board),
   path('services',views.services, name='services'),
   path('signin',views.signin),
   path('about',views.about),
   # customer views
   path('customer/home',customerviews.home),
   path('customer/product',customerviews.product),
]