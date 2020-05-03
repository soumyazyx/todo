from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
]
