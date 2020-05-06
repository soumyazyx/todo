from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    path('', include('frontend.urls')),
    path('api/', include('api.urls')),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
