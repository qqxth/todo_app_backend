from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.base')),

    path('admin/', admin.site.urls),
]
