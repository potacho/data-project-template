from django.urls import path

from . import views


urlpatterns = [

    path('', views.vendor_list, name='vendor_list'),

    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),

    path(r'vendor/new/', views.vendor_new, name='vendor_new'),

    path('vendor/<int:pk>/edit/', views.vendor_edit, name='vendor_edit'),
]