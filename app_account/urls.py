from django.urls import path
from .views import SignInView, SignUpView, ActiveEmail, SignOutView, ChangePasswordView, UserProfile

app_name = 'account'

urlpatterns = [
    path('profile/', UserProfile.as_view(), name='user_profile'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('active_email/<uidb64>/<token>/', ActiveEmail.as_view(), name='active'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]
