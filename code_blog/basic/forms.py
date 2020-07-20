from django import forms
from .models import codes

class codeForm(forms.ModelForm):
    
    class Meta():
        model = codes
        fields = ('author', 'title', 'text')