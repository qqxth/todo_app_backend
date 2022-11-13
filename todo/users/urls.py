from django.urls import path
from .views import UserTokenObtainPairView

app = 'users'

urlpatterns = [
    path('jwt/create/', UserTokenObtainPairView.as_view()),
]
