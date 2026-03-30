import secrets

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomAuthenticationForm, CustomUserCreationForm
from users.models import CustomUser


class RegisterView(FormView):
    model = CustomUser
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user) # Оставлено на очень долгую память как способ автологина
        # self.send_welcome_email(user.email) # Оставлено на очень долгую память как способ автописьма

        user.is_active = False
        token = secrets.token_hex(16)  # 16 - шкала чисел
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/email-confurm/{token}/"
        send_mail(
            subject="Авторизация на сайте",
            message=f"Для завершения регистрации перейдите по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)

    # Оставлено на долгую память
    # def send_welcome_email(self, user_email):
    #     subject = 'Добро пожаловать в наш сервис'
    #     message = 'Спасибо, что зарегистрировались в нашем сервисе!'
    #     recipient_list = [user_email]
    #     send_mail(subject, message, recipient_list)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("catalog:product_list")


def UserLogoutView(request):
    logout(request)
    return redirect("catalog:product_list")
