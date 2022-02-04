from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('', include('bill.urls')),
    path('', include('product.urls')),
    path('', include('billProduct.urls')),
    path('', include('user.urls')),
]
