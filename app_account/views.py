from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import reverse
from django.views.generic import TemplateView
from .forms import SignInForm


class SignInView(LoginView):
    template_name = 'auth/login.html'
    form_class = SignInForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('siteview:home')


class SignUpView(TemplateView):
    template_name = 'auth/register.html'


class SignOutView(LogoutView):
    template_name = 'auth/logout.html'


class ChangePasswordView(TemplateView):
    template_name = 'auth/change_password.html'
