from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/signin.html'))
    # We use auth_views.LoginView.as_view() to specify the view for handling login.
]