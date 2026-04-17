from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserLoginView, email_verification

from . import views

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView, name="logout"),
    path("email-confurm/<str:token>/", email_verification, name="email-confirm"),
]
