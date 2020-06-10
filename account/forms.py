from django import forms

class LoginForm(forms.Form):
    Логин = forms.CharField()
    Пароль = forms.CharField(widget=forms.PasswordInput)
