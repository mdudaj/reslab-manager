# -*- encoding: utf-8 -*-

from django.urls import path

from .views import CustomLoginView, CustomLogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
