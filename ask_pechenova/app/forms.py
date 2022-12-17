from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
# from app.models import Question


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=4, widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data['password']

        if data == 'password':
            raise ValidationError('uncorrected')
        return data


class RegistrationForm(ModelForm):
    password_check = forms.CharField(min_length=4, widget=forms.PasswordInput)

    class Meta:
        # model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def clean(self):
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_check']

        if password_1 != password_2:
            raise ValidationError("Password don't match!")
        return self.cleaned_data


class AskForm(ModelForm):

    title = forms.CharField()
    text = forms.CharField()
    tags = forms.CharField()

    class Meta:
        # model = Question
        fields = ['title', 'text', 'question_tags']