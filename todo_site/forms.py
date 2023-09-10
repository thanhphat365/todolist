from django import forms
from .models import User
class Userform(forms.Models.Form):
    class Meta:
        model = User
        fileds = '__all__'