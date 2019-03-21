from django import forms
from django.contrib.auth.models import User
from whats_for_dinner.models import *


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
