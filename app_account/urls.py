from django.urls import path
from .views import SignInView, SignUpView, SignOutView, ChangePasswordView, activate

app_name = 'account'

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('active_email/<uidb64>/<token>/', activate, name='active'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password')
]
