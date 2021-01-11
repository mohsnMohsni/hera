from django.urls import path
from .views import SignInView, SignUpView, SignOutView, ChangePasswordView

app_name = 'account'

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]
