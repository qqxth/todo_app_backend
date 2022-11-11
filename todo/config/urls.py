from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),

    path('api/auth/', include('users.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    path('admin/', admin.site.urls),
]
