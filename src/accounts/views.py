# -*- encoding: utf-8 -*-

from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    """Custom login view."""

    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    extra_context = {"title": "Login"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.extra_context["title"]
        return context


class CustomLogoutView(LogoutView):
    """Custom logout view."""

    next_page = "accounts:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Logout"
        return context
