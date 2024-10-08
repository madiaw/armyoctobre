from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('stock/', include('stock.urls')),
    path('auth/', include('authentication.urls')),
]