from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # phone_number = forms.CharField(max_length=15, required=False,
    #                                help_text='Необязательное поле. Введите ваш номер телефона.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        exclude = (
            "is_staff",
            "is_active",
            "is_superuser",
        )

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #
    #     if phone_number and not phone_number.isdigit():
    #         raise forms.ValidationError('Номер телефона должен содержать только цифры.')
    #
    #     return phone_number


class CustomAuthenticationForm(AuthenticationForm):
    pass