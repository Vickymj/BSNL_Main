from django.urls import path
from . import views
urlpatterns = [
	path('',views.home),
	path('booksum',views.booksum),
	path('bss',views.bss),
	path('newbooking',views.newbooking,name='newbooking'),
	path('generate',views.generate),
	path('newbooking',views.newbooking),
	path('receipt',views.receipt),
	path('login',views.login),
	path('project',views.project),
]