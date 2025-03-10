from django.urls import path
from .views import UserRegisterationView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name='Register'),
    path('login/', UserLoginView.as_view(), name="Login")
]
