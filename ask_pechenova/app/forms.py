from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, widgets
from .models import Question, Answer


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
    class Meta:
        model = Question
        fields = ['title', 'text', 'question_tags']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Title name'
            }),
            "text": TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Question text'
            }),
            "question_tags": TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Tags'
            })
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']