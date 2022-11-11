from django.urls import path
from .views import UserTokenObtainPairView

app = 'users'

urlpatterns = [
    path('create-token/', UserTokenObtainPairView.as_view())
]
