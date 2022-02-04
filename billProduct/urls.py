from django.urls import path
from billProduct import views

urlpatterns = [
    path('billProduct', views.billProduct_list),
    path('billProduct/<int:pk>', views.billProduct_detail),
]