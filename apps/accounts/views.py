from .forms import SignInForm, SignUpForm, ChangePasswordForm, AddAddressForm, EditProfileForm
from django.views.generic import CreateView, FormView, RedirectView, TemplateView, UpdateView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse, redirect, render
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.http import HttpResponse
from apps.orders.models import Cart
from .models import User


class SignInView(LoginView):
    form_class = SignInForm
    redirect_authenticated_user = True
    template_name = 'account/auth/login.html'

    def get_success_url(self):
        return reverse('siteview:home')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/auth/register.html'

    def form_valid(self, form):
        """
        If form is valid, hash password and save user then send mail to
        user.email field that user had enter to validate email and active user
        """
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        Cart.objects.create(user=obj)
        current_site = get_current_site(self.request)
        mail_subject = _('Active your shop account.')
        message = render_to_string('account/auth/email-confirm/active_email.html', {
            'user': obj,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
            'token': account_activation_token.make_token(obj),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        # email.send()
        return render(self.request, 'account/auth/email-confirm/email_response.html')


class ActiveEmail(RedirectView):
    """
    A link has been sent to user with valid token and if user click on it
    this function run and get token from url and check it,
    if it is valid make True the user.is_active field and make active the user.
    """

    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(self.kwargs.get('uidb64')))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        activation_token = account_activation_token.check_token(user, self.kwargs.get('token'))
        if user is not None and activation_token:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('siteview:home')
        else:
            return HttpResponse(_('Activation link is invalid!'))


class SignOutView(LogoutView):
    template_name = 'account/auth/logout.html'


class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'account/auth/change_password.html'

    def form_valid(self, form):
        """
        If form is valid get user and set new password,
        at the end redirect to home.
        """
        user = self.request.user
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect('siteview:home')


class UserProfile(TemplateView):
    template_name = 'account/user-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = self.request.user.address.all()
        context['order_list'] = self.request.user.cart.order.all()
        return context


class AddAddress(LoginRequiredMixin, FormView):
    form_class = AddAddressForm
    template_name = 'account/add-address.html'

    def form_valid(self, form):
        valid_form = form.save(commit=False)
        valid_form.user = self.request.user
        valid_form.save()
        return super().form_valid(valid_form)

    def get_success_url(self):
        return reverse('account:user_profile')


class EditProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'account/edit-profile.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get()

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('account:user_profile')
