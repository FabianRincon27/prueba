from django.urls import path
from client import views

urlpatterns = [
    path('client', views.client_list),
    path('client/<int:pk>', views.client_detail),
    path('client/download/<int:pk>/', views.client_download),
    path('client/massive/', views.client_massive)
]