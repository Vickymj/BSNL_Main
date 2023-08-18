from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
	path('home1',views.home1,name='home1'),
	path('booksum',views.booksum),
	path('bss',views.bss),
	path('newbooking',views.newbooking,name='newbooking'),
	path('generate',views.generate),
	path('newbooking',views.newbooking),
	path('receipt',views.receipt,name='receipt'),
	path('login',views.login,name='login'),
	path('confirmletter',views.confirmletter),
	path('project',views.project,name='project'),
	path('update_data/<int:id>',views.update_data, name='update_data'),
	path('delete_data/<str:id>',views.delete_data, name='delete_data'),
    path('test',views.create_receipt, name='test'),
]