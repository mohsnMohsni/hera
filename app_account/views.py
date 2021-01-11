from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import reverse, redirect, render
from django.views.generic import CreateView, FormView
from .forms import SignInForm, SignUpForm, ChangePasswordForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import login
from .models import User
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import ugettext_lazy as _


class SignInView(LoginView):
    template_name = 'auth/login.html'
    form_class = SignInForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('siteview:home')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'auth/register.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        current_site = get_current_site(self.request)
        mail_subject = _('Active your shop account.')
        message = render_to_string('auth/email-confirm/active_email.html', {
            'user': obj,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
            'token': account_activation_token.make_token(obj),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(self.request, 'auth/email-confirm/email_response.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('blog:home')
    else:
        return HttpResponse(_('Activation link is invalid!'))


class SignOutView(LogoutView):
    template_name = 'auth/logout.html'


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'auth/change_password.html'

    def form_valid(self, form):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk'))
        except User.DoesNotExist:
            return HttpResponse(status=404)
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        return redirect('siteview:home')
