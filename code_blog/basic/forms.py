from django import forms
from .models import codes

class CodeForm(forms.ModelForm):
    
    class Meta():
        model = codes
        fields = ('author', 'title', 'text')