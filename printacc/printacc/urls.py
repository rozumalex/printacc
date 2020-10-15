from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import urls

swagger_pattern = [
    path('', include('accounts.urls', namespace='api')),
]

schema_view = get_swagger_view(title='Pastebin API', patterns=swagger_pattern)

urlpatterns = [
    path('', include('accounts.urls', namespace='api')),
    path('auth/', include(urls, namespace='auth')),
    path('swagger/', schema_view, name='openapi'),
    path('admin/', admin.site.urls)
]
