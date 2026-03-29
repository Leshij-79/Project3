from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class CustomUserCreateView(View):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("catalog:product_list")
