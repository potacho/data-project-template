from django.urls import path

from . import views


urlpatterns = [
	
	path(r'', views.vendor_new, name='vendor_new'),
	    
    # path('list/', views.vendor_list, name='vendor_list'),

    # path(r'vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),

    # path(r'vendor/<int:pk>/edit/', views.vendor_edit, name='vendor_edit'),

    path(r'data/', views.data_view),

    path(r'results/', views.results_view),
]