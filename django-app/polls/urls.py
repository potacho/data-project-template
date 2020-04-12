from django.urls import path

from . import views


urlpatterns = [

    path('', views.vendor_list, name='vendor_list'),

    path(r'vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),

    path(r'vendor/new/', views.vendor_new, name='vendor_new'),

    path(r'vendor/<int:pk>/edit/', views.vendor_edit, name='vendor_edit'),

    path(r'vendor/button/', views.button),

    path(r'output/', views.vendor_button, name='script'),

    path(r'external/', views.external),
]