from django import forms 
from core.models import Contact 

class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'email-input',
            })
        )

    class Meta:
        model = Contact
        fields = ('full_name','email','number','subject','message')
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'adınızı daxil edin', 'class': 'email-input'}),
            'number': forms.TextInput(attrs={'id': 'number', 'placeholder': 'Əlaqə', 'class': 'email-input'}),
            'subject': forms.TextInput(attrs={'id': 'subject', 'placeholder': 'Subject', 'class': 'email-input'}),
            'message': forms.TextInput(attrs={'id': 'message', 'placeholder': 'Message', 'class': 'message_inp'}),
            
            
            }