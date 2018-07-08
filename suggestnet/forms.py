from django import forms
from .models import Suggest_input


class Suggest_Form(forms.ModelForm):

    class Meta:
        model = Suggest_input
        fields='__all__'#('title','text','date')
