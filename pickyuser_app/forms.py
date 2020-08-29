from django import forms
from pickyuser_app.models import CustomUserMod
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # https://docs.djangoproject.com/en/3.1/topics/auth/default/


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):

    class Meta:
        model = CustomUserMod
        fields = ['username', 'password', 'homepage', 'display_name', 'age']


class AdminForm(forms.ModelForm):

    class Meta:
        model = CustomUserMod
        fields = ['username', 'password', 'homepage', 'display_name', 'age']
