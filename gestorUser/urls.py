from django.urls import path, include

from gestorUser.views import SingupView

urlpatterns = [
    path("signup/", SingupView.as_view(), name="signup")
    ]