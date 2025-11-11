################################################
"""
URL configuration for app project.
"""
################################################
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from utils.homepage import HomePageView
from utils.healthcheck import healthz
from helpers.api_base import BASE_API

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path(f"{BASE_API}/pages/", include('api.pages.urls')),
    path(f"{BASE_API}/homepage/", include('api.homepage.urls')),
    path(f"{BASE_API}/configuration/", include('api.configuration.urls')),
    path(f"{BASE_API}/feature/", include('api.features.urls')),
    path('healthz/', healthz),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
