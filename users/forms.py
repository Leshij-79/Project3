from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms

from catalog.forms import StyleFormMixin
from users.models import CustomUser


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar', 'country')


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')

        return phone_number


class CustomAuthenticationForm(StyleFormMixin, AuthenticationForm):
    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ('username', 'password')
