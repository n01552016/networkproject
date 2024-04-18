from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    smtp_sender = forms.EmailField(label='Sender Email')
    smtp_password = forms.CharField(label='SMTP Password', widget=forms.PasswordInput)

    class Meta:
        model = Email
        fields = ['smtp_sender', 'smtp_password', 'receivers', 'cc', 'subject', 'body', 'attachment']
