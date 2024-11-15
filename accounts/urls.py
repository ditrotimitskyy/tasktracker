from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path("accounts/signup/", UserCreateView.as_view(), name="signup")
]