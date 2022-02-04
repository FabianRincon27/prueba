from django.urls import path
from bill import views

urlpatterns = [
    path('bill', views.bill_list),
    path('bill/<int:pk>', views.bill_detail),
]