from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from users.forms import CustomUserCreationForm, CustomAuthenticationForm
from users.models import CustomUser


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user) # Оставлено на очень долгую память как способ автологина
        # self.send_welcome_email(user.email)
        return super().form_valid(form)

    # def send_welcome_email(self, user_email):
    #     subject = 'Добро пожаловать в наш сервис'
    #     message = 'Спасибо, что зарегистрировались в нашем сервисе!'
    #     recipient_list = [user_email]
    #     send_mail(subject, message, recipient_list)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('catalog:product_list')

