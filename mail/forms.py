from django import forms
from .models import Mail

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['subject', 'text', 'mail_adress', 'delay']

        widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.TextInput(attrs={'class':'form-control'}),
            'mail_adress': forms.TextInput(attrs={'class':'form-control'}),
            'delay': forms.NumberInput(attrs={'class':'form-control'}),
        }
