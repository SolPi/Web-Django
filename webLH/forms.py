from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
            'psw': forms.PasswordInput(render_value=False),
        }
        fields ="__all__"